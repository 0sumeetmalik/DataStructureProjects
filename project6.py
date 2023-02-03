"""
1. Union Function
a. Created Deep copy of list1 and list2
b. Created a set named value_check which stores all values we are appending in union linked list
c. Using value_check to ensure no duplicate values are added in unon linkedlist
d. Traversing both list to find final union
e. Issue with Code I see is : repetition of code in Union. I was thinking of recursive solution, but didn't want to make it complex
Time complexity is O(n * m)

2. Intersection Function
a. Similar structure like Union
b. Just added values by single Traverse in one list
Time complexity O(n * m) where n i set fo values in one and m is number of value in other set

Overall i feel Linkedlist are not great data structure for finding union and intersection. Array are more efficient
"""


import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def first_value_move_head(linked_list):
    first_value = linked_list.head
    linked_list.head = linked_list.head.next

    return first_value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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


def union(llist_1, llist_2):
    # Your Solution Here
    value_check = set()
    union_llist = LinkedList()
    llist_1_copy = copy.deepcopy(llist_1)
    llist_2_copy = copy.deepcopy(llist_2)

    if union_llist.head is None:
        first_node = first_value_move_head(llist_1_copy)
        union_llist.head = Node(first_node.value)
        union_llist.tail = union_llist.head
        value_check.add(first_node.value)

    while llist_1_copy.head is not None:
        next_node = first_value_move_head(llist_1_copy)

        if not next_node.value in value_check:
            union_llist.tail.next = Node(next_node.value)
            union_llist.tail = union_llist.tail.next
            value_check.add(next_node.value)

    while llist_2_copy.head is not None:
        next_node = first_value_move_head(llist_2_copy)
        if not next_node.value in value_check:
            union_llist.tail.next = Node(next_node.value)
            union_llist.tail = union_llist.tail.next
            value_check.add(next_node.value)

    return union_llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    intersect_llist = LinkedList()
    llist_1_copy = copy.deepcopy(llist_1)
    llist_2_copy = copy.deepcopy(llist_2)
    value_check = set()

    while llist_1_copy.head is not None:
        f_node = first_value_move_head(llist_1_copy)
        list2_node = llist_2_copy.head
        while list2_node is not None:
            if f_node.value == list2_node.value:
                # Create Intersection LinkedList
                if intersect_llist.head is None:
                    intersect_llist.head = Node(f_node.value)
                    intersect_llist.tail = intersect_llist.head
                    value_check.add(f_node.value)
                    break

                if not f_node.value in value_check:
                    intersect_llist.tail.next = Node(f_node.value)
                    intersect_llist.tail = intersect_llist.tail.next
                    value_check.add(f_node.value)

            list2_node = list2_node.next

    return intersect_llist


if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))
