with open("currency.txt") as f:
    lines=f.readlines()

currency_dict={}
for line in lines:
    parsed=line.split("\t")
    currency_dict[parsed[0]]=parsed[1]

amount=float(input("Enter the amount: \n"))
print("Enter the name of the currency you want to convert this amount to? Available options: \n",
      currency_dict.keys())
[print(item) for item in currency_dict.keys()]
currency=input("Please enter one of these values: \n")
print(f"{amount} INR is equal to: {amount * float(currency_dict[currency])} {currency}")


