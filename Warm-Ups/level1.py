""" Hackathon - Level 1 """

def min_max_product(list):
    
    max = 0
    for n in list:
        if n > max:
            max = n
            
    min = 10000
    for n in list:
        if n < min:
            min = n
    
    return max * min

if __name__ == '__main__':
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))
