"""
Stack Implementation following

Hands-on
Data Structure and Algorithms with Python (2nd Edition) by Dr. Basant Agarwal and Benjamin Baka

"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Push (add) a new Node onto the top of the stack
        If stack is empty:
            - new node to be added is the first Node. self.top will point to that and next will be None
            
        Else:
            - New node next will point to the previous top node
            - New node will now be top
        """

        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size = self.size + 1

    def pop(self):
        """
        Pop (remove) the first Node off the top of the stack and reduce our size.
        If stack is empty:
            - Delete should not do anything (cannot delete data from empty stack)
        elif stack has a top data:
            - delete the data by pointing self.top to current self.top.next
        else (stack length is 1):
            - delete stack and change self.top to None 
        :return - data
        """
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        """
        This will check the value at the top of the stack
        :return: data
        """
        if self.top:
            return self.top.data
        return None


"""
Life application example (Bracket-matching application)

Objective:
    - Verify that whether a statment containing brackets (, [ or { is balanced 
        - closing brackets matches opening bracket 
    - also ensures one pair of brackets really is contained in another 
"""


def bracketsMatch(statement):
    stack = Stack()
    for ch in statement:
        last = None
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
        if last is '{' and ch is '}':
            continue
        elif last is '[' and ch is ']':
            continue
        elif last is '(' and ch is ')':
            continue
        elif ch in ('}', ']', ')') and last is None:  # at this point if we have any of the closing brackets and last is None, we know they dont have opening correspondent
            return False
    if stack.size > 0:
        return False
    else:
        return True


sl = (
    "{ (foo) (bar) } [hello] (((this)is)a)test",
    "{ (foo) (bar) } [hello] (((this)is)atest",
    "{ (foo) (bar) } [hello] (((this)is)a)test))"
)

for l in sl:
    print ("{}: {}".format(l, bracketsMatch(l)))


# Test cases
# Start setting up a Stack
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(5)

print("sneeck peek is : {}".format(stack.peek()))
print(stack.pop())
print (stack.pop())
print (stack.pop())
print (stack.pop())
print (stack.pop())
print("sneeck peek is : {}".format(stack.peek()))