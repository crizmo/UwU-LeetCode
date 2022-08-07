
def intToRoman(num):
    # """
    # :type num: int
    # :rtype: str
    # """
        
    
    integer = [["I", 1], ["II", 2], ["III", 3], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
    
    res = ""
    for sym, val in reversed(integer):
        if num // val:
            count = num // val
            res += (sym * count)
            num = num % val

    return res
        
intToRoman(8)