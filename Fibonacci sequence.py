# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
x = 0
if nterms<=0:
   print("Enter positive integer")
elif nterms==1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")

   '''#Using For Loop
   for i in range(1):
      for j in range(nterms):
         print(n1)
         nth=n1+n2
         n1,n2=n2,nth'''


  #Using While Loop
   while x < nterms:
      print(n1)
      (n1,n2)=(n2,n1+n2)
      x=x+1
   