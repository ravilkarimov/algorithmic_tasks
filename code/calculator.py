class Operation:
    def __init__(self, left_node, string, right_node):
        self.type = string
        self.left_node = left_node
        self.right_node = right_node

    def evaluate(self):
        if self.type == '+':
            return self.left_node + self.right_node
        elif self.type == '-':
            return self.left_node - self.right_node
        elif self.type == '/':
            return self.left_node / self.right_node
        elif self.type == '*':
            return self.left_node * self.right_node


# class Calculator(object):
#   def evaluate(self, string):
#     return 0




# print(Calculator().evaluate("2 / 2 + 3 * 4 - 6")) # => 7


