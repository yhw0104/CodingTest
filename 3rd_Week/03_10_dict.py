class Dict:
    def __init__(self):
        self.items = [None] * 8


    # put(key, value) : key 에 value 저장하기
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return


    # get(key) : key 에 해당하는 value 가져오기
    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!