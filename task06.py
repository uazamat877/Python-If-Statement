son = (input("raqam kiriting:"))

raqam = son[:2]

if raqam == "90" or raqam == "91":
    print("Ucell")
elif raqam == "93" or raqam == "94":
    print("Beeline")
elif raqam == "95" or raqam == "97":
    print("Uzmobile")
elif raqam == "88" or raqam == "99":
    print("Mobiuz")
else:
    print("Boshqalar")