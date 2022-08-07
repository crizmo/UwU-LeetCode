
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    
    for i in range(len(s)):
        # here we check if the number is in bounds of the length of the input and 
        # if it has 2 numbers then if the first number smaller than the second number then we substract it from the 2nd number
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else :
            res += roman[s[i]]
            
    print(res)
    return res
        
romanToInt("IV")