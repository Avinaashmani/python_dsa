
## Hashmap function implementation ##

# Hashmap uses a string index
# Hashmap/ Hashtable is a user defiend function, Dictionary is a
# python implementation for the hash function

class hashfunction:

    def __init__(self):
        
        self.max_no = 10
        self.arr = [[] for i in range(self.max_no)]

    def get_hash(self,key):
        hash_key = 0 
        for char in key:
            hash_key = hash_key + ord(char)
        return hash_key % self.max_no
    
    
    def __setitem__(self, key, value):

        hash_func = self.get_hash(key)
        found = False
        
        for i, val in enumerate (self.arr[hash_func]):
            if len(val) >= 2 and val[0] == key:
                self.arr[hash_func][i] = (key, value)
                found = True
                break
        
        if not found:
            self.arr[hash_func].append((key, value))

    def __getitem__(self, key):

        hash_key = self.get_hash(key)
        for i in self.arr[hash_key]:
            if i[0] == key:
                return i[1]

    def __delitem__ (self, key):
        hash_key = self.get_hash(key)

        for idx_no, val in enumerate(self.arr[hash_key]):
            if val[0] == key:
                del self.arr[hash_key][idx_no]

if __name__ == '__main__':

    hash_key = hashfunction()
    
    hash_key['8987n.65223w'] = 'red ball'
    hash_key['9002n.12390w'] = 'blue ball'
    hash_key['0987n.12349w'] = 'blue ball'
    print(hash_key['9002n.12390w'])

    print(hash_key.arr)
