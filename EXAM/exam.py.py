while True:
    print("\nWelcome to the Bill Splitter App!")

    bill = float(input("Enter total bill amount: "))
    if bill <= 0:
        print("Bill must be positive.")
        continue

    people = int(input("Enter number of people: "))
    if people <= 0:
        print("Number of people must be greater than 0: ")
        continue

    tippercent = int(input("Enter tip percentage (0/5/10/15/20): "))
    if tippercent not in [0, 5, 10, 15, 20]:
        print("Tip must be one of 0, 5, 10, 15, 20:")
        continue

    tip = (tippercent / 100) * bill
    Final_bill = bill + tip
    per_person = Final_bill / people
    print(f"\nTip Amount: ₹{tip}")
    print(f"\ntotal bill(with Tip): ₹{bill + tip}")
    print(f"\nEach person should pay: ₹{ Final_bill / people}:")
     
    print(input("\nWould you like calculate another bill? (y/n): "))
    
    
         