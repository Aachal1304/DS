def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n):
        for j in range(n - i -1):
            if salaries[j] >salaries[j+1]:
             salaries[j], salaries[j+1] = salaries[j+1], salaries[j]
    return salaries

salaries = [48000.50, 70000.75, 63000.32, 75000.40,
            79000.32, 82000.64, 88000.74, 92000.78]

selection_salaries = salaries.copy()
selection_sort(selection_salaries)

print("Salaries using selection_sort:")
print(selection_salaries)
print("\n Top five higest salaries:")
print(selection_salaries[-5:])

bubble_salaries = salaries.copy()
bubble_sort(selection_salaries)

print("Salaries using bubble_sort:")
print(bubble_salaries)
print("\n Top five higest salaries:")
print(bubble_salaries[-5:])