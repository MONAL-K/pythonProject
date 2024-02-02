# This function uses global variable s
def f():
    global s
    s =s+ 'GFG'
    print("Inside Function", s)


# Global scope
s = "I love Geeksforgeeks"
f()