print("Welcome to Expense_Tracker Application")
finish= False
TotalCost=0
while finish == False:
   Expense=input("Enter an expense name:")
   Cost=int(input("Enter its cost:"))
   print(Expense)
   TotalCost=TotalCost+Cost
   expense_status=input("Have spent on something else too?(yes/no)")
   if expense_status.lower()=="no": # If we don't use paranthese'()' it's simply means that I said look at it but do not run or initiate it.
      finish= True
print(TotalCost)      

