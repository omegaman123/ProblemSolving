def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)


if __name__ == '__main__':
    test = (input("enter a haystack"))
    test2 = input('enter a needle')
    print(strStr(test, test2))
