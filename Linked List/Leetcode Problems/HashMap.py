class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_: dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.dict_.update({key: value})

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.dict_.keys():
            return self.dict_.get(key)
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.dict_.keys():
            self.dict_.pop(key)

    def print(self):
        print(self.dict_)

# Your MyHashMap object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyHashMap()
    key1 = int(input('Enter key: '))
    value1 = int(input('Enter value: '))
    obj.put(key1, value1)

    key2 = int(input('Enter key: '))
    value2 = int(input('Enter value: '))
    obj.put(key2, value2)

    key_get = int(input('Enter key get: '))

    param_2 = obj.get(key_get)
    print(param_2)
    key_ = int(input('Enter key to be deleted: '))
    obj.remove(key_)
    obj.print()
