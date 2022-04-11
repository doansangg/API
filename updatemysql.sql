use qlkt_ptn;

create table LoaiTB (
idLoaiTB int AUTO_INCREMENT PRIMARY KEY, 
TenLoaiTB varchar(50) NULL
);

create table ThietBi (
idThietBi int AUTO_INCREMENT PRIMARY KEY, 
TenTB varchar(50) NULL,
idLoaiTB int,
FOREIGN KEY (idLoaiTB)
      REFERENCES LoaiTB(idLoaiTB)
);

create table LopHoc (
idLop int AUTO_INCREMENT PRIMARY KEY, 
TenLop varchar(50) NULL,
SoLuongSV int NULL
);

create table GiaoVien (
idGV int AUTO_INCREMENT PRIMARY KEY, 
TenGV varchar(50) NULL,
NgaySinh date NULL,
    GioiTinh bit NULL,
    SDT varchar(10)
);

create table PhieuDangKySD (
    
idPhieu int AUTO_INCREMENT PRIMARY KEY, 
    idLop int,
    idGV int,
FOREIGN KEY (idLop)
      REFERENCES LopHoc(idLop),
FOREIGN KEY (idGV)
      REFERENCES GiaoVien(idGV),
TenMonHoc varchar(100) NULL,
    TenBaiTN varchar(100) NULL,
    Ngay date not NULL,
    TietBD int,
    TietKT int,
    TrangThai bit NULL
);

CREATE TABLE CT_PhieuDK(
    idPhieu int references PhieuDangKySD(idPhieu),
    idThietBi int references ThietBi(idThietBi),
	PRIMARY KEY (idPhieu, idThietBi)
);

CREATE TABLE PhieuMuonTra(
	idPhieuMuon int AUTO_INCREMENT PRIMARY KEY,
    idGv int references GiaoVien(idGV),
	NgayMuon date NOT NULL,
	HanTra date NOT NULL,
	TrangThai bit NULL
);

CREATE TABLE CT_PhieuMuonTra(
    idPhieuMuon int references PhieuMuonTra(idPhieuMuon),
    idThietBi int references ThietBi(idThietBi),
	PRIMARY KEY (idPhieuMuon, idThietBi)
);

