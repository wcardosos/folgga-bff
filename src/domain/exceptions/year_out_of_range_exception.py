class YearOutOfRangeException(Exception):
    def __init__(self, year: int):
        super().__init__(f"The year {year} is out of range")