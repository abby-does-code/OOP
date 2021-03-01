##Create a class called Course that contains Title, CRN, Capacity, and Code


class Course:
    def __init__(self, title, num, capacity, code):
        self.__class_title = title
        self.__class_CRN = num
        self.__class_capacity = capacity
        self.__class_code = code

    def get_CRN(self, num):
        return self.__class_CRN

    def get_capacity(self, capacity):
        return self.__class_capacity
