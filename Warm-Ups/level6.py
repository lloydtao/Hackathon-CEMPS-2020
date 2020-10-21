""" Hackathon - Level 6 """

def cipher(string, x):
    """Applies the Caeser Sipher to the given string, shifting by x"""
    # Input validation:
    # Check that inputs are the correct types. If not, try and convert them
    try:
        string = str(string)
        x = int(x)
    except:
        print("Invalid types given as inputs")
        return
    if x < 0:
        print("Please use a positive number for the shift")
        return
    
    # Logic:
    # Make sure that our shift is below 26 so that our wrapping works
    x = x%26
    output = ""
    for c in string:
        # Convert the character into it's ASCII code and shift by x
        o = ord(c) + x
        # If o is greater than the ASCII code for z then wrap back to 'a'
        output += chr(o) if o <= 122 else chr(o - 26)
    return output

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return salve
    print(cipher('pxisb', 3))
