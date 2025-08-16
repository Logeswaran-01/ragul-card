tamil = int(input("Enter your tamil mark:"))
english = int(input("Enter your english mark:"))
maths=int(input("Enter your maths mark:"))
physics =int(input("Enter your physics mark:"))
chemistry = int(input("Enter your chemistry mark:"))
cs = int(input("Enter your computer science mark:"))
average = (tamil+english+maths+physics+chemistry+cs)/6

if(average < 35):
  print("POOR STUDENT")

if(average > 35 and average<70):
  print("AVERAGE STUDENT")

else:
  print("GOOD STUDENT")