use qlkt_ptn;
INSERT Into `LoaiTB`(`TenLoaiTB`) VALUES ('Máy chủ'),
('Máy để bà'),
('Máy xách tay'),
('Các thiết bị di động'),
('Các thiết bị lập trình nhúng'),
('Các phầm mềm cài đặt trên máy chủ và máy trạm')


INSERT INTO `ThietBi`(`TenTB`, `idLoaiTB`) VALUES ('Máy chủ 1', 1),
('Máy chủ 2', 1),
('Máy chủ 3', 1),
('Máy để bàn 1', 2),
('Máy để bàn 2', 2),
('Máy xách tay 1', 3),
('Máy xách tay 2', 3),
('Thiết bị di động 1',4),
('Thiết bị di động 2',4),
('Thiết bị lập trình nhúng 1',5),
('Thiết bị lập trình nhúng 2',5),
('Phần mềm 1',6),
('Phần mềm 2',6),
('Phần mềm 3',6)

INSERT INTO `GiaoVien`(`TenGV`, `NgaySinh`, `GIoiTinh`, `SDT`) VALUES ('Nguyễn Thị Hiề', '1986-12-12', 1, '0363656740'),
('Nguyễn Quốc Khánh', '1986-12-10', 0, '0363656300'),
('Phan Nguyên Hải', '1985-12-12', 0, '0334567890'),
('Phạm Thị Bích Vâ', '1988-12-12', 1, '0367418330')


INSERT INTO `LopHoc`(`TenLop`, `SoLuongSV`) VALUES ( 'CNTT1', 20),
( 'CNTT2', 17),
( 'BDATTT', 24),
( 'ANHTTT', 23)



INSERT INTO `PhieuDangKySD`(`idLop`,`idGV`, `TenMonHoc`,`TenBaiTN`, `Ngay`, `TietBD`, `TietKT`, `TrangThai`)  VALUES (1,1,'Lập trình tích hợp', 'Bai thi nghiem 1','2022-04-07', 1,3, 1),
(2,2,'Lập trình phần mềm an toà', 'Bai thi nghiem 1', '2022-04-08', 1,3, 1),
(3,3,'Công nghệ phần mềm','Bai thi nghiem 2', '2022-04-08', 2,5, 1),
(3,2,'Lập trình phần mềm an toà', 'Bai thi nghiem 2','2022-04-08', 9,10, 1),
(3,3,'Công nghệ phần mềm', 'Bai thi nghiem 3','2022-04-09', 1,3, 1),
(4,2,'Lập trình phần mềm an toà', 'Bai thi nghiem 3','2022-04-09', 4,6, 1),
(4,3,'Công nghệ phần mềm', 'Bai thi nghiem 2','2022-04-09', 1,3, 1),
(4,4,'Lập trình nâng cao', 'Bai thi nghiem 1','2022-04-09', 7,9, 1)


INSERT INTO `CT_PhieuDK`(`idPhieu`, `idThietBi`) VALUES (1,1),
(1,2),
(1,4),
(1,8),
(1,10),
(2,1),
(2,3),
(2,5),
(3,7),
(3,9),
(4,11),
(5,1),
(6,2),
(7,3),
(8,4)



INSERT INTO `PhieuMuonTra`(`idGV`,  `NgayMuon`, `HanTra`, `TrangThai`)  VALUES (1, '2022-04-01', '2022-04-08' ,0),
(1, '2022-04-01', '2022-04-08' ,0),
(1, '2022-04-01', '2022-04-09' ,0),
(1, '2022-04-01', '2022-04-10' ,0),
(1, '2022-04-02', '2022-04-13' ,0),
(1, '2022-04-03', '2022-04-13' ,0),
(1, '2022-04-03', '2022-04-13' ,0),
(1, '2022-04-04', '2022-04-13' ,0)


INSERT INTO `CT_PhieuMuonTra`(`idPhieuMuon`, `idThietBi`) VALUES (1,1),
(1,2),
(1,4),
(1,8),
(1,10),
(2,1),
(2,3),
(2,5),
(3,7),
(3,9),
(4,11),
(5,1),
(6,2)

