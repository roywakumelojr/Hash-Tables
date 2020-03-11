# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # # Finding the index
        # index = self._hash_mod(key)

        # # Printing out a warning then the information is getting overwritten
        # if self.storage[index] is not None:
        #     print('Warning: The information is getting overwritten')
        # self.storage[index] = LinkedPair(key, value)

        ##### Day 2 Code #####
        index = self._hash_mod(key)
        new_index = LinkedPair(key, value)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = new_index
                return 
            current_index = self.storage[index] 
            while current_index.next is not None:
                if current_index.key == key:
                    current_index = new_index
                    break
                current_index = current_index.next 
            current_index.next = new_index
        else:
            self.storage[index] = new_index

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # # Finding the index.
        # index = self._hash_mod(key)

        # # Print a warning if the index is None.
        # if self.storage[index] is None:
        #     print('Warning: No information was found')
        #     return

        # # Reassign the location of the item being removed to None.
        # self.storage[index] = None

        ##### Day 2 Code #####
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None 
                return 
            else: 
                while self.storage[index].key is not key and self.storage[index] is not None:
                    self.storage[index] = self.storage[index].next
                self.storage[index] = None 
                return
        else:
            print('Warning: No information was found')
            return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # # Finding the index.
        # index = self._hash_mod(key)

        # # Returns the stored value.
        # if self.storage[index] is not None:
        #     if self.storage[index].key == key:
        #         return self.storage[index].value
        #     else:
        #         print('warning: The key does not match')
        #         return None
        # else:
        #     return None

        ##### Day 2 Code #####
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                current_node = self.storage[index]
                while current_node.key is not key and current_node is not None:
                    current_node = current_node.next 
                return current_node.value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # for content in self.storage:
        #     if content is not None:
        #         new_index = self._hash_mod(content.key)
        #         new_storage[new_index] = LinkedPair(content.key, content.value)
        # self.storage = new_storage

        ##### Day 2 Code #####
        self.capacity *= 2
        self.storage = [None] * self.capacity
        new_storage = self.storage

        for content in new_storage:
            if content is None:
                pass
            elif content.next is None: 
                self.insert(content.key, content.value)
            else:
                while content is not None:
                    self.insert(content.key, content.value)
                    content = content.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
