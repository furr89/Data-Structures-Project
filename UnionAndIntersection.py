class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Turns a linked list into a set for quick access
def get_access(llist):

    access = {}

    current = llist.head
    while current:

        if current.value not in access.keys():
            access[current.value] = 1

        else:
            access[current.value] += 1

        current = current.next

    return access

# Handles duplicate values in the list
def substract_intersect(dict, value):

    dict[value] -= 1

    if dict[value] <= 0:
        dict.pop(value)

# Combines the lists
def union(llist_1, llist_2):

    new_list = LinkedList()

    cur_l1 = llist_1.head
    while cur_l1:
        new_list.append(cur_l1)
        cur_l1 = cur_l1.next

    cur_l2 = llist_2.head
    while cur_l2:
        new_list.append(cur_l2)
        cur_l2 = cur_l2.next

    return new_list

# Gets the nodes that are in both lists
def intersection(llist_1, llist_2):

    new_list = LinkedList()
    intersect = get_access(llist_1)
    #print(intersect)
    
    # If there is elements in both lists, add it in new one
    cur_l2 = llist_2.head
    while cur_l2:
        if cur_l2.value in intersect:
            new_list.append(cur_l2)
            substract_intersect(intersect, cur_l2.value)
        cur_l2 = cur_l2.next

    #print(intersect)
    return new_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Union adds 3 more nodes, intersect would only get 3 of the nodes
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [5,5,5,5,5,5,5,5,5,5]
element_2 = [5,5,5]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 2
# Unions should add them both, intersect should be none
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = ['0', '1', '2', '3', '4', '5']
element_2 = [1,2,3]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))

# Test Case 3
# Both union and intersect should be none
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))