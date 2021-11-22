class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        return self.stack.pop()

number_list = Stack()
with open('input.txt') as f1:
    with open('output.txt', 'w') as f2:
        M = int(f1.readline())
        for i in range(M):
            command = f1.readline()
            if command[0] == "+":
                number_list.push(int(command[2:]))
            else:
                f2.write(str(number_list.pop()) + '\n')

                