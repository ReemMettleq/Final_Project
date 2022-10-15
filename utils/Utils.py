class Constants:
    ACTIVE = 1
    EXPIRED = 2
    CANCELED = 3


class MethodsUtils:

    @staticmethod
    def check_value_is_empty(*value: str):
        for item in value:
            if item.isspace() or item =="":
                return True

