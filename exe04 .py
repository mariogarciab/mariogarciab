#The variable sh was changed from previous exercise 03, but still same funtion as input for the hours  
sh = input("enter hours: ")
# the var sr was also altered since previous exercise
sr = input("enter rate: ")
#different distribution or accomodation for the same result // float was also added here
fh = float(sh)
fr = float(sr)
#the next line might remain as a comment or not depending on the wanted result
# print (fh, fr) 
#the next line is a block for if, I start working on the concept of tap 4 spaces as sub command
if fh > 40 :
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    print (reg,otp)
    xp = reg + otp
 #happends the same here with else is another block of code
else:
  #  print("Regular")
    xp = fh * fr
    print("Pay", xp)

