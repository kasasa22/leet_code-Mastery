def is_palindrome(x: int)->bool:
    if x < 0 or (x%10==0  and x!=0):
        return False
    
    r_half = 0

    while x > r_half:
        r_half = r_half*10 + x%10
        x//=10

    return x==r_half or x==r_half //10

print (is_palindrome(121))
print (is_palindrome(-121))
print (is_palindrome(10))
print (is_palindrome(212))
