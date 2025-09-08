from app.schemas.result import Result
from app.schemas.ums_admin_login_param import UmsAdminLoginParam
from app.schemas.ums_admin_param import UmsAdminParam
from app.services.ums_admin_service import UmsAdminService


class UmsAdminApi:

    TOKEN_PREFIX = 'Bearer '

    def __init__(self):
        self.admin_service = UmsAdminService()


    def login(self, ums_admin_login_param: UmsAdminLoginParam):
        """
        管理员登录接口

        Args:
            ums_admin_login_param: 登录参数对象

        Returns:
            Result: 登录结果

        用户名、密码不能为空

        """
        token = self.admin_service.login(ums_admin_login_param.username, ums_admin_login_param.password)
        if token is None:
            return Result('用户名或密码错误', False)
        if "token" in token:
            return Result(self.TOKEN_PREFIX + token, True)
        else:
            return Result(token, False)


    def register(self, ums_admin_param: UmsAdminParam):
        """
        管理员注册接口

        Args:
            ums_admin_param: 注册参数对象

        Returns:
            Result: 注册结果

        用户名、密码和邮箱不能为空
        """
        result = self.admin_service.register(ums_admin_param)
        if result:
            return Result('注册成功', True)

        return Result('注册失败', False)

    def send_phone_code(self, phone: str):
        """
        发送手机验证码接口

        Args:
            phone: 手机号码

        Returns:
            Result: 发送结果

        输入手机号，生成4位验证码
        """
        result = self.admin_service.send_phone_code(phone)
        if len(result) < 4:
            return Result(result, False)

        return Result(result, True)

    def validate_phone_code(self, phone: str, code: str):
        """
        验证手机验证码接口

        Args:
            phone: 手机号码
            code: 验证码

        Returns:
            Result: 验证结果

        使用手机号和验证码进行校验
        """
        result = self.admin_service.validate_phone_code(phone, code)
        if len(result) < 5:
            return Result(result, False)

        return Result(result, True)