class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the stack.
        Runtime - O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last (top) item for the stack.
        Runtime - O(1)
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the last item in the stack.
        Runtime - O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the length of the stack
        Runtime - O(1)
        """
        return len(self.items)

    def is_empty(self):
        """ Returns boolean if there are items in the stack or not. """
        if self.items:
            return False
        return True


def match_symbols(symbol_string):
    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    openers = symbol_pairs.keys()
    stack = Stack()

    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]

        if symbol in openers:
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            else:
                top_item = stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1

    if stack.is_empty():
        return True

    return False


print(match_symbols('([{}])'))
print(match_symbols('([){]}'))
