# schemas.py
from datetime import date
from xmlrpc.client import Boolean
from pydantic import BaseModel
from typing import Optional, List

from pymysql import Date

#############################
class GiaoVien(BaseModel):
    __tablename__ = "giaovien"

    idGV: int
    TenGV: str

class PaginatedGiaoVien(BaseModel):
    data: List[GiaoVien]

#####################################333
class Lop(BaseModel):
    __tablename__ = "lophoc"

    idLop: int
    TenLop: str

class PaginatedClasses(BaseModel):
    data: List[Lop]

# TO support creation and update APIs
class CRLoaiTB(BaseModel):
    __tablename__ = "loaitb"

    
    TenLoaiTB : str

# To support list TB API
class PaginatedTypeTBInfo(BaseModel):
    data: List[CRLoaiTB]
    # class Config:
    #     orm_mode = True

# TO support list and get APIs
class TB(CRLoaiTB):
    idLoaiTB : int

    class Config:
        orm_mode = True

# To support list TB API
class PaginatedTBInfo(BaseModel):
    data: List[TB]
    # class Config:
    #     orm_mode = True

# liệt kê thiết bị theo chủng loại (truyền id vào)
# TO support creation and update APIs
class ChungLoaiTB(BaseModel):
    __tablename__ = "thietbi"
    TenTB : str
    idLoaiTB : int
    TenLoaiTB: str

# TO support list and get APIs
class ThB(ChungLoaiTB):
    idThietBi : int

    class Config:
        orm_mode = True
# To support list TB API
class LietkeInfo(BaseModel):
    data: List[ThB]


# liệt kê thiết bị tới hạn mượn (truyền n nagyf và vào)
# TO support list and get APIs
class Muon_ToiHan(BaseModel):
    idThietBi: int
    idPhieuMuon: int
    tenTB: str
    HanTra: date
    TenLoaiTB:str

class LietkeMuonInfo(BaseModel):
    data: List[Muon_ToiHan]

# liệt kê các bài thí nghiệm theo tên giáo viên
# TO support list and get APIs
class Get_BTN(BaseModel):
    idPhieu: int
    tenMonHoc: str
    tenBaiTN:str
    tenGV:str

class ND_BTN(BaseModel):
    data: List[Get_BTN]


#Insert loại thiết bị
class LoaiThietBi(BaseModel):
    TenLoaiTB : str

#Insert bảng thiết bị
class ThietBi_Insert(BaseModel):
    TenTB : str
    idLoaiTB : int

class ThietBi_Send(BaseModel):
    TenTB : str
    TenLoaiTB : str

#Update bảng thiết bị
class ThietBi_Edit(BaseModel):
    idTB: int
    TenTB : str
    TenLoaiTB : str
    
#Insert PhieuMuonTra
class MuonTra(BaseModel):
    TenGV : str
    TenBaiTN: str
    Ngay: Date
    TrangThai_PDK : Boolean
    TenLop : str
    TenTB: List[str]
    TietBD : int
    TietKT : int
    TenMonHoc: str
    NgayMuon : Date
    HanTra : Date
    TrangThai_PMT : Boolean

#Insert chitietmuontra
class CT_MuonTra(BaseModel):
    idPhieu: str
    idThietBi: List[str]
    
#Update Phieu Dang ky
class DangKy_Edit(BaseModel):
    idPhieu: int
    TenGV : str
    TenBaiTN: str
    TietBD : int
    TietKT : int
    TenMonHoc: str
    HanTra : Date

# liệt kê khai thác thiết bị theo thời gian
# TO support creation and update APIs
class KhaiThac(BaseModel):
    idPhieu: int
    TenGV: str
    TenLop: str
    Ngay: Date
    TietBD:int
    TietKT: int

class Lietke_KhaiThac(BaseModel):
    data: List[KhaiThac]

# liệt kê khai thác thiết bị của phòng
# TO support creation and update APIs
class DangKiSuDung(BaseModel):
    idThietBi: int
    TenTB : str
    TenGV : str
    Ngay : Date
    TietBD : int
    TietKT : int

class Lietke_KTP(BaseModel):
    data: List[DangKiSuDung]

# liệt kê danh thiết bị đang cho mượn
class DangMuon(BaseModel):
    idThietBi: int
    TenTB : str
    TenLoaiTB : str
    NgayMuon : Date
    HanTra :Date

class Lietke_DKM(BaseModel):
    data: List[DangMuon]
