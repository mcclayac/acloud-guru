
vegtablesList = ['Carrots','Tomatoes','Squash','Onions', 'Peas','Brocolli']
FruitSet = {'Apples', 'Oranges','Stawberry','Grapes','Pineapple'}

for (fruit, vegtable) in zip(vegtablesList, FruitSet):
    print("veggie {0} and {1} fruit".format(vegtable, fruit))



idx = 0
hatstack = ['hay'] * 30
hatstack[13]= 'Needle'

print(hatstack)

for (i, v) in enumerate(hatstack):
    print("Looking ..")
    if v == 'Needle' :
        print("found it at index {0}".format(i))
        idex = i
        break


total = 0
while True:
    num = input('Enter a number ?')
    if not num: break
    total += int(num)
    print("Number is {0},  total = {1}".format(num, total))

print('End total = {0}'.format(total))



