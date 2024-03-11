# Q1bi
# def Func(x):
#     total = 0
#     for i in range(x):
#         total += i * (i - 1)
#     return total
#
# x = Func(5)
# print(x)

# Q1bii
# x = 'acegikm'
# y = 'bdfhjln'
# z = ' '
# for i in range(len(x)):
#     z = z +x[i] + y[i]
# print(z)

# Q1c
# counter = 0
# while counter < 100:
#     if counter % 2 == 0:
#         counter += 1
#     else:
#         counter *= 2
# print(counter)

# Q2ai
# sentence = "that car was really fast"
# for character in sentence:
#     if character == "t":
#         print("found a 't' in sentence")
#     else:
#         print("maybe the next character?")

# Q2aii
# L = [1, 2, 3, 4]
# L = [str(i) for i in L]
# x = ''.join(L)
# print(x)
# print(type(x))

# Q2bi
# Convert input into integer.
# min = int(input("Enter a lower range: "))
# max = int(input("Enter a upper range: "))
#
# # To concatenate string, use + instead of ,
# print("Prime number(s) between " + str(min) + " and " + str(max) + " is/are: ", end='')
#
# # To include max, +1
for num in range(min, max+1):
    if num > 1:
        check = True
        for i in range(2, num):
            if num % i == 0:
                check = False
                break
        if check:
            print(num, end='')

# Q2bii
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        value = n * factorial(n-1)
    return value

print(factorial(4))


