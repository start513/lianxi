from enum import Enum

class ResultCode(Enum):
    SUCCESS = (200, "操作成功"),
    FAILED = (500, "操作失败"),
    VALIDATE_FAILED = (404, "参数检验失败"),
    UNAUTHORIZED = (401, "暂未登录或token已经过期"),
    FORBIDDEN = (403, "没有相关权限")

    def get_code(self):
        return self.value[0]

    def get_msg(self):
        return self.value[1]

    def get_result(self):
        return {
            'code': self.value[0],
            'msg': self.value[1]
        }