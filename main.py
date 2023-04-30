print ("Write P if you want to know perimeter,S if square,C if calculator and I to chat bot")
answer1=input()
if answer1=="P":
    print("Write S if you want to know square,C if circle,R if restangle and T to triangle")
    answer2=input()
    if answer2=="S":
        print("Write a")
        a1=input()
        f1=int(a1)+int(a1)+int(a1)+int(a1)
        print(f1)
    if answer2=="C":
       print("write radius")
       r1=input()
       f2=2 * 3,1415926535 * int(r1)
       print(f2)
    if answer2=="T":
        print("write a")
        a2=input()
        print("write b")
        b1=input()
        print("write c")
        c1=input()
        f3=int(a2)+int(b1)+int(c1)
        print(f3)
    if answer2=="R":
        print("write a")
        a3=input()
        print("write b")
        b2=input()
        f4=int(a3)+int(b2)+int(a3)+int(b2)
        print(f4)
if answer1=="S":
    print("Write S if you want to know square,C if circle and R if restangle")
    answer3=input()
    if answer3=="S":
        print("write a")
        a4=input()
        f5=int(a4)*int(a4)
        print(f5)
    if answer3=="C":
        print("write radius")
        r2=input()
        f6=int(r2)*int(r2)*3,1415926535
        print(f6)
    if answer3=="R":
        print("write a")
        a5=input()
        print("write b")
        b3=input()
        f7=int(a5)*int(b3)
        print(f7)
if answer1=="C":
    print("write a")
    a6=input()
    print("write b")
    b4=input()
    print("write sign")
    sign1=input()
    if sign1=="+":
        f8=int(a6)+int(b4)
        print(f8)
    if sign1=="-":
        f9=int(a6)-int(b4)
        print(f9)
    if sign1=="*":
        f10=int(a6)*int(b4)
        print(f10)
    if sign1=="/":
        f11=int(a6)/int(b4)
        print(f11)
if answer1=="I":
    a=input()
    if a=="hello":
        print("hello")
    b=input()
    if b=="how are you":
        print("I'm ok,how are you")
    c=input()
    if c=="i'm ok":
        print("goodbye")
    d=input()
    if d=="Nurlan":
        print("It's my name!!!")

        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        