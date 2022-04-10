#from datetime import date as date
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, Boolean, Date
from database import Base
import enum
from sqlalchemy import ForeignKey
from pydantic import BaseModel

# bảng loại thiết bị
class LoaiTB(Base):
    __tablename__ = "loaitb"

    idLoaiTB = Column(Integer, primary_key=True, index=True)
    TenLoaiTB = Column(String)

# bảng thiết bị
class ThietBi(Base):
    __tablename__ = "thietbi"

    idThietBi = Column(Integer, primary_key=True, index=True)
    TenTB = Column(String)
    idLoaiTB = Column(ForeignKey('loaitb.idLoaiTB'), index=True)

# bảng lớp học
class LoaiTB(Base):
    __tablename__ = "lophoc"

    idLopHoc = Column(Integer, primary_key=True, index=True)
    TenLop = Column(String)
    SoLuongSV = Column(String)

# bảng giáo viên
class GiaoVien(Base):
    __tablename__ = "giaovien"

    idGV = Column(Integer, primary_key=True, index=True)
    TenGV = Column(String)
    NgaySinh = Column(Date)
    GioiTinh = Column(Boolean)
    SDT = Column(String)

# bảng phiếu đăng kí SD
class PhieuDangKySD(Base):
    __tablename__ = "phieudangkisd"

    idPhieu = Column(Integer, primary_key=True, index=True)
    TenBaiTN = Column(String)
    Ngay = Column(Date)
    TrangThai = Column(Boolean)
    idLop = Column(ForeignKey('lophoc.idLop'), index=True)
    idGV = Column(ForeignKey('giaovien.idGV'), index=True)

# bảng chi tiết phiếu đăng kí
class CT_PhieuDangKySD(Base):
    __tablename__ = "ct_phieudk"

    idPhieu = Column(Integer, primary_key=True)
    idThietBi = Column(Integer, primary_key=True)
    idPhieu = Column(ForeignKey('phieudangkisd.idPhieu'), index=True)
    #idThietBi = Column(ForeignKey('thietbi.idThietBi'), index=True)

# bảng phiểu mượn trả
class PhieuMuonTra(Base):
    __tablename__ = "phieumuontra"

    idPhieuMuon = Column(Integer, primary_key=True, index=True)
    NgayMuon = Column(Date)
    HanTra = Column(Date)
    TrangThai = Column(Boolean)
    idGV = Column(ForeignKey('giaovien.idGV'), index=True)

# bảng chi tiết phiếu mượn trả
class CT_PhieuMuonTra(Base):
    __tablename__ = "ct_phieumuontra"

    idPhieuMuon = Column(Integer, primary_key=True, index=True)
    idThietBi = Column(Integer, primary_key=True, index=True)
    idPhieu = Column(ForeignKey('phieumuontra.idPhieuMuon'), index=True)
    idThietBi = Column(ForeignKey('thietbi.idThietBi'), index=True)