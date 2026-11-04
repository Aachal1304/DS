undo = []
redo = []
doc = ""

while True:
    print("\n1. Make change")
    print("n2. undo")
    print("n3. redo")
    print("n4. Display document")
    print("n5. Exit")

    ch = int(input("Enter choice:"))

    if ch == 1:
        undo.append(doc)
        text = input("Enter text:")
        doc = text
        redo.clear()

    elif ch == 2:
      if undo:
            redo.append(doc)
            doc = undo.pop()
      else:
          print("Nothing to undo!:")

    elif ch == 3:
        if redo:
            undo.append(doc)
            doc = redo.pop()
        else:
            print("Nothing to redo!:")

    elif ch == 4:
        print("Document:", doc)

    elif ch == 5:
        break
    else:
        print("Invalid choice:")
        
