def linear_search(account_ids, key):
    for i in range(len(account_ids)):
        if account_ids[i] == key:
            return i
    return -1

# Customer account IDs list
account_ids = [101, 205,309, 412, 550]

# Account ID to search
key = int(input("Enter customer account ID to search:"))

# Calling linear search
result = linear_search(account_ids, key)

if result != -1:
    print("Account id found at index:", result)
else:
    print("Account id not found:")
