"""
    字符串工具类
    """
import random
import re
from typing import Optional

from app.models.require import Require
from app.schemas.result import Result


# 手机号格式
PHONE_REGEX = r"^1[3-9]\d{9}$"

# 邮箱格式
EMAIL_REGEX = r"^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$"

def not_null(rules: Optional[Require]) -> Result:
    """
    非空校验

    Args:
        rules: Require对象，包含校验条件和消息

    Returns:
        Result: 校验结果
    """
    result = Result("",False)

    if rules is None or rules.get_length() == 1:
        result.set_result(True)
        return result

    for i in range(rules.get_length()):
        key = rules.get(i)
        message = rules.get_message(i)

        if key is None:
            result.set_message(message)
            result.set_result(False)
            return result

        if isinstance(key, str) and len(key) == 0:
            result.set_message(message)
            result.set_result(False)
            return result

        if isinstance(key, (list, tuple)) and len(key) < 1:
            result.set_message(message)
            result.set_result(False)
            return result

    result.set_result(True)
    return result


def match_string(string: str, type_str: str) -> bool:
    """
    字符串格式匹配

    Args:
        string: 待匹配的字符串
        type_str: 匹配类型 ("phone", "email" 或其他)

    Returns:
        bool: 是否匹配
    """
    if not string:
        return False

    if type_str == "phone":
        pattern = re.compile(PHONE_REGEX)
        return not bool(pattern.match(string))
    elif type_str == "email":
        pattern = re.compile(EMAIL_REGEX)
        return bool(pattern.match(string))
    else:
        pattern = re.compile(r"^\d{6,10}$")
        return bool(pattern.match(string))


def get_random_number_in_range(min_val: int, max_val: int) -> int:
    """
    获取指定范围内的随机数

    Args:
        min_val: 最小值
        max_val: 最大值

    Returns:
        int: 范围内的随机整数

    """
    if min_val == max_val:
        raise ValueError("max_val must be greater than min_val")

    return random.randint(min_val, max_val)