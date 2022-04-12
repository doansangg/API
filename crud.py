# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import TBInfoInfoAlreadyExistError, TBInfoNotFoundError
from models import *
from schemas import PaginatedTypeTBInfo, PaginatedTBInfo,LietkeMuonInfo,ND_BTN,LoaiThietBi,ThietBi_Insert,ThietBi_Send, MuonTra


'''
/* liệt kê thiết bị theo chủng loại (truyền id vào)*/
select * from ThietBi where idLoaiTB='1'  
/* -	Liệt kê các thiết bị đang được mượn sắp tới hạn trả (trước 05 ngày)*/
select tenTB, HanTra, TenLoaiTB from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra<= GETDATE() +5 

/* -	Liệt kê các thiết bị đã quá hạn trả*/
select tenTB, HanTra, TenLoaiTB from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra< GETDATE()

/*-	Liệt kê các bài thí nghiệm của giáo viên theo ID của giáo viên đó (truyền id vào)*/
select tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV and  A.idGV=1
'''
#/* liệt kê thiết bị theo chủng loại (truyền id vào)*/
def get_loaithietbi(session: Session) -> List[PaginatedTypeTBInfo]:
    result = session.execute("""select TenLoaiTB from LoaiTB""").all()
    return result

def get_thietbi_chungloai(session: Session, _id: int) -> List[PaginatedTBInfo]:
    if (_id == 0):
        result = session.execute("""select * from ThietBi A, LoaiTB B where A.idLoaiTB = B.idLoaiTB""").all()
    else:
        result = session.execute("""select * from ThietBi A, LoaiTB B where A.idThietBi={} and A.idLoaiTB = B.idLoaiTB""".format(_id)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/* Liệt kê các thiết bị đang được mượn sắp tới hạn trả (trước 05 ngày)*/
def get_muon_toihan(session: Session, n: int) -> List[LietkeMuonInfo]:
    result = session.execute("""select A.idThietBi, tenTB, HanTra, TenLoaiTB, D.idPhieuMuon from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
        where A.idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra<= CURRENT_DATE() + {}""".format(n)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result


#/* -	Liệt kê các thiết bị đã quá hạn trả*/
def get_quahan(session: Session) -> List[LietkeMuonInfo]:
    result = session.execute("""select A.idThietBi, tenTB, HanTra, TenLoaiTB, D.idPhieuMuon from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra< CURRENT_DATE() """).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/*-	Liệt kê các bài thí nghiệm của giáo viên theo ID của giáo viên đó (truyền id vào)*/
def get_baithinghiem(session: Session, _id) -> List[ND_BTN]:
    if (_id == 0):
        result = session.execute("""select tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV """).all()
    else :
        result = session.execute("""select tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV and  A.idGV={}""".format(_id)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/* Insert thiết bị
def Insert_TB(session: Session, ThB:ThietBi_Send) -> ThietBi:
    LoaiTB_Info = session.query(LoaiTB).filter(LoaiTB.TenLoaiTB == ThB.TenLoaiTB).first()
    TB_detail = session.query(ThietBi).filter(ThietBi.TenTB == ThB.TenTB, ThietBi.idLoaiTB == LoaiTB_Info.idLoaiTB).first()
    if TB_detail is not None:
        return TBInfoInfoAlreadyExistError
    # ThietBi_insert = ThietBi_Insert
    # ThietBi_insert.idLoaiTB = LoaiTB_Info.idLoaiTB
    # ThietBi_insert.TenTB = ThB.TenTB
    print(LoaiTB_Info.idLoaiTB)
    new_TB = ThietBi(**{"idLoaiTB":LoaiTB_Info.idLoaiTB,"TenTB":ThB.TenTB})
    session.add(new_TB)
    session.commit()
    session.refresh(new_TB)
    return new_TB

#/* Insert loại thiết bị
def Insert_LTB(session: Session, LTB_insert:LoaiThietBi) -> LoaiTB:
    #print("doan sang")
    LTB_detail = session.query(LoaiTB).filter(LoaiTB.TenLoaiTB == LTB_insert.TenLoaiTB).first()
    if LTB_detail is not None:
        return TBInfoInfoAlreadyExistError
    new_LTB = LoaiTB(**LTB_insert.dict())
    session.add(new_LTB)
    session.commit()
    session.refresh(new_LTB)
    return new_LTB


#/* Đăng kí mượn cho giáo viên

def Insert_MuonTra(session:Session, MT: MuonTra) -> Boolean:
    GV_Detail = session.query(GiaoVien).filter(GiaoVien.TenGV == MT.TenGV).first()
    TB_Detail = session.query(ThietBi).filter(ThietBi.TenTB==MT.TenTB).first()
    print("ten lop: ",MT.TenLop)
    LH_Detail = session.query(LopHoc).filter(LopHoc.TenLop == MT.TenLop).first()
    # print("doan sang")
    # Insert PDKSD
    #new_PDKSD = PhieuDangKySD(**{'idLop':LH_Detail.idLop,'idGV':GV_Detail.idGV, 'TenMonHoc':MT.TenMonHoc,'TenBaiTN':MT.TenBaiTN, 'TietBD':MT.TietBD, 'TietKT':MT.TietKT, 'TrangThai':MT.TrangThai_PDK})
    new_PDKSD = PhieuDangKySD(**{"idLop":LH_Detail.idLop,"idGV":GV_Detail.idGV, "TenMonHoc":MT.TenMonHoc,"TenBaiTN":MT.TenBaiTN, "Ngay":MT.Ngay, "TietBD":MT.TietBD, "TietKT":MT.TietKT, "TrangThai":MT.TrangThai_PDK})
    session.add(new_PDKSD)
    session.commit()
    session.refresh(new_PDKSD)

    #Insert CT_PhieuDk
    new_PDK = CT_PhieuDangKySD(**{"idPhieu":new_PDKSD.idPhieu,"idThietBi":TB_Detail.idThietBi})
    session.add(new_PDK)
    session.commit()
    session.refresh(new_PDK)

    #Insert PhieuMuonTra
    new_PMT = PhieuMuonTra(**{'idGV':GV_Detail.idGV,  'NgayMuon':MT.NgayMuon, 'HanTra':MT.HanTra, 'TrangThai':MT.TrangThai_PMT})
    session.add(new_PMT)
    session.commit()
    session.refresh(new_PMT)

    #Insert CT_PhieuMuonTra
    new_CTPMT = CT_PhieuMuonTra(**{'idPhieuMuon':new_PMT.idPhieuMuon, 'idThietBi':TB_Detail.idThietBi})
    session.add(new_CTPMT)
    session.commit()
    session.refresh(new_CTPMT)
    return True
