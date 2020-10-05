def mergeList(nums1, m, nums2, n):
    index_num1 = 0
    index_num2 = 0
    while index_num2 < n:
        while index_num1 < m + index_num2 and nums1[index_num1] < nums2[index_num2]:
            index_num1 += 1
        nums1.insert(index_num1, nums2[index_num2])
        index_num2 += 1

    while m + n != len(nums1):
        nums1.pop()


if __name__ == '__main__':
    test1 = [1, 2, 3, 0, 0, 0]
    test2 = [2, 5, 6]
    mergeList(test1, 3, test2, 3)
    print(test1)

