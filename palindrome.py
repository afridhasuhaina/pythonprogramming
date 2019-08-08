def reverse(s):
    return s[::-1]
def ispalindrome(s):
    rev=reverse(s)
    
    if s==rev:
       return True
    return False
    
s=int(input())
ans=ispalindrome(s)

if ans==1:
    print("yes")
else:
    print("no")
