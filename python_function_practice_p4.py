# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(one,two,three):
    if one > two and one > three:
        maximum_number = one
        print(maximum_number)
    if two > one and two > three:
        maximum_number = two
        print(maximum_number)
    if three > one and three > two:
        maximum_number = three
        print(maximum_number)

max_num(4,5,6)
    

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return print(result)

mult_list([1,2,3,4,5,6])
        

# Write a Python function called rev_string() to reverse a string.
def rev_string(x):
    text = x[::-1]
    print(text)

rev_string('Hello World')

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num,beg_range,end_range):
    if num >= beg_range and num <= end_range:
        print('True')
    else:
        print('False')

num_within(4,2,7)

num_within(3,5,10)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    row = [1]
    print(row)
    for i in range(n-1):
        row_length = i+2
        new_row = list(range(row_length))
        for j in new_row:
            left = j-1
            right = j
            add_left = 0
            add_right = 0
            if left >= 0:
                add_left = row[left]
            if right < len(row):
                add_right = row[right]
            new_row[j] = add_left + add_right
        
        print(new_row)
        row = new_row
            
pascal(10)
