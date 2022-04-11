## BackUp database in mysql xampp

## Using FastAPI


* Change config - line 6 in database.py:
```
DATABASE_URL = "mysql+mysqldb://root:@localhost:3307/qlkt_ptn"
```
Run Server:
```
uvicorn --reload main:app
```
### Test API Sever (PostMan)
- http://127.0.0.1:8000/nd_btn?_id=2
- http://127.0.0.1:8000/quahan
- http://127.0.0.1:8000/chungloai?_id=1
- http://127.0.0.1:8000/muon_toihan?n=4

#### post
* Dang ki muon tra: http://127.0.0.1:8000/addDK
```
{
    "TenGV" : "Nguyễn Quốc Khánh",
    "TenBaiTN": "Bai thi nghiem 2",
    "Ngay": "2022-06-08",
    "TrangThai_PDK" : true,
    "TenLop" : "CNTT1",
    "TenTB": "Máy chủ 2",
    "TietBD" : 3,
    "TietKT" : 5,
    "TenMonHoc": "CNPM_DOANSANG",
    "NgayMuon" : "2022-04-01",
    "HanTra" : "2022-04-08",
    "TrangThai_PMT" : false
}
```
* Them Thiet Bi : http://127.0.0.1:8000/addTB
```
{"TenTB" :"Thái Doãn Sang1" ,"TenLoaiTB": "Đỗ Diệp"}
```
* Them loai thiet bi: http://127.0.0.1:8000/addLTB
```
{"TenLoaiTB": "Đỗ Diệp"}
```
