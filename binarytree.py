import string
import random
import time


class bstree:
    def __init__(self):
        self.hi = None

    def size(self):
        if (self.tree()):
            return 1 + self.left.size() + self.right.size()
        return 0

    def tree(self):
        # This counts as a tree if it has a field self.value
        # it should also have sub-trees self.left and self.right
        return hasattr(self, 'value')

    def insert(self, value):
        if self.tree():
            print("true")
            # TODO if tree is not NULL then insert into the correct sub-tree
            if self.value == value:
                return False
            elif self.value < value:
                self.right = bstree()
                self.right.insert(value)
            else:
                self.left = bstree()
                self.left.insert(value)
        else:
            print("false")
            # TODO otherwise create a new node containing the value
            self.value = value
            print("_______________")
            # print("value: " + self.value)

    def find(self, val):
        if self.value == val:
            return True
        elif self.value < val:
            if self.right == None:
                return False
            return self.right.find(val)
        else:
            if self.left == None:
                return False
            return self.left.find(val)

    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            if hasattr(self, "left"):
                self.left.print_set_recursive(depth + 1)
            if hasattr(self, "right"):
                self.right.print_set_recursive(depth + 1)

    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)

    def print_stats(self):
        # TODO update code to record and print statistic
        print("Placeholder - remove this print statement")


hi = bstree()
lis = ["k", "b", "c", "d", "e", "m", "n", "f", "z"]
for i in range(len(lis)):
    hi.insert(lis[i])
hi.print_set()
