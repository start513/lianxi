from app.crud.ums_admin import UmsAdmin
from app.models.require import Require
from app.models.ums_admin import UmsAdmin as AdminModel
from app.schemas.result import Result
from app.schemas.ums_admin_param import UmsAdminParam
import app.utils.string_utils as utils

phone_code = {}

class UmsAdminService:

    def __init__(self):
        self.ums_admin_curd = UmsAdmin()


    def login(self, username: str, password: str):

        result = utils.not_null(Require.me().put(username, "用户名不能为空!").put(password, "密码不能为空!"))

        if not result.is_result():
            return result.message

        admin = self.ums_admin_curd.get_admin(username, password)
        if not admin:
            return None

        if admin.status != 1:
            return "账号已禁用，无法登录！"

        return "token" + str(admin.user_id) + ":" + admin.username

    def register(self, ums_admin_param: UmsAdminParam):
        admin = self.ums_admin_curd.get_admin_by_username(ums_admin_param.username)
        if not admin:
            return None

        ums_admin = AdminModel(username=ums_admin_param.username,
                             password=ums_admin_param.password,
                             email=ums_admin_param.email,
                             nick_name=ums_admin_param.nick_name,
                             status=1)
        result = self.ums_admin_curd.insert(ums_admin)
        if result == 1:
            return ums_admin

        return None


    def send_phone_code(self, phone: str):
        result = utils.not_null(Require.me().put(phone, "手机号不能为空!"))
        if not result.is_result():
            return result

        if not utils.match_string(phone, "phone"):
            return "手机号码格式不正确"

        code = utils.get_random_number_in_range(000, 999)
        phone_code[phone] =  code
        return str(code)

    def validate_phone_code(self, phone: str, code: str):
        result = utils.not_null(Require.me().put(phone, "手机号不能为空!"))
        if not result.is_result():
            return result

        if not utils.match_string(phone, "phone"):
            return "手机号码格式不正确"

        if phone_code.get(phone) != code:
            return "验证码错误"
        return "验证成功"