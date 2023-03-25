#Tip calculator project


print("Welcome to the tip calculator.")
tot_bill =float(input("what was the total bill?$"))
perc_tip =float(input("What percentage tip would you lilke to give? 10, 12, or 15? "))
no_split =float(input("How many people to split the bill?"))
pay_each = (tot_bill+tot_bill*(perc_tip/100))/no_split
final = "{:.3f}".format(pay_each)
print(f"Each person should pay :${final}")
