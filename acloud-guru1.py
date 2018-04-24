





def naughty_product(numbers):
    p = 1
    while numbers:
        p *= numbers.pop()
    return p



num = [1,2,3,4]

res = naughty_product(num)
print(res)


