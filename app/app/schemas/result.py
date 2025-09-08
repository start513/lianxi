from typing import Optional


class Result:

    def __init__(self, message: str, result: bool):
        self.message = message
        self.result = result

    def get_message(self) -> Optional[str]:
        return self.message

    def set_message(self, message: str) -> None:
        self.message = message

    def is_result(self) -> bool:
        return self.result

    def set_result(self, result: bool) -> None:
        self.result = result


