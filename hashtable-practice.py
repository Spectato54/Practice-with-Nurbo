from collections import Counter, defaultdict

# 1. Word Counting
def wordCounting(arr):
    return Counter(arr)

# 2. Character Frequency
def charFreq(s):
    return Counter(s)

# 3. Remove Duplicates from List
# Do I return original array?
def rmDup(arr):
    return set(arr)

# Returning original arr
def rmDupOrig(arr):
    seen = set()
    write = 0
    for n in arr:
        if n not in seen:
            seen.add(n)
            arr[write] = n
            write += 1
    
    while len(arr) > write:
        arr.pop()

    return arr
    
# 4. Character Position Mapping
def charPosMap(s):
    pos = defaultdict(list)
    for i in range(len(s)):
        pos[s[i]].append(i)
    return pos
print(charPosMap("hello"))

# 5. Find Duplicates
def findDup(arr):
    seen = set()
    dup = set()
    for n in arr:
        if n in seen:
            dup.add(n)
        else:
            seen.add(n)
    return dup
print(findDup([1, 2, 3, 2, 4, 5, 5]))        

# 6. Character Mapping Between Strings
