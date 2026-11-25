medical_cause = input("Do you have a medical cause? Y/N: ").strip().upper()

if medical_cause == 'Y':
    print("You have been granted the permission to take part in the exam.")

else:
    attendance = int(input("Type in attendance: "))

    if attendance >= 75:
        print("Allowed.")

    else:
        print("Not allowed haha.")