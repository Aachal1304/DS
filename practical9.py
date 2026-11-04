class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None


# Insert operation
def insert(r, x):
    if not r:
        return Node(x)

    if x < r.x:
        r.l = insert(r.l, x)
    elif x > r.x:
        r.r = insert(r.r, x)

    return r


# Search operation
def search(r, x):
    if not r or r.x == x:
        return r

    if x < r.x:
        return search(r.l, x)
    else:
        return search(r.r, x)


# Delete operation
def delete(r, x):
    if not r:
        return r

    if x < r.x:
        r.l = delete(r.l, x)

    elif x > r.x:
        r.r = delete(r.r, x)

    else:
        if not r.l:
            return r.r

        if not r.r:
            return r.l

        t = r.r
        while t.l:
            t = t.l

        r.x = t.x
        r.r = delete(r.r, t.x)

    return r


# Display (Inorder Traversal)
def display(r):
    if r:
        display(r.l)
        print(r.x, end=" ")
        display(r.r)


# Main Program
root = None

while True:
    print("\n1. Insert  2. Delete  3. Search  4. Display  5. Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        root = insert(root, int(input("Value: ")))

    elif ch == 2:
        root = delete(root, int(input("Value: ")))

    elif ch == 3:
        x = int(input("Value: "))
        print("Found" if search(root, x) else "Not found")

    elif ch == 4:
        display(root)
        print()

    elif ch == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")