# A node class with pointers to next and prev nodes. Stores the key and value
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None
        self.prev = None

# Doubly linked list class with behaviors similar to a queue
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0

    # Returns the size of the list
    def get_size(self):
        return self.size

    # Adds a new node to the front of the list 
    def add(self, new_node):

        # If the list is empty, set the node to be equal to the head and the tail 
        if self.head == None:
            self.head = new_node
            self.tail = self.head

        # If the list is not empty, inserts the head in front 
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def remove_last_helper(self):
        
        # The tail now points to the tail's previous node
        self.tail = self.tail.prev

        # If there is only one node
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None

    # Removes a node from the back of the list
    def remove_last(self):

        # If the size is 0, return 
        if self.get_size() == 0:
            return

        # Saves the last node to be removed
        deleted_node = self.tail

        self.remove_last_helper()

        self.size -= 1
        return deleted_node

    # Removes specified node 
    def remove_node(self, node):

        if self.get_size() == 0:
            return

        # If the node is in the middle
        if node != self.tail and node != self.head:
            node.prev.next = node.next
            node.next.prev = node.prev

        # If the node is at the back
        elif node == self.tail:
            self.remove_last_helper()

        self.size -= 1
        

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = DoublyLinkedList()
        self.storage = {}

    # Moves the node to the front of the list
    def reorder_node(self, node):
         if node != self.cache.head:

                # Delete node and add it back in front
                self.cache.remove_node(node) 
                self.cache.add(node)

    def get(self, key):

        # If the key is in storage, update the cache's order and return the value
        if key in self.storage.keys():

            # Get the node from the dictionary
            accessed_cache = self.storage[key] 

            # Reorders the cache if it's not in front
            self.reorder_node(accessed_cache)

            #print(accessed_cache.value)
            return accessed_cache.value

        else:
            return -1


    def set(self, key, value):

        # Create Node object from inputs and saves key and value 
        cache_node = Node(key, value)
        
        # If the key is not in storage, add it to the cache and the storage
        if key not in self.storage.keys():
            
            self.cache.add(cache_node)
            self.storage[key] = cache_node

            # Remove the last item from cache and storage if capacity has been exceeded
            if self.cache.get_size() > self.capacity:
                last_in_cache = self.cache.remove_last() 
                self.storage.pop(last_in_cache.key)

        # If the key already exists, update it
        else:
            updated_node = self.storage[key]

            # Remove from storage and cache
            self.cache.remove_node(updated_node)
            self.storage.pop(key)

            # Add it back
            self.cache.add(cache_node)
            self.storage[key] = cache_node

# Testing purposes. Prints order of cache, the head and tail, and dictionary
def debug_cache(lru_cache):

    cache_order = []
    temp = lru_cache.cache.head

    while temp:
        cache_order.append(temp.value)
        temp = temp.next

    print("Order of list", cache_order)
    print("Head:", lru_cache.cache.head.value, "| Tail:", lru_cache.cache.tail.value)
    print(lru_cache.storage, "Cache size:", lru_cache.cache.get_size())


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # Returns 1

our_cache.get(2)       # Returns 2
our_cache.get(9)       # Returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6) 

our_cache.get(3)      # Returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#debug_cache(our_cache) 

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(2, 22)

# Test Case 2
our_cache.set(345123456789012345678901234567890, 123456789123456789123456789.6)

# Test Case 3
our_cache.set(None, [])
our_cache.get(None) # Returns []

our_cache.get(345123456789012345678901234567890) # Returns 123456789123456789123456789.6

#debug_cache(our_cache)