"""
Created a recursive function which check each folder whether it is group
if yes, it goes further in, also checks if user exit in each stage
As soon as user is found, it returns True value

"""


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


def is_user_in_group(user, sub_groups):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or sub_groups is None or user == '':
        return -1

    # print(sub_groups.get_users(), user)
    for index, sub_user in enumerate(sub_groups.get_users()):
        if sub_user == user:
            return True

    for sub_groups in sub_groups.get_groups():
        if is_user_in_group(user, sub_groups):  # Using recursion to check User in a sub user groups
            return True
    return False


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # test Case 1 , Finding a User
    print(is_user_in_group('sub_child_user', parent))

    # Test Case 2, Empty value, return -1
    print(is_user_in_group('sub_child_user', None))
    print(is_user_in_group('', parent))

    # test Case 3, very large user name input value, multiple values in users
    sub_child_user2 = "sub_child_user_veryyyyyyyyyyyyyyyyyyyyyy_largeeeeeeeeeee_valueeeeeeeeeeee"
    sub_child.add_user(sub_child_user2)
    print(is_user_in_group('sub_child_user_veryyyyyyyyyyyyyyyyyyyyyy_largeeeeeeeeeee_valueeeeeeeeeeee', parent))
