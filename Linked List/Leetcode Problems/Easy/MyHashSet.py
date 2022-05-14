class MyHashSet:

    def __init__(self, val=0, next=None):
        """
        Initialize your data structure here.
        """
        self.hash = []

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# key = int(input("Enter val"))
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
