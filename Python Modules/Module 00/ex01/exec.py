import sys

# n = len(sys.argv)
# print ("Total arguments passed ", n);

list = sys.argv[1:]

if len(list) != 0:
    i = len(list) - 1
    new_list = []
    while i >= 0:
        new_list.append(list[i][::-1].swapcase())
        i -= 1
    joined_string = ' '.join(new_list)
    print(joined_string)
