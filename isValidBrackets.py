# Check if a string expression of paranthesis, brackets, etc is valid. '([]) is valid, ((]) is not
def isValid(s):
    s_list = list(s)
    brack_map = {'(': ')', '{': '}', '[': ']'}
    para_map = ['(', '{', '[']
    stack = []
    for c in s_list:
        if c in para_map:
            stack.append(c)
        elif stack and c == brack_map[stack[-1]]:
            stack.pop()
    return stack == []


if __name__ == '__main__':
    test = input("Enter a String to Test:")
    print(isValid(test))
