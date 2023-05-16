import sys

queue = []

def qpush(arg):
    queue.append(arg)

def qpop():
    if not len(queue):
        return -1
    
    ret = queue[0]
    queue.pop(0)
    return ret

def qsize():
    return len(queue)

def qempty():
    if len(queue):
        return 0
    else:
        return 1
    
def qfront():
    if not len(queue):
        return -1
    
    return queue[0]

def qback():
    if not len(queue):
        return -1
    
    return queue[-1]

T = int(sys.stdin.readline())
for _ in range(T):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        qpush(cmd[1])
    if cmd[0] == "pop":
        print(qpop())
    if cmd[0] == "size":
        print(qsize())
    if cmd[0] == "empty":
        print(qempty())
    if cmd[0] == "front":
        print(qfront())
    if cmd[0] == "back":
        print(qback())
