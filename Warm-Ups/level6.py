""" Hackathon - Level 6 """

def cipher(string, x):
    output = ""
    for c in string:
        o = ord(c) + x
        output += chr(o) if o <= 122 else chr(o - 26)
    return output

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return salve
    print(cipher('pxisb', 3))
