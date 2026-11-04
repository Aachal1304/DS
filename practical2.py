def binary_search(account_ids, key):
    low = 0
    high = len(account_ids) -1

    while low <= high:
        mid = (low + high) // 2

        if account_ids[mid] == key:
            return mid
        elif account_ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
# Customer account IDs list(must be sorted)
account_ids = [101, 205, 309, 412, 550]

# Account ID to search
key = int(input("Enter customer account id to search:"))

# Calling binary search
result = binary_search(account_ids, key)

if result != -1:
    print("Account id found at index:", result)
else:
    print("Account id not found:")

        