class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1
        if self.count / self.size > 0.7:
            self.resize()

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False

    def resize(self):
        new_table = [[] for _ in range(2 * self.size)]
        old_table = self.table
        self.table = new_table
        self.size *= 2
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

# Sample test
if __name__ == "__main__":
    h = HashTable()
    h.insert("apple", 100)
    h.insert("banana", 200)
    print("Search 'apple':", h.search("apple"))
    print("Search 'banana':", h.search("banana"))
    h.delete("apple")
    print("Search 'apple' after deletion:", h.search("apple"))