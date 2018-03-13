def is_palindrome(n):
    mystr = str(n)
    if len(mystr) == 1: return True
    elif len(mystr) ==2: return mystr[0] == mystr[-1]
    else: return mystr[0] == mystr[-1] and is_palindrome(mystr[1:-1])

#print(is_palindrome(11011), is_palindrome(110011), is_palindrome(123123), is_palindrome(12312))
mylist = [n1*n2 for n1 in range(900,1000)
          for n2 in range(900,1000) if is_palindrome(n1*n2)]

print(max(mylist))