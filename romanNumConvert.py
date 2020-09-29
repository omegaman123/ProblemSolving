
def convertRomanNum(s):
    val_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub_map = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
    s_list = list(s)
    total = 0
    i = 0
    while i < len(s_list):
        if s_list[i] in sub_map:
            if i+1 < (len(s_list)) and s_list[i+1] in sub_map[s_list[i]]:
                total = total + val_map[s_list[i+1]] - val_map[s_list[i]]
                i += 2
            else:
                total = total + val_map[s_list[i]]
                i += 1
        else:
            total = total + val_map[s_list[i]]
            i += 1

    return total


if __name__ == '__main__':
    test = (input("enter a roman numeral to convert"))
    print(convertRomanNum(test))
