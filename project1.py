# The rent calculator 
rent=input("Enter the monthly rent: ")
rent=float(rent)
food= input("Enter the monthly food expenses: ")
food=float(food)
electrycity_units=input("Enter the monthly electricity units consumed: ")
electrycity_units=float(electrycity_units)
chatge_per_unit=input("Enter the charge per unit: ")
chatge_per_unit=float(chatge_per_unit)
electrycity_bill= electrycity_units * chatge_per_unit
number_of_people=int(input("Enter the number of people sharing the rent: "))


total_monthly_expenses= (rent + food + electrycity_bill)// number_of_people
print("Total monthly expences every one should pay is : ", total_monthly_expenses)
