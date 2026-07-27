stack = []

stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

print("Stack Elements:")
for i in stack:
    print(i)

if len(stack) == 0:
    print("\nStack is Empty")
else:
    print("\nStack is Not Empty")