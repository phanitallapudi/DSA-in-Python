class HashTable:
    def __init__(self):
        self.hash_table = {}
    
    def __repr__(self) -> str:
        return str(self.hash_table)
    
    def add(self, key, value):
        if key in self.hash_table:
            return False
        self.hash_table[key] = value
        return True
    
    def get(self, key):
        if key not in self.hash_table:
            return None
        return self.hash_table[key]
    
    def set(self, key, value):
        if key not in self.hash_table:
            return False
        self.hash_table[key] = value
        return True
    
    def delete(self, key):
        return self.hash_table.pop(key, False) is not False
    