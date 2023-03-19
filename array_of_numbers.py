"""this function prints a two d array of numbers the increment is 0.1"""

def print_array_of_numbers(number_of_lines):
    for i in range(1,number_of_lines+1):
        for j in range(1,10):
            print(str(0+i-1)+'.'+str(j),end=" ")
        print(i)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    NUMBER_OF_LINES = 9
    print_array_of_numbers(NUMBER_OF_LINES)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
