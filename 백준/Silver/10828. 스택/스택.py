import sys

T = int(sys.stdin.readline())
stack = []

def push(arg):
    stack.append(arg)

def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)
    
def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])

for _ in range(T):
    func = sys.stdin.readline().split()
    if func[0] == "top":
        top()
    
    elif func[0] == "size":
        size()
    
    elif func[0] == "empty":
        empty()

    elif func[0] == "pop":
        pop()

    elif func[0] == "top":
        top()

    elif func[0] == "push":
        push(func[1])

