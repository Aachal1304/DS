Size = 10
table = [None] * Size
DELETED = "DELETED"

def insert(key):
    index = key % Size
    for i in range(Size):
        pos = (index + i) % Size
        if table[pos] is None or table[pos] == DELETED:
            table[pos] = key
            print("Key inserted.")
            return
        if table[pos] == key:
           print("Key already exists.")
           return
        print("Hash table is full.")

def search(key):
    index = key % Size
    for i in range(Size):
        pos = (index + i) % Size
        if table[pos] is None:
            break
        if table[pos] == key:
            print("Key found at index", pos)
            return
        print("Key not found.")

def delete(key):
    index = key % Size
    for i in range(Size):
        pos = (index + i) % Size
        if table[pos] is None:
            break
        if table[pos] == key:
            table[pos] = DELETED
            print("Key deleted.")
            return
        print("Key not found.")

        def display():
            for i in range(Size):
                print(i, ":", table[i])

        while True:
            print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
            ch = int(input("Enter choice:"))

            if ch == 1:
                insert(int(input("Enter key:")))

            elif ch == 2:
                search(int(input("Enter key:")))

            elif ch == 3:
                delete(int(input("Enter key:")))

            elif ch == 4:
                display()

            elif ch == 5:
                break

            else:
                print("Invalid choice!")

