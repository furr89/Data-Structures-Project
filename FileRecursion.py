import os

# Simple node and linked list class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None 

    # Adds node to the end of list
    def append(self, value):

        if self.head == None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


# Traverses a folder and returns a list of files
def traverse_files(path, files=LinkedList()):

    # Creates a list of the current path
    content = os.listdir(path)

    # Go through the list, combine the path with starting
    for c in content:
        c = os.path.join(path, c)

        # Add to list if it's a file
        if os.path.isfile(c):
            files.append(c)

        # Otherwise, keep searching the directory
        else:
            files = traverse_files(c, files)

    return files


def find_files(suffix, path):

    file_filter = []

    # If given an incorrect or fake path
    if path == "" or not os.path.exists(path):
        print(file_filter)
        return file_filter

    # Traverse the linked list, if the file matches the suffix, add to the file filter
    head = traverse_files(path).head
    while head:

        if (head.data).endswith(suffix):
            file_filter.append(head.data)

        head = head.next

    print(file_filter)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
find_files(".c", "./testdir") # Should return paths with .c files

# Test Case 2
find_files(".h", "./testdir") # Should return paths with .h files

# Test Case 3
find_files("", "./testdir") # Should return all files in the given directory

# Test Case 4
find_files(".html", "./testdir") # Should return empty list

# Test Case 5
find_files(".c", "./fakedir") # Should return empty list

# Test Case 6
find_files(".c", "") # Should return empty list
