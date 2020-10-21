""" Hackathon - Level 3 """

def oddish_evenish(x):
    num = str(x)
    total = 0
    for char in num:
        total += int(char)
    print(total)
    
    if total % 2 == 0:
        return "Evenish"
    return "Oddish"


if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return Oddish
    print(oddish_evenish(1190))
