#while loop (claculator)
while True:
        
        a=float(input("enter any number"))
        b=float(input("enter any number"))
        op=input("enter a opreation you want to perform +,-,/,*")
        if(op=='+'):
            c=a+b
            print("addition of a,b",c)
        elif(op=='-'):
            c=a-b
            print("subtraction of a,b",c)
        elif(op=='*'):
            c=a*b
            print("multiplication of a,b",c)
        elif(op=='/'):
            if b==0:
                print("divison is not possible, please choose valid option")
            else:
                c=a/b
                print("divison of a,b",c)
                repeat=input("dou you want to repeat yes/no")
                if(repeat.lower()!='yes'):
                     break
        

         



        
