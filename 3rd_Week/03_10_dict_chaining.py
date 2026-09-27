class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())


    # put(key, value) : key 에 value 저장하기
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        return


    # get(key) : key 에 해당하는 value 가져오기
    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index].get(key)


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!