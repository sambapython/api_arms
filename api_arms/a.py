print("hello")
def fun():
    try:
        for i in range(-3,10,3):
            print(i)
            break 
            print("hi")
        else:
            print("this is else block")
    except Exception as err:
        print(err)
    finally:
        print("this is finally")
    print("HI!@#")

fun()
