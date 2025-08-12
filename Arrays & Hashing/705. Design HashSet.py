# Boolean Array
class MyHashSet:

    def __init__(self):
        self.vals = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.vals[key] = True

    def remove(self, key: int) -> None:
        self.vals[key] = False

    def contains(self, key: int) -> bool:
        return self.vals[key]


"""
Brute Force
class MyHashSet:

    def __init__(self):
        self.values = []

    def add(self, key: int) -> None:
        if key not in self.values:
            self.values.append(key)

    def remove(self, key: int) -> None:
        if key in self.values:
            self.values.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.values
"""


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)