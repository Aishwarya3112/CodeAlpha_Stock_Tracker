#getting the user stock name and prices
 
Stock_prices={}
n=int(input("Enter the no of stocks you need:"))
file=open("Stock_Tracker.txt",'w')
for i in range(n):
    name=input("Enter Stock name:").upper()
    try:
        price=float(input(f"Enter the price of {name}:"))
    except ValueError:
        print("Inavlid Price ! Please enter a number.")
        continue
    Stock_prices[name]=price
    file.write(f"{name} : {price}\n")
file.close()

#Getting the Quantity  
   
Portfolio={}
Total_Investment=0
file=open("Stock_Tracker.txt",'a')
for stock in Stock_prices:
    try:
        share=int(input(f"Enter the quantity of shares:"))
    except ValueError:
        print("Inavlid Quantity ! Please enter a Wholenumber.")
        continue
    Portfolio[stock]=share
    Investment=share*Stock_prices[stock]
    Total_Investment+=Investment
    file.write(f"{stock}: {Stock_prices[stock]} x {share} share = {Investment}\n")
file.write(f"\nTotal_Investment: {Total_Investment}\n")
file.close()

#Read and Display the Stock

try:
    file=open("Stock_Tracker.txt",'r')
    print("Portfolio Summary:")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found ! , Please try again")


    