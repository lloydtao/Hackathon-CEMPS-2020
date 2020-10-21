""" Hackathon - Level 5 """


def convert(numeral):
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i, c in enumerate(numeral):
        if (i + 1) == len(numeral) or roman_numerals[c] >= roman_numerals[
            numeral[i + 1]
        ]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result


if __name__ == "__main__":
    # Add any code to test your solution here
    # As per the example, this should return 1145
    print(convert("MCXLV"))
