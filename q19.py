income = 45000
tax_payable = 0
print("Given income:", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # Tax on first 10k is 0. Tax on the rest is 10%
    tax_payable = (income - 10000) * 10 / 100
else:
    # First 10,000 (0% tax)
    # Next 10,000 (10% tax = 1,000)
    tax_payable = 0 + (10000 * 10 / 100) 
    # Remaining income (20% tax)
    tax_payable += (income - 20000) * 20 / 100

print("Total income tax to pay is", tax_payable)