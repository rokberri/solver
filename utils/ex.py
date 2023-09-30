class WrongСoefficientException(Exception):
    def __init__(self, text="Ошибка в задании коэфицентов. Их сумма должна быть равна 1"):
        self.txt = text
