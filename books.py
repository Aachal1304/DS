from collections import Counter
n = int(input("Enter the number of library members: "))
borrow_counts = []

for i in range(n):
    count = int(input(f"Enter books borrowed by member {i+1}:"))
    borrow_counts.append(count)

average = sum(borrow_counts) / n 
print("Average books borrowed:", average)

higest = max(borrow_counts)
lowest = min(borrow_counts)

print("Higest borrow count:", higest)
print("Lowest borrow count:", lowest)

zero_count = borrow_counts.count(0)
print("Members with zero borrowings:", zero_count)

frequency = Counter(borrow_counts)
max_frequency = max(frequency.values())

mode = []
for key, value in frequency.items():
    if value == max_frequency:
        mode.append(key)

        print("Most frequent borrow count (Mode):", mode)