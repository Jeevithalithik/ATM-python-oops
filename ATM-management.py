class atm():
   def __init__(self,name,accnum,amount,pin):
      self.name=name
      self.accnum=accnum
      self.pin=pin
   def ind(self):
      global a
      z=int(input("enter the account number:"))
      for i in accnum:
        if(i==z):
           a=accnum.index(i)
      print("welcome",name[a])
   def pi(self):
      y=int(input("enter the pin number:"))
      if(y==pin[a]):
         x=str(input("which type of transaction do you want:deposite (or) withdraw (or) balance:"))
         if(x=="deposite"):
            u=int(input("enter the amount"))
            u1=amount[a]+u
            print("your deposite amount is:",u)
            print("balance amount:",u1)
         elif(x=="withdraw"):
            u=int(input("enter the amount:"))
            u1=amount[a]-u
            print("your withdraw amount is:",u)
            print("balance amount:",u1)
         elif(x=="balance"):
            u1=amount[a]
            print("balance amount:",u1)
         else:
            print("your pin is incorrect")
name=["priya","jeeva","lithik","ramesh","hari","rajesh"]
accnum=[1100,1200,1300,1400,1500,1600]
amount=[10000,5000,12000,15000,20000,30000]
pin=[1223,4562,7893,4567,9087,1245]
obj=atm(name,accnum,amount,pin)
obj.ind()
obj.pi()
                  