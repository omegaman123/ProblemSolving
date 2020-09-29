# Add one to an integer carrying over if needed
def plusOne(num):
    if int(num[-1]) == 9:
        for i, digit in enumerate(reversed(num)):
            if int(digit) == 9:
                num[0-i-1] = 0
            else:
                num[0-i-1] = int(digit) + 1
                break
        else:
            num.insert(0, int(1))
    else:
        num[-1] = int(num[-1]) + int(1)
    return num


if __name__ == '__main__':
    test = input("Enter a number to add one to:")
    print(f'{list(test)} becomes {plusOne(list(test))}')
