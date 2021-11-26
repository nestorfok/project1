class bstree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def size(self):
        sum = 1 if self.tree() else 0

        if self.left is not None:
            sum += self.left.size()

        if self.right is not None:
            sum += self.right.size()

        return sum

    def tree(self):
        return self.value is not None

    def insert(self, value):
        if self.tree():
            if self.value > value:
                if self.left is None:
                    self.left = bstree()
                self.left.insert(value)
            else:
                if self.right is None:
                    self.right = bstree()
                self.right.insert(value)
        else:
            self.value = value

    def find(self, val):
        if self.value is None:
            return False
        elif self.value == val:
            return True
        elif self.value > val and self.left is not None:
            return self.left.find(val)
        elif self.right is not None:
            return self.right.find(val)
        else:
            return False

    def print_set_recursive(self, depth):
        if self.tree():
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            if self.left is not None:
                self.left.print_set_recursive(depth + 1)
            if self.right is not None:
                self.right.print_set_recursive(depth + 1)

    # You can update this if you want
    def print_set(self):
        print("Tree:")
        self.print_set_recursive(0)

    def print_stats(self):
        # TODO update code to record and print statistic
        print("Placeholder - remove this print statement")


tree = bstree()

lis = [5, 3, 7, 2, 9, 4, 8]

for num in lis:
    tree.insert(num)

tree.print_set()

for num in lis:
    print(tree.find(num))

print(tree.find(-10))
