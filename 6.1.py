import math

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        return False

    def push(self, item):
        if self.is_empty() == False:
            self.stack.append((item, min(item, self.stack[-1][1])))
        else:
            self.stack.append((item, item))

    def pop(self):
        return self.stack.pop()[0]

    def find_min(self):
        if self.is_empty() == True:
            return math.inf
        return self.stack[-1][1]

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()


    def push(self, item):
        self.s1.push(item)

    def pop(self):
        if self.s2.is_empty() == True:
            while self.s1.is_empty() == False:
                self.s2.push(self.s1.pop())
        if self.s2.is_empty() == True:
            return None
        return self.s2.pop()

    def find_min(self):
        return min(self.s1.find_min(), self.s2.find_min())



number_list = Queue()
with open('input.txt') as f1:
    with open('output.txt', 'w') as f2:
        M = int(f1.readline())
        for i in range(M):
            command = f1.readline()
            print(command)
            if command[0] == '+':
                number_list.push(int(command[2:]))
            elif command[0] == '-':
                number_list.pop()
            elif command[0] == '?':
                f2.write(str(number_list.find_min()) + '\n')