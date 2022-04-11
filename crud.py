# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import TBInfoInfoAlreadyExistError, TBInfoNotFoundError
from models import *
from schemas import PaginatedTBInfo,LietkeMuonInfo,ND_BTN


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
def get_thietbi_chungloai(session: Session, _id: int) -> List[PaginatedTBInfo]:
    result = session.execute("""select * from ThietBi where idLoaiTB={}""".format(_id)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/* Liệt kê các thiết bị đang được mượn sắp tới hạn trả (trước 05 ngày)*/
def get_muon_toihan(session: Session, n: int) -> List[LietkeMuonInfo]:
    result = session.execute("""select tenTB, HanTra, TenLoaiTB from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
        where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra<= CURRENT_DATE() + {}""".format(n)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result


#/* -	Liệt kê các thiết bị đã quá hạn trả*/
def get_quahan(session: Session) -> List[LietkeMuonInfo]:
    result = session.execute("""select tenTB, HanTra, TenLoaiTB from ThietBi A, LoaiTB B, CT_PhieuMuonTra C, PhieuMuonTra D
where A. idThietBi= C.idThietBi and C.idPhieuMuon= D.idPhieuMuon and A.idLoaiTB=B.idLoaiTB and D.TrangThai=0 and HanTra< CURRENT_DATE() """).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result

#/*-	Liệt kê các bài thí nghiệm của giáo viên theo ID của giáo viên đó (truyền id vào)*/
def get_baithinghiem(session: Session,_id) -> List[ND_BTN]:
    result = session.execute("""select tenBaiTN, tenGV from PhieuDangKySD A, GiaoVien B where A.idGV=B.idGV and  A.idGV={}""".format(_id)).all()
    if result is None:
        raise TBInfoNotFoundError
    print(result)
    return  result