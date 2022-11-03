class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

new_user = "Joe"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Checks to see if input is incorrect 
def is_valid(user, group):

    if user == None or group == None:

        print("Incorrenct group or user")
        return False

    if type(user) == int or type(group) == int:

        print("Incorrenct group or user")
        return False

    if user == "" or group == "":

        print("Incorrenct group or user")
        return False

# Return True if user is in the group, False otherwise
def is_user_in_group(user, group):

    if is_valid(user, group) == False:
        return False

    # Loops through users in group
    for u in group.get_users():
        if user == u:
            print(user, "in", group.name)
            return True

    print(user, "not in", group.name)
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Sub child user should be in group
is_user_in_group(sub_child_user, sub_child)

# Test Case 2
# Sub child user should not be in group
is_user_in_group(sub_child_user, child)

# Test Case 3
# New user should not be in parent group
is_user_in_group(new_user, parent)

# From test case 4 to 6, it would produce an incorrect message becase it is either null or not a string

# Test Case 4
is_user_in_group(sub_child_user, None)

# Test Case 5
is_user_in_group(1, parent)

# Test Case 6
is_user_in_group(new_user, "")