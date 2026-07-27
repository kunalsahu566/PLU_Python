'''
4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced.
'''


n = int(input("Enter the number of participants: "))
timings = []

for i in range(n):
    timing = float(input(f"Enter timing of participant {i + 1} (seconds): "))
    timings.append(timing)

# Insertion sort to arrange timings from fastest to slowest
for i in range(1, len(timings)):
    key = timings[i]
    j = i - 1
    while j >= 0 and timings[j] > key:
        timings[j + 1] = timings[j]
        j -= 1
    timings[j + 1] = key

print("Timings from fastest to slowest:", timings)

# Show top 3 winners
print("1st Winner:", timings[0])
if len(timings) > 1:
    print("2nd Winner:", timings[1])
if len(timings) > 2:
    print("3rd Winner:", timings[2])

# Binary search for a timing
search_time = float(input("Enter a timing to search: "))
low = 0
high = len(timings) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if timings[mid] == search_time:
        found = True
        print(f"Timing {search_time} found at position {mid + 1}")
        break
    elif timings[mid] < search_time:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Timing {search_time} not found")


