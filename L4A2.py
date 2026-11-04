Amount = int(input("Enter your amount here: "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100 available:", note_1)
print("Notes of 50 available:", note_2)
print("Notes of 10 available:", note_3)