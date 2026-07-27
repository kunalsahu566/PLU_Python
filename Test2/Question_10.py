queue = []

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Original Queue:")
for i in queue:
    print(i)

removed = queue.pop(0)

print("\nRemoved Element:", removed)

print("\nUpdated Queue:")
for i in queue:
    print(i)