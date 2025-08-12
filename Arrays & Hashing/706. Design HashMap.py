# Array
class MyHashMap:

    def __init__(self):
        self.map = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


"""
Brute Force
class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.values[self.keys.index(key)]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.keys:
            i = self.keys.index(key)
            self.keys.pop(i)
            self.values.pop(i)
"""


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)