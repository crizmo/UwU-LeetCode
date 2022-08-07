def isPalindrome(x):
    if x > 0:
        temp = x
        rev = []
        while temp > 0:
            print(temp)
            digit = temp % 10
            rev.append(digit)
            temp = temp // 10
        org = rev[::-1]
        print("The number is Palindrome") if org == rev else print("The number is not Palindrome")
        return rev == org
    elif x == 0:
        return True
    else:
        return False

isPalindrome(121)