import csv

import allure

from app.schemas.ums_admin_login_param import UmsAdminLoginParam
from app.api.ums_admin_api import UmsAdminApi
import pytest


def read(path):
    with open(path,"r",encoding="UTF-8") as f:
        data=csv.reader(f)
        list=[]
        next(data)
        for i in data:
            list.append(i)
        return list

class TestLogin:
    @pytest.mark.parametrize("username,password,res,res1",read("../resource/login_data.csv"))
    def test_login(self,username,password,res,res1):
        with allure.step("创建用户对象"):
            user =UmsAdminLoginParam(username,password)
        with allure.step("调用登录方法"):
            ass=UmsAdminApi().login(user).message
            ass1=UmsAdminApi().login(user).result
        with allure.step("断言"):
            assert res == ass
            assert bool(res1) == ass1
