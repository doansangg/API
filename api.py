# api.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_thietbi_chungloai,get_muon_toihan,get_quahan,get_baithinghiem,Insert_LTB,Insert_TB,Insert_MuonTra, get_loaithietbi
from database import get_db
from exceptions import TBInfoException
from schemas import LietkeInfo,LietkeMuonInfo,ND_BTN,LoaiThietBi,ThietBi_Insert,ThietBi_Send,MuonTra, PaginatedTypeTBInfo

router = APIRouter()

# Example of Class based view
@cbv(router)
class TB:
    session: Session = Depends(get_db)

    @router.get("/loaithietbi", response_model=PaginatedTypeTBInfo)
    def list_repo(self):
        list = get_loaithietbi(self.session)
        response = { "data": list }
        return response

    # API to get the list of car info
    @router.get("/chungloai", response_model=LietkeInfo)
    def list_cars(self, _id: int = 0):
        cars_list = get_thietbi_chungloai(self.session, _id)
        print(cars_list)
        response = { "data": cars_list}

        return response

    @router.get("/muon_toihan", response_model=LietkeMuonInfo)
    def list_muon(self, n: int = 1):

        muon_list =get_muon_toihan(self.session, n)
        #print("doan sang")
        print(muon_list)
        response = { "data": muon_list}

        return response

    @router.get("/quahan", response_model=LietkeMuonInfo)
    def list_quahan(self):

        quahan_list =get_quahan(self.session)
        #print("doan sang")
        print(quahan_list)
        response = { "data": quahan_list}

        return response

    @router.get("/nd_btn", response_model=ND_BTN)
    def get_btn(self, _id: int = 0):

        btn_list =get_baithinghiem(self.session,_id)
        #print("doan sang")
        print(btn_list)
        response = { "data": btn_list}

        return response

    @router.post("/addLTB")
    def add_LTB(self,LTB:LoaiThietBi):
        try :
            print("data: ",LTB.TenLoaiTB)
            LTB = Insert_LTB(self.session,LTB)
            return LTB
        except TBInfoException as cie:
            raise HTTPException(**cie.__dict__)

    @router.post("/addTB")
    def add_TB(self,TB:ThietBi_Send):
        try :
            #print("data: ",LTB.TenLoaiTB)
            TB = Insert_TB(self.session,TB)
            return TB
        except TBInfoException as cie:
            raise HTTPException(**cie.__dict__)

    @router.post("/addDK")
    def add_TB(self, MT:MuonTra):
        try :
            #print("data: ",LTB.TenLoaiTB)
            result = Insert_MuonTra(self.session,MT)
            return result
        except TBInfoException as cie:
            raise HTTPException(**cie.__dict__)