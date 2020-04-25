class Stack:
    _stack = []

    def get_stack(self):
        return self._stack

    def is_empty(self):
        return True if len(self._stack) == 0 else False

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def size(self):
        return len(self._stack)


if __name__ == '__main__':
    open_brc = tuple('([{')
    close_brc = tuple(')]}')
    mapping = dict(zip(open_brc, close_brc))

    def check_for_balanced(expression: str):
        if len(expression) % 2 == 1:
            return False

        stack = Stack()
        for character in expression:
            if character in open_brc:
                stack.push(mapping[character])
            elif stack.is_empty() or character != stack.pop():
                return False

        return not stack.get_stack()

    test1 = '(((([{}]))))'
    test2 = '}{}'
    test3 = '{{[(])]}}'
    test4 = '[[{())}]'
    test5 = '[([])((([[[]]])))]{()}'

    print(check_for_balanced(test5))
