# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
idx = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Reverse the digits of an integer removing trailing 0s from the front, keeping the sign
def reverse(x):
    reversed_num = ''
    sign = 1
    if int(x) < 0:
        sign = -1
    for s in reversed(x):
        if s != '-' and int(s) > 0:
            reversed_num += s
    return sign * int(reversed_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = (input("enter a number to reverse"))
    print(reverse(test))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
