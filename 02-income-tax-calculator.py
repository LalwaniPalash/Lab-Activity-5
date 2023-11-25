import time

print("\nIncome Tax Calculator\n")
time.sleep(2)

try:
    tax_regime = input("What tax regime would you like to opt for? (old/new): ").lower()
except ValueError:
    print("Error: Invalid Input!")

try:
    total_income = int(input("What is your total income?: "))
except ValueError:
    print("Error: Invalid Input!")

if tax_regime == "old":
    entity_type = input("Are you a Resident individual(RI) / HUF / AJP / AOP / BOI or a Non-Resident Individual(NRI)?: ").lower()
    if entity_type in ["ri", "resident", "resident individual"]:
        age = int(input("What is the person's age?: "))
    if entity_type in ["huf", "ajp", "aop", "boi", "nri", "non resident", "non-resident"] or (entity_type in ["ri", "resident", "resident individual"] and age < 60):
        
        slab1_limit = 250000
        slab2_limit = 500000
        slab3_limit = 1000000
        rate_slab1 = 0.05
        rate_slab2 = 0.2
        rate_slab3 = 0.3

        if total_income <= slab1_limit:
            income_tax = 0
        elif total_income <= slab2_limit:
            income_tax = (total_income - slab1_limit) * rate_slab1
        elif total_income <= slab3_limit:
            income_tax = (slab2_limit - slab1_limit) * rate_slab1 + (total_income - slab2_limit) * rate_slab2
        else:
            income_tax = (slab2_limit - slab1_limit) * rate_slab1 + (slab3_limit - slab2_limit) * rate_slab2 + (total_income - slab3_limit) * rate_slab3

        surcharge_rate = 0
        if 5000000 < total_income <= 10000000:
            surcharge_rate = 0.1
        elif 10000000 < total_income <= 20000000:
            surcharge_rate = 0.15
        elif 20000000 < total_income <= 50000000:
            surcharge_rate = 0.25
        elif total_income > 50000000:
            surcharge_rate = 0.37

        surcharge = income_tax * surcharge_rate

        cess_rate = 0.04
        cess_base = income_tax + surcharge if surcharge_rate > 0 else income_tax
        cess = cess_base * cess_rate

        print(f"\nYour income tax for the year is: Rs. {income_tax:.2f}")
        print(f"Surcharge on income tax is: Rs. {surcharge:.2f}")
        print(f"Cess on tax (including surcharge) is: Rs. {cess:.2f}")
        print(f"Total tax payable (including surcharge and cess) is: Rs. {income_tax + surcharge + cess:.2f}")

    elif entity_type in ["ri", "resident", "resident individual"] and 60 <= age <= 79:

        slab1_limit_senior = 300000
        slab2_limit_senior = 500000
        slab3_limit_senior = 1000000
        rate_slab1_senior = 0.05
        rate_slab2_senior = 0.2
        rate_slab3_senior = 0.3

        if total_income <= slab1_limit_senior:
            income_tax = 0
        elif total_income <= slab2_limit_senior:
            income_tax = (total_income - slab1_limit_senior) * rate_slab1_senior
        elif total_income <= slab3_limit_senior:
            income_tax = (slab2_limit_senior - slab1_limit_senior) * rate_slab1_senior + (total_income - slab2_limit_senior) * rate_slab2_senior
        else:
            income_tax = (slab2_limit_senior - slab1_limit_senior) * rate_slab1_senior + (slab3_limit_senior - slab2_limit_senior) * rate_slab2_senior + (total_income - slab3_limit_senior) * rate_slab3_senior

        surcharge_rate = 0
        if 5000000 < total_income <= 10000000:
            surcharge_rate = 0.1
        elif 10000000 < total_income <= 20000000:
            surcharge_rate = 0.15
        elif 20000000 < total_income <= 50000000:
            surcharge_rate = 0.25
        elif total_income > 50000000:
            surcharge_rate = 0.37

        surcharge = income_tax * surcharge_rate

        cess_rate = 0.04
        cess_base = income_tax + surcharge if surcharge_rate > 0 else income_tax
        cess = cess_base * cess_rate

        print(f"\nYour income tax for the year is: Rs. {income_tax:.2f}")
        print(f"Surcharge on income tax is: Rs. {surcharge:.2f}")
        print(f"Cess on tax (including surcharge) is: Rs. {cess:.2f}")
        print(f"Total tax payable (including surcharge and cess) is: Rs. {income_tax + surcharge + cess:.2f}")

    elif entity_type in ["ri", "resident", "resident individual"] and age >= 80:
    	slab1_limit_very_senior = 500000
    	slab2_limit_very_senior = 1000000
    	rate_slab1_very_senior = 0.2
    	rate_slab2_very_senior = 0.3 

    	if total_income <= slab1_limit_very_senior:
    		income_tax = 0
    	elif total_income <= slab2_limit_very_senior:
    		income_tax = (total_income - slab1_limit_very_senior) * rate_slab1_very_senior
    	else:
    		income_tax = (slab2_limit_very_senior - slab1_limit_very_senior) * rate_slab1_very_senior + (total_income - slab2_limit_very_senior) * rate_slab2_very_senior

    	surcharge_rate = 0
    	if 5000000 < total_income <= 10000000:
    		surcharge_rate = 0.1
    	elif 10000000 < total_income <= 20000000:
    		surcharge_rate = 0.15
    	elif 20000000 < total_income <= 50000000:
    		surcharge_rate = 0.25
    	elif total_income > 50000000:
    		surcharge_rate = 0.37

    	surcharge = income_tax * surcharge_rate

    	cess_rate = 0.04
    	cess_base = income_tax + surcharge if surcharge_rate > 0 else income_tax
    	cess = cess_base * cess_rate

    	print(f"\nYour income tax for the year is: Rs. {income_tax:.2f}")
    	print(f"Surcharge on income tax is: Rs. {surcharge:.2f}")
    	print(f"Cess on tax (including surcharge) is: Rs. {cess:.2f}")
    	print(f"Total tax payable (including surcharge and cess) is: Rs. {income_tax + surcharge + cess:.2f}")

    else:
        print("Error: Invalid entity type.")
elif tax_regime == "new":

	slab1_limit_new = 300000
	slab2_limit_new = 600000
	slab3_limit_new = 900000
	slab4_limit_new = 1200000
	slab5_limit_new = 1500000
	rate_slab1_new = 0.05
	rate_slab2_new = 0.1
	rate_slab3_new = 0.15
	rate_slab4_new = 0.2 
	rate_slab5_new = 0.3

	if total_income <= slab1_limit_new:
		income_tax = 0
	elif total_income <= slab2_limit_new:
		income_tax = (total_income - slab1_limit_new) * rate_slab1_new
	elif total_income <= slab3_limit_new:
		income_tax = (slab2_limit_new - slab1_limit_new) * rate_slab1_new + (total_income - slab2_limit_new) * rate_slab2_new
	elif total_income <= slab4_limit_new:
		income_tax = (slab2_limit_new - slab1_limit_new) * rate_slab1_new + (slab3_limit_new - slab2_limit_new) * rate_slab2_new + (total_income - slab3_limit_new) * rate_slab3_new
	elif total_income <= slab5_limit_new:
		income_tax = (slab2_limit_new - slab1_limit_new) * rate_slab1_new + (slab3_limit_new - slab2_limit_new) * rate_slab2_new + (slab4_limit_new - slab3_limit_new) * rate_slab3_new + (total_income - slab4_limit_new) * rate_slab4_new
	else: 
		income_tax = (slab2_limit_new - slab1_limit_new) * rate_slab1_new + (slab3_limit_new - slab2_limit_new) * rate_slab2_new + (slab4_limit_new - slab3_limit_new) * rate_slab3_new + (slab5_limit_new - slab4_limit_new) * rate_slab4_new + (total_income - slab5_limit_new) * rate_slab5_new

	surcharge = 0
	if 5000000 < total_income <= 10000000:
		surcharge_rate = 0.1
	elif 10000000 < total_income <= 20000000:
		surcharge_rate = 0.15
	elif 20000000 < total_income <= 50000000:
		surcharge_rate = 0.25

	surcharge = income_tax * surcharge_rate

	cess_rate = 0.04
	cess_base = income_tax + surcharge if surcharge_rate > 0 else income_tax
	cess = cess_base * cess_rate

	print(f"\nYour income tax for the year is: Rs. {income_tax:.2f}")
	print(f"Surcharge on income tax is: Rs. {surcharge:.2f}")
	print(f"Cess on tax (including surcharge) is Rs. {cess:.2f}")
	print(f"Total tax payable (including surcharge and cess) is: Rs. {income_tax + surcharge + cess:.2f}")

else:
    print("Error: Invalid tax regime.")
