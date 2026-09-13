# list = [1,2,3,4,5]
# print(list[1])
# print(type(list))

# import array as arr
# array_1 = arr.array("i", [2, 4, 6, 8])
# print(array_1[1])
# print(type(array_1))


class Person:
    def __init__(self, name):
        self.name = name
        print("hihi my name is ", name)

    def talk(self):
        print("내이름은",self.name , "입니다.")


person_1 = Person("철수")
person_1.talk()

person_2 = Person("영희")
person_2.talk()
