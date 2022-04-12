# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import TBInfoInfoAlreadyExistError, TBInfoNotFoundError
from models import *
from schemas import PaginatedTypeTBInfo, PaginatedTBInfo,LietkeMuonInfo, PaginatedClasses, Lietke_KhaiThac, DangKy_Edit,\
                    ND_BTN,LoaiThietBi,ThietBi_Edit,ThietBi_Send, MuonTra, PaginatedGiaoVien, Lietke_DKM,Lietke_KTP

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

/*Báo cáo khai thác thiết bị theo thời gian: truyền ngày vào*/
select idPhieu, TenGV,TenLop,  Ngay, TietBD, TietKT from PhieuDangKySD A, LopHoc B, GiaoVien C where A.idLop=B.idLop and A.idGV=C.idGV
and Ngay between '2022-04-08' and '2022-04-14'

/*Báo cáo khai thác thiết bị của phòng (được đăng ký sử dụng)*/
select B.idThietBi, TenTB, TenGV, Ngay, TietBD, TietKT from CT_PhieuDK A, ThietBi B, PhieuDangKySD C, GiaoVien D where A.idThietBi=B.idThietBi and A.idPhieu=C.idPhieu
and C.idGV=D.idGV and Ngay between '2022-04-08' and '2022-04-14'

/* Báo cáo danh sách thiết bị đang cho mượn*/
select B.idThietBi, TenTB, TenLoaiTB, NgayMuon, HanTra from CT_PhieuMuonTra A, ThietBi B, PhieuMuonTra C, LoaiTB D where A.idThietBi=B.idThietBi and A.idPhieuMuon=C.idPhieuMuon
and B.idLoaiTB=D.idLoaiTB and TrangThai= 0 

'''
#/* liệt kê thiết bị theo chủng loại (truyền id vào)*/
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
        where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and CURRENT_DATE() <= HanTra and HanTra<= CURRENT_DATE() + {}""".format(n)).all()
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
def get_baithinghiemGV(session: Session,_id) -> List[ND_BTN]:     
    result = session.execute("""select A.idPhieu, tenMonHoc, tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV and  A.idGV={}""".format(_id)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/*-	Liệt kê các bài thí nghiệm của tất cả giáo viên (hoặc theo id bài thí nghiệm)*/
def get_baithinghiem(session: Session,_id) -> List[ND_BTN]:
    if (_id == 0):
        result = session.execute("""select A.idPhieu, tenMonHoc, tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV """).all()
    else :
        result = session.execute("""select A.idPhieu, tenMonHoc, tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV and  A.idPhieu={}""".format(_id)).all()
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
    # #print(ThietBi_insert)
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
    print("ten lop: ",MT.TenLop)
    LH_Detail = session.query(LopHoc).filter(LopHoc.TenLop == MT.TenLop).first()
    #Insert PhieuMuonTra
    new_PMT = PhieuMuonTra(**{'idGV':GV_Detail.idGV,  'NgayMuon':MT.NgayMuon, 'HanTra':MT.HanTra, 'TrangThai':MT.TrangThai_PMT})
    session.add(new_PMT)
    session.commit()
    session.refresh(new_PMT)

    new_PDKSD = PhieuDangKySD(**{"idLop":LH_Detail.idLop,"idGV":GV_Detail.idGV, "TenMonHoc":MT.TenMonHoc,"TenBaiTN":MT.TenBaiTN, "Ngay":MT.Ngay, "TietBD":MT.TietBD, "TietKT":MT.TietKT, "TrangThai":MT.TrangThai_PDK})
    session.add(new_PDKSD)
    session.commit()
    session.refresh(new_PDKSD)

    for index in MT.TenTB:
        TB_Detail = session.query(ThietBi).filter(ThietBi.TenTB==index).first()       
        # print("doan sang")
        # Insert PDKSD
        #new_PDKSD = PhieuDangKySD(**{'idLop':LH_Detail.idLop,'idGV':GV_Detail.idGV, 'TenMonHoc':MT.TenMonHoc,'TenBaiTN':MT.TenBaiTN, 'TietBD':MT.TietBD, 'TietKT':MT.TietKT, 'TrangThai':MT.TrangThai_PDK})
        
        #Insert CT_PhieuDk
        new_PDK = CT_PhieuDangKySD(**{"idPhieu":new_PDKSD.idPhieu,"idThietBi":TB_Detail.idThietBi})
        session.add(new_PDK)
        session.commit()
        session.refresh(new_PDK)
     
        #Insert CT_PhieuMuonTra
        new_CTPMT = CT_PhieuMuonTra(**{'idPhieuMuon':new_PMT.idPhieuMuon, 'idThietBi':TB_Detail.idThietBi})
        session.add(new_CTPMT)
        session.commit()
        session.refresh(new_CTPMT)
    return True

#/* Insert loại thiết bị
def LietKe_TB(session: Session, LTB_insert:LoaiThietBi) -> LoaiTB:
    #print("doan sang")
    LTB_detail = session.query(LoaiTB).filter(LoaiTB.TenLoaiTB == LTB_insert.TenLoaiTB).first()
    if LTB_detail is not None:
        return TBInfoInfoAlreadyExistError
    new_LTB = LoaiTB(**LTB_insert.dict())
    session.add(new_LTB)
    session.commit()
    session.refresh(new_LTB)
    return new_LTB


# Liệt kê khai thác theo thời gian
def get_khaithacthoigian(session: Session, Date_BD: str,Date_KT: str) -> List[Lietke_KhaiThac]:
    result = session.execute("""select idPhieu, TenGV,TenLop,  Ngay, TietBD, TietKT from PhieuDangKySD A, LopHoc B, GiaoVien C where A.idLop=B.idLop and A.idGV=C.idGV
and Ngay between {} and + {}""".format(Date_BD,Date_KT)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Liệt kê khai thác thiết bị phòng
def get_khaithacthietbiphong(session: Session, Date_BD: str,Date_KT: str) -> List[Lietke_KTP]:
    result = session.execute("""select B.idThietBi, TenTB, TenGV, Ngay, TietBD, TietKT from CT_PhieuDK A, ThietBi B, PhieuDangKySD C, GiaoVien D where A.idThietBi=B.idThietBi and A.idPhieu=C.idPhieu
and C.idGV=D.idGV and Ngay between {} and {}""".format(Date_BD,Date_KT)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Liệt kê các thiết bị đang cho mượn
def get_dangchomuon(session: Session) -> List[Lietke_DKM]:
    result = session.execute("""select B.idThietBi, TenTB, TenLoaiTB, NgayMuon, HanTra from CT_PhieuMuonTra A, ThietBi B, PhieuMuonTra C, LoaiTB D where A.idThietBi=B.idThietBi and A.idPhieuMuon=C.idPhieuMuon
and B.idLoaiTB=D.idLoaiTB and TrangThai= 0 """).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Lấy danh sách tên thiết bị
def get_tenloaithietbi(session: Session) -> List[PaginatedTypeTBInfo]:
    result = session.execute("""select TenLoaiTB from LoaiTB""").all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Lấy danh sách lớp
def get_tenlop(session: Session) -> List[PaginatedClasses]:
    result = session.execute("""select idLop, TenLop from LopHoc""").all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Lấy danh sách thiết bị
def get_tenthietbi(session: Session):
    result = session.execute("""select TenTB from ThietBi""").all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

# Lấy danh sách giáo viên
def get_tengiaovien(session: Session) -> List[PaginatedGiaoVien]:
    result = session.execute("""select idGV, TenGV from GiaoVien""").all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/* Edit thiết bị
def Edit_TB(session: Session, ThB:ThietBi_Edit) -> ThietBi:
    Loai = session.query(LoaiTB).filter(LoaiTB.TenLoaiTB == ThB.TenLoaiTB).first()
    TB_detail = session.query(ThietBi).filter(ThietBi.idThietBi == ThB.idTB).first()
    if TB_detail is None:
        return TBInfoNotFoundError
    TB_detail.idThietBi = TB_detail.idThietBi
    TB_detail.TenTB = ThB.TenTB
    TB_detail.idLoaiTB = Loai.idLoaiTB
    session.commit()
    return 'success'

#/* Xóa phiếu mượn
def delete_MuonTra(session:Session, id: int) -> Boolean:
    phieudangky = session.query(PhieuDangKySD).filter(PhieuDangKySD.idPhieu == id).first()
    phieumuontra = session.query(PhieuMuonTra).filter(PhieuMuonTra.idPhieuMuon == id).first()
    ct_phieu = session.query(CT_PhieuDangKySD).filter(CT_PhieuDangKySD.idPhieu == id).all()
    ct_phieutra = session.query(CT_PhieuMuonTra).filter(CT_PhieuMuonTra.idPhieuMuon == id).all()
    session.delete(phieudangky)
    session.delete(phieumuontra)
    for ct in ct_phieu:
        session.delete(ct)
    for ct in ct_phieutra:
        session.delete(ct)
    session.commit()
    return True

#/* Sửa thông tin phiếu đăng ký
def edit_MuonTra(session:Session, dangky: DangKy_Edit):
    DK_detail = session.query(PhieuDangKySD).filter(PhieuDangKySD.idPhieu == dangky.idPhieu).first()
    if DK_detail is None:
        return TBInfoNotFoundError
    DK_detail.TenGV = dangky.TenGV
    DK_detail.TenBaiTN = dangky.TenBaiTN
    DK_detail.TietBD = dangky.TietBD
    DK_detail.TietKT = dangky.TietKT
    DK_detail.TenMonHoc = dangky.TenMonHoc
    DK_detail.HanTra = dangky.HanTra
    session.commit()
    return 'success'