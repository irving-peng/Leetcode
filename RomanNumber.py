s = "III"
# output 3

s2 = "MCMXCIV" # 4 + 90 + 
#output 58, 
s3 = 'MCDLXXVI' # 6 + 20 + 50 L -C 100 + D 500, + M 1000

# start from last before end call j
# if j < j+ 1: is pair, plus j+1, minus j
# j move left 1 index
# else: not pair, add right
# (only minus if smaller than right !)
#output 1476


# start in the list, iterate , till current letter < =remain
# ==num : + cur_letter
#end
# if biggest_dec = num % 10 
# if 4 or 9:
#  + letters[cur + 1] + curLetter 
# remaider - thissum
#
# 1-3 letter: 
# + big_decimal * cur_letter
# remainder - thissum * big_decimal

# keep find letter
import math
def IntToRoman(num):
    """
    :type s: str
    :rtype: int
    """
    result = ""
    remain = num
    letters = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    convert = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1,     
    }
    i = 0 
    while ( i < len(letters)):
        # cuurent letter too big to fit in
        if remain <= 0 :
            break
        print("result: ", result)
        print("current", letters[i])
        print(remain, letters[i],convert[letters[i]])
        if not i+2 > len(letters)-1:
            temp = convert[letters[i+1]]
        elif not i+1 > len(letters)-1:
            temp = convert[letters[i+1]]
        else:
            temp =0 
        if remain < convert[letters[i]] - 1 * temp:
            print("next letter: ", str(convert[letters[i]] - 1 * temp))
            i += 1
            continue
        
        # equal
        if remain == convert[letters[i]]:
            result += letters[i]
            remain -= convert[letters[i]]
        # 4 or 9
        power = math.floor(math.log10(remain))
        big_decimal = int(str(remain)[0])
        print("first letter", str(remain)[0])
        if big_decimal == 4 or big_decimal == 9:
            if big_decimal ==4:
                result += letters[i+1]
                result += letters[i]
                remain -= (big_decimal) * convert[letters[i+1]]
            else:
                result += letters[i+2]
                result += letters[i]
                remain -= (big_decimal) * convert[letters[i+2]]
                print("minus", str(convert[letters[i+2]]))
                
                continue
        else:
            # <= 3 times
            if big_decimal <= 3:
                result += big_decimal * letters[i]
                remain -= convert[letters[i]] * big_decimal
                
            # more than 3 times
            else:
                result += letters[i]
                remain -=  convert[letters[i]]
                
        
        # finish calculating
        
    return result

print(IntToRoman(1994))