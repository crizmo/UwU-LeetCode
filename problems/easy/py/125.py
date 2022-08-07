# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
s = "a."

def pali():
    new = " ".join(s.split()).replace(" ", "")
    new = ''.join(ch for ch in new if ch.isalnum())
    stuff = new.lower()

    return True if stuff[::-1] == stuff else False

pali()