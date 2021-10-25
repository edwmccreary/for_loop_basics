# Basic 
for i in range(151):
    print(i)

# Multiples of Five
for i in range(5,1001):
    if i % 5 == 0:
        print(i)

# Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print(str(i) + " Coding Dojo")
    elif i % 5 == 0:
        print(str(i) + " Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge
sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum += i
print(sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Flexible Counter
def flex_counter(low,high,mult):
    for i in range(low,high+1):
        if i % mult == 0:
            print(i)

flex_counter(5,100,5)