file1 = open("MyFile.txt", "a")

try:
    file2 = open("no_file.txt", "a")
except FileNotFoundError:
    print("file does not exist, please enter valid filename/path")
else:
    print("file 1 opens")

file1.write('str1 \n')

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)

with open("MyFile.txt") as f:
    for line in f:
        print(line)
        if 'str1' in line:
            break

def readfile(filepath):
    file1 = open(filepath)
    for line_ in file1:
        print(line_, end='')
    file1.close()


def write_func(var):
    var = str(var)
    file1.write(var)




string1 = 'badger \n'
write_func(string1)


# file1 = open("MyFile.txt", "r")
#
# lines = file1.readlines()

# for line in lines:
#     var1 = 'badger'
#     var2 = line.split(",")
#     my_file = open('new_file.txt', 'w')
#     my_file.writelines(var1)
#     my_file.close()
# file1.close()


file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is :")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

file1.readlines()

# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()
