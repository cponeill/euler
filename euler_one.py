# This is my answer to question number one. Pretty simple enough.

def euler_one(s):
    return sum(n for n in range(s) if n%3 == 0 or n%5 == 0)

# This will print out the answer you need for the very first question which is 233168.
print euler(1000)
