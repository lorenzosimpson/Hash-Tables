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
        self.count = 0

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
        # # if collision
        # if self.storage[index] is None:
        #     self.storage[index] = LinkedPair(key, value)

        #hash key to find indexof self.storage
        index = self._hash_mod(key)

        #check if None
        if self.storage[index] is None:
            #add linkedPair
            self.storage[index] = LinkedPair(key, value)
        #else
        else:
            #create new LinkedPair
            new_pair = LinkedPair(key, value)
            #add it to head
            new_pair.next = self.storage[index]
            #self.storage[0] = mew LinkedPair
            self.storage[index] = new_pair
            

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        next_pair = None

        # hash the key
        # if none, do nothing - nothing to remove
        while pair is not None and pair.key is not key:
            next_pair = pair
            pair = next_pair.next # keep moving
            
        if pair is None:
            print('Warning: nothing to remove there')
        # else
        else:
            # loop through to find the key
            # if found at the root, no pointers to worry about
            if next_pair is None:
                self.storage[index] = pair.next
                # if it's found at the end
            elif pair.next == None and next_pair is not None:
                next_pair.next = None
                # else - it's found in the middle
            else:
                next_pair.next = pair.next
                    

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        while pair is not None:
            if pair.key == key:
                return pair.value
            pair = pair.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        new_storage = [None] * self.capacity
        self.storage = new_storage

        for i in range(len(old_storage)):
            if old_storage[i] is not None:
                pair = old_storage[i]
                while pair != None:
                    self.insert(pair.key, pair.value)
                    pair = pair.next

            


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
 
    print(ht.storage)

    
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
