l = []
while True:
    c = int(input('''
        1 Push Element
        2 Pop First Elements
        3 Front Element
        4 Last Element
        5 Display Stack
        6 Exit

        '''))
    if c == 1:
        n = input("Enter The Value:-");
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Empty Queue:")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Value", l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Value", l[-1])

    elif c==5:
        print("Display Queue",l)

    elif c == 6:
        break;
    else:
        print("invalid opr...")