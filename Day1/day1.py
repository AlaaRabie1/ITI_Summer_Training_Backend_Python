print("A program that counts up the number of vowels [a, e, i, o, u] contained in the string.")
inp = input("Enter a string: ")
vowels = ['a','e','i','o','u']
count = 0
for i in inp:
    for j in vowels:
        if i == j:
            count = count + 1

print(f"count = {count}")


print("Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.")
array = []
for i in range(0,5):
    elem = input("Write the elemnt: ")
    array.append(elem)

print(array)
array.sort()
print(array)
array.reverse()
print(array)



print("A program that prints the number of times the string 'iti' occurs in anystring.")
str1 = input("Enter a string: ")
iti_count = str1.count("iti")
print(f"iti count = {iti_count}")



print("A program that remove all vowels from the input word and generate a brief version of it.")
word = input("enter any word: ")
print(f"word before = {word}")
vowels = ['a','e','i','o','u']
for i in word:
    for j in vowels:
        if i == j:
            print(f"i = {i} , j = {j}")
            word = word.replace(i,"")

print(f"word after = {word}")




print("A program that prints the locations of a character in any string you added.")
wordd = input("enter any word: ")
char = input("now enter the char you want : ")
print(f"Character = {char}:")
for index, c in enumerate(wordd):
    if c == char:
        print(f"appears at index = {index}")




print("A program that generate a multiplication table from 1 to the number passed.")
mult_num = int(input("enter a number: "))
l2 = []
for i in range(1,mult_num+1):
    l = []
    for j in range(1,i+1):
        multiply = i * j
        l.append(multiply)
    l2.append(l)

print(l2)



print("A program that build a Mario pyramid like below:")
number = int(input("enter a number: "))
for i in range(1,number+1):
    for j in range(0,i):
        print('*' , end = "")
    print("\n")