number = 20

def outer_func():
    print(f"search outer_func: {globals()}")
    number = 40
    def enc_func():
        print("search enclousing scope")
        def local_func():
            print(f"search local_func: {number}")
        local_func()
    enc_func()

outer_func()
