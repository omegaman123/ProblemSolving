def stepCount(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return stepCount(n-1) + stepCount(n-2)


if __name__ == '__main__':
    while True:
        test = (input("enter a number of steps to check"))
        print(f'{stepCount(int(test))} possible ways to climb {test} steps')
