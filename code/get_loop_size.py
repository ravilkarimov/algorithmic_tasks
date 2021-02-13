class Node:
    def __init__(self, next_node=None, order=None):
        self.next = next_node
        self.order = order

    def __str__(self):
        return "Node: {}".format(self.order)


def loop_size(node):
    d = {}
    o = 1
    d[node] = o
    n = node
    while True:
        if n.next != None:
            if d.get(n.next) == None: 
                n = n.next
                o += 1
                d[n] = o
            else:
                return d.get(n) - d.get(n.next) + 1
        else:
            print("No cycle")
            break


# Make a short chain with a loop of 3
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
# loop_size(node1)
print(loop_size(node1))

'''
Best solution

def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

'''