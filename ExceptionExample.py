


try:
    imp = input("Enter a number: ")
    imp_int = int(imp)
except ValueError:
    int_int = None
    print("That's not a number !")
except NameError:
    print("Name error")
except:
    print("I have no idea")





