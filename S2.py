def kk():
    a = 45
    print(45)

    def ll():
        nonlocal a
        a = 42
        print(a)
    ll()
    print(a)
kk()

