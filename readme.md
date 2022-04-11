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