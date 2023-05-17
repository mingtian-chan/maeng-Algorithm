import sys

T = int(sys.stdin.readline())

deque = []

def push_front(arg):
    deque.insert(0,arg)

def push_back(arg):
    deque.append(arg)

def pop_front():
    if not len(deque):
        return -1    
    return deque.pop(0)

def pop_back():
    if not len(deque):
        return -1
    return deque.pop(-1)
def size():
    return len(deque)

def empty():
    if len(deque):
        return 0
    return 1

def front():
    if not deque:
        return -1
    
    return deque[0]

def back():
    if not deque:
        return -1
    
    return deque[-1]

for _ in range(T):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        push_front(cmd[1])
    if cmd[0] == "push_back":
        push_back(cmd[1])
    if cmd[0] == "pop_front":
        print(pop_front())
    if cmd[0] == "pop_back":
        print(pop_back())
    if cmd[0] == "size":
        print(size())
    if cmd[0] == "empty":
        print(empty())
    if cmd[0] == "front":
        print(front())
    if cmd[0] == "back":
        print(back())
    # print(cmd[0], "deque : " , deque)
