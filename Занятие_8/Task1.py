class Date:
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def extraction(cls, data_str):
        day, month, year = map(int, data_str.split('-'))
        return day, month, year

    @staticmethod
    def validation(data_str):
        day, month, year = Date.extraction(data_str)
        if 0 < day <= 31 and 0 < month <= 12 and 1900 < year <= 2100:
            print(data_str)
        else:
            print("Некорректно введена дата")

date = Date('12-10-2020')
Date.validation(date.data_str)