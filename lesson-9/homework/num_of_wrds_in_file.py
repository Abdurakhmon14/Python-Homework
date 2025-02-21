1. Count number of words in a file
with open('test.txt', 'r') as file:
    data = file.read().split()
    print(f'The number of words: {len(data)}')
    print(data)

2.find an replace file
 with open('test.txt', 'w+') as file:
    for i in file:
        print(i.replace('Hello', 'Bye'))
with open('test.txt', 'r+') as file:
    data = file.read().replace('Hello', 'Bye')
with open('test.txt', 'w') as file:
    file.write(data)

try:
    3/0
except ZeroDivisionError as z:
    print('You got zero division error')
finally:
    print('Execution completed')    
