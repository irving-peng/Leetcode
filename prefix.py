
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # numRows/3 pair 

    # first 4 + 2 (4-2) = 6 as a pair and index 0,1,2,3,2,1 , 0 
    # first col numRows item(0,1,2,3) _> numRows ==4 (numRows - 1: main col) index: 0,1,2,3 
    # second col (2) index: 2
    # third col (1) index : 1

    # forth col (0,1,2,3) index: 0,1,2,3
    # fifth col(2)
    # six col (3)

    # 1. first calculate pair length = numOfRow + (numOfRow -2) if numOfRow >  1 
    # index: 0 - numOfRow / 2 - 1 and  numOfRow  - len(numOfRow + (numOfRow -2)) - 1
    # use a list with index from 0 to len(numOfRow + (numOfRow -2)) - 1 to store the row num of each item
    # return from row 0 to row numOfRow - 1

    pair_len = 2* numRows -2
    mid = pair_len / 2
    result = {}
    if numRows > 1:
        for i in range(numRows):
            result[i] = []


    for i in range(len(s)):
        # front half # 0, 1,2,3
        if i % pair_len <= mid:
            row_index = i % pair_len
            result[row_index].append(s[i]) # add to result
        # back half, 2, 1
        else: # i % pair > mid
            row_index = mid - (i % pair_len- mid) # 1 step after mid would be mid - 1
            result[row_index].append(s[i])
    convert = ""
    for key in result:
        for l in result[key]:
            convert += l
    return convert
    

s = "PAYPALISHIRING"
numRows = 4
pair_len = 2* numRows -2
mid = pair_len / 2
result = {}
if numRows > 1:
    for i in range(numRows):
        result[i] = []


for i in range(len(s)):
    # front half # 0, 1,2,3
    if i % pair_len <= mid:
        row_index = i % pair_len
        result[row_index].append(s[i]) # add to result
    # back half, 2, 1
    else: # i % pair > mid
        row_index = mid - (i % pair_len- mid) # 1 step after mid would be mid - 1
        result[row_index].append(s[i])



print(convert("PAYPALISHIRING", 4))