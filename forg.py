test_cases = int(input())
for test_case in range(test_cases):
    value_str = str(input())
    value = int(value_str)
    if "4" not in value_str:
        print ("Case #%d: %d %d" % (test_case + 1, value, 0))
        continue

    mid = int(value / 2)
    if mid % 2 == 0:
        mid = mid + 1
    #print(mid)
    if value == 4:
        result1 = 2
        result2 = 2
    else:
        for i in range(mid, value - 1, 2):
            result1 = i
            result2 = value - result1
            if "4" not in str(result1) and "4" not in str(result2):
                break
    print ("Case #%d: %d %d" % (test_case + 1, result1, result2))
