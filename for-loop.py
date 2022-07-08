# for letter in "Aregak Tours":
    # print(letter)


friends = ['Jim', 'Kevin', 'Karen']

# for letter in friends:
#     print(letter)

# for index in range(len(friends)):
#     print(index)

# for index in range(5):
#     if index == 0:
#         print(index)
#     else:
#         print('Hi bro')     


def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result
print(raise_to_power(2,3))  