stack = []

stack.append(1)
stack.append(10)
stack.append(150)
stack.append(200)

print("Original Stack:")
for i in stack:
    print(i)

removed = stack.pop()

print("\nPopped Element:", removed)

print("Updated Stack:")
for i in stack:
    print(i)