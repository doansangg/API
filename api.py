# api.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from pymysql import Date
from sqlalchemy.orm import Session
from crud import get_tengiaovien, get_thietbi_chungloai,get_tenthietbi, get_tenlop, Edit_TB, delete_MuonTra,\
                    get_muon_toihan,get_quahan,get_baithinghiem,Insert_LTB,Insert_TB,Insert_MuonTra,\
                    get_dangchomuon,get_khaithacthietbiphong,get_khaithacthoigian, get_tenloaithietbi, edit_MuonTra
            
from database import get_db
from exceptions import TBInfoException
from schemas import LietkeInfo,LietkeMuonInfo,ND_BTN,LoaiThietBi,PaginatedClasses,ThietBi_Edit,DangKy_Edit,\
                        ThietBi_Send,MuonTra,Lietke_DKM,Lietke_KhaiThac,Lietke_KTP, PaginatedTypeTBInfo, PaginatedGiaoVien

router = APIRouter()


# Example of Class based view
@cbv(router)
class TB:
    session: Session = Depends(get_db)

    # API to get the list of chungloai info
    @router.get("/chungloai", response_model=LietkeInfo)
    def list_s(self, _id: int = 1):

        chungloai_list = get_thietbi_chungloai(self.session, _id)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}

        return response

    @router.get("/lietkethoigian", response_model=Lietke_KhaiThac)
    def list_thoigian(self, Date_BD:str, Date_KT:str):

        chungloai_list = get_khaithacthoigian(self.session, Date_BD,Date_KT)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response

    @router.get("/lietketbphong", response_model=Lietke_KTP)
    def list_phong(self, Date_BD:str, Date_KT:str):

        chungloai_list = get_khaithacthietbiphong(self.session, Date_BD,Date_KT)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response

    @router.get("/lietkedangchomuon", response_model=Lietke_DKM)
    def list_dangmuon(self):

        chungloai_list = get_dangchomuon(self.session)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
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
    def get_btn(self, _id: int = 1):

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
    def add_TB1(self,TB:ThietBi_Send):
        # TB = Insert_TB(self.session,TB)
        # return TB
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

    @router.get("/laytenltb", response_model=PaginatedTypeTBInfo)
    def list_tenltb(self):

        chungloai_list = get_tenloaithietbi(self.session)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response
    
    @router.get("/laytenlop", response_model=PaginatedClasses)
    def list_tenlop(self):

        chungloai_list = get_tenlop(self.session)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response

    @router.get("/laytenthietbi")
    def list_tenthietbi(self):

        chungloai_list = get_tenthietbi(self.session)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response
    
    @router.get("/laytengiaovien", response_model=PaginatedGiaoVien)
    def list_tengiaovien(self):

        chungloai_list = get_tengiaovien(self.session)
        #print("doan sang")
        print(chungloai_list)
        response = { "data": chungloai_list}
        return response

    @router.delete('/deleteDK')
    def delete_DK(self, id: int):
        try :
            #print("data: ",LTB.TenLoaiTB)
            result = delete_MuonTra(self.session,id)
            return result
        except TBInfoException as cie:
            raise HTTPException(**cie.__dict__)


    # Api to update device
    @router.put('/chungloai')
    def update_device(self, TB: ThietBi_Edit):
        thietbi = Edit_TB(self.session, TB)
        response = { "data": thietbi}

        return response

    # Api to update phieudangky
    @router.put('/dangky')
    def update_dangky(self, dangky: DangKy_Edit):
        dangkyedit = edit_MuonTra(self.session, dangky)
        response = { "data": dangkyedit}

        return response