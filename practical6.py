Size = 10
table = [[] for _ in range(Size)]

def insert(key, value):
    index = key % Size

    for i, (k, v) in enumerate(table[index]):
        if k == key:
            table[index][i] = (key, value)
            print("Key updated.")
            return
        table[index].append((key, value))
        print("Key inserted.")

def search(key):
    index = key % Size
    for k, v in table[index]:
        if k == key:
            print("Value:", v)
            return
        print("Key not found.")

def delete(key):
    index = key % Size
    for item in table[index]:
        if item [0] == key:
            table[index].remove(item)
            print("Key deleted.")
            return
        print("Key not found.")

        while True:
            print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
            ch = int(input("Enter choice:"))

            if ch == 1:
                key = int(input("Enter key:"))
                value = input("Enter value:")
                insert(key, value)

            elif ch == 2:
                key = int(input("Enter key:"))
                search(key)

            elif ch == 3:
                key = int(input("Enter key:"))
                delete(key)

            elif ch == 4:
                for i in range(Size):
                    print(i, ":" , table[i])

            elif ch == 5:
                break

            else:
                print("Invalid choice!")

