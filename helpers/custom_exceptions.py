class BigNumberError(Exception):
    """Custom exception for task 3_1"""
    def __init__(self, str, n):
        super().__init__(f"{n} is invalid value for n. n must be less than or equal {len(str)}")

