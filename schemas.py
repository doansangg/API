# schemas.py
from datetime import date
from pydantic import BaseModel
from typing import Optional, List


# TO support creation and update APIs
class CRLoaiTB(BaseModel):
    __tablename__ = "loaitb"

    
    TenLoaiTB : str


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
    tenTB: str
    HanTra: date
    TenLoaiTB:str

class LietkeMuonInfo(BaseModel):
    data: List[Muon_ToiHan]

# liệt kê các bài thí nghiệm theo tên giáo viên
# TO support list and get APIs
class Get_BTN(BaseModel):
    tenBaiTN:str
    tenGV:str

class ND_BTN(BaseModel):
    data: List[Get_BTN]