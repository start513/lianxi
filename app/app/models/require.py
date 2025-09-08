from typing import List, Any


class Require:
    """
    存放校验条件和响应信息
    """

    def __init__(self):
        self.conditions: List[Any] = []  # 不为空的条件集合
        self.messages: List[str] = []  # 响应信息集合

    def put(self, param: Any, message: str) -> 'Require':
        self.conditions.append(param)
        self.messages.append(message)
        return self

    @staticmethod
    def me() -> 'Require':
        return Require()

    def get(self, index: int) -> Any:
        return self.conditions[index]

    def get_message(self, index: int) -> str:
        return self.messages[index]

    def get_length(self) -> int:
        return len(self.conditions)