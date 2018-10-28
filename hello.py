def hello(who):
    print('Hello ' + who)

hello('Alexey')

def out_int(min, max):
    x = 0
    arr = []
    for x in range(min, max):
        if x % 2 == False:
            x = str(x)
            arr.append(x)
    return arr

even_arr = out_int(0, 100)
mystr = 'Even numbers: '
print(mystr + ', '.join(even_arr))

print ('Enter your name: ')
x = input()
print ('Hello ' + x)
