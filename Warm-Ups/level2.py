""" Hackathon - Level 2 """

def longest_word(string):
    words = string.split()
    for i in range(0,len(words)):
        words[i] = words[i].replace(',', '')
    print(words)
    return max(words, key=len)

if __name__ == '__main__':
    print(longest_word("lorem ipsum, dolor sit amet"))
