import sys

# n = len(sys.argv)
# print ("Total arguments passed ", n);

list = sys.argv[1:]

if len(list) != 0:
    # print("list without the executable : ", list)
    i = 0
    while i < len(list):
        list[i] = list[i][::-1]
        i += 1
    joined_string = ' '.join(list)
    print(joined_string)
    # print("Reversed and joined string ", joined_string)
