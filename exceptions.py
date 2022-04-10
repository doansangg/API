# exceptions.py
class TBInfoException(Exception):
    ...


class TBInfoNotFoundError(TBInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Không thể thực thi lệnh"


class TBInfoInfoAlreadyExistError(TBInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Sẵn sang thoát"
