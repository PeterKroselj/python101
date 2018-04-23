
x = int(raw_input("Enter value for x: "))
y = int(raw_input("Enter value for y: "))

operation = raw_input('Choose math operation: +, -, /, *: ')

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '/':
    result = x / y
elif operation == '*':
    result = x * y
else:
    result = 'Invalid information'

print result
