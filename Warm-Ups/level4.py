""" Hackathon - Level 4 """

def double_swap(string, a, b):

    output = []
    for i in range(0,len(string)):
        if string[i] == a:
            output.append(b)
            continue
        if string[i] == b:
            output.append(a)
            continue
        output.append(string[i])
    return "".join(output)

if __name__ == '__main__':
    print(double_swap('veni, vidi, vici', 'v', 'i'))
