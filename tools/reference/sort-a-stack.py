def sortStack(stack):
    sorted_stack = []
    while stack:
        value = stack.pop()
        while sorted_stack and sorted_stack[-1] > value:
            stack.append(sorted_stack.pop())
        sorted_stack.append(value)
    return sorted_stack
