class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty() == True:
            return None
        return self.stack.pop()

brackets = Stack()
with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        n = int(f.readline())
        for i in range(n):
            scoba = f.readline()
            if i != n-1:
                s = scoba[:len(scoba)-1]
            else:
                s = scoba
            flag = True
            for j in range(len(s)):
                if j == 0 and (s[j] == ')' or s[j] == ']'):
                    f1.write('NO\n')
                    flag = False
                    break
                elif s[j] == '(' or s[j] == '[':
                    brackets.push(s[j])
                else:
                    if brackets.is_empty() == True and j != 0:
                        f1.write('NO\n')
                        flag = False
                        break
                    prev = brackets.pop()
                    if s[j] == ')' and prev == '[' or s[j] == ']' and prev == '(':
                        f1.write('NO\n')
                        flag = False
                        break
            if flag == True:
                f1.write('YES\n')