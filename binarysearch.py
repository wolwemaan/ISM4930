# Using Python2 as tested on https://ideone.com/ or http://tpcg.io/PpX4vN30 
# Program to demonstrate a binary search implementation

# Binary search function
# Note: Expect a *sorted* array as input
def bsearch(col, num):
    if len(col) == 0:
        return -1
    left = 0
    # max indexes
    right = len(col) - 1
    while left <= right:
        # Slice what we got in half to get a middle point
        mid = left + (right - left) / 2
        
        # If the middle point of the collection is what we are looking for, were done.
        # Otherwise (if it is present at all), it will be either to the left or to right 
        # of the midpoint, meaning subsequent calls will onlydeal with *that section
        # Then we repeat the process of finding a new midpoint and setting new boundaries
        # until the while condition is no longer true
        if col[mid] == num:
            return mid
        elif col[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    # If we reach this point it means that the number isn't present in the collection
    return -1

## Main
col = [int(x) for x in raw_input().split()]

print "Search in collection:"
print(col)

# 
# Input: first line: read collection of numbers
# Following lines: a number to search for
# Example:
#-1 0 3 5 9 12
#3
#-1
#12
#2
#9
#0
#5
while True:
    try:
        # Read number to search for
        num = int(raw_input()) 
        print "Search for number", num
        
        # Do search and print result
        result = bsearch(col, num)
        if result == -1:
            print "Not found"
        else:
            print "Found at index", result
        print ""
    except:
         break    
