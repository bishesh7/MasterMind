
print("Do you think you are a mastermind? Well, let's check it out. I have selected "
      "four sets of colors out of six colors in specific arrangement.")
print('')
print("The colors are blue(b),white(w), green(g), yellow(y), oragne(o)and red(r)")
print('')
print("For each correct color in correct position, you get 'c' "
      "and for each correct color in misplaced position, you get 'm'.")
print('')
print("If you guess the color pattern in 10 chances, you are a mastermind!")
print('')
def color():          # function color generates colors.
    import random
    x=random.randrange(1,7)
    if x==1:
        t="b"
    elif x==2:
        t="w"
    elif x==3:
        t="g"
    elif x==4:
        t="y"
    elif x==5:
        t="o"
    else:
        t="r"
    return t

def cgs():       #cgs= computer generated seqence of colors.
    first= color()
    second= color()
    third= color()
    fourth= color()
    p=(str(first)+str(second)+str(third)+str(fourth))
    return p

r=cgs()

z=input("Enter the pattern of the color:")



life=10
while life>0:


    def compare(q):        #the function compare gives 'c' for correct color in correct position.
        if z[q]==r[q]:
            k ="c"
        else:
            k=""
        return k

    def other(q,i):       #the function other(q,i) gives 'm' for correct color in wrong position.
        if q!=i:
            if compare(q)=="c" or compare(i)=="c":
                k=""
            elif z[q]==r[i]:
                k="m"

            else:
                k=""
        else:
            k=""
        return k

    def sing(q):         # function sing applies other (q,i) to cgs and user's input.
            i=int(3)
            while i>=0:
                a=(other(q,i))
                if a=="m":
                    t=i
                    i=-1
                else:
                  i=i-1
                  t=5
            return t 
                    

    def bse():       # function bse excludes the matching of already matched colors multiple times.
        a=sing(0)
        b=sing(1)
        c=sing(2)
        d=sing(3)
        v=""
        if a!=5:
            v=v+"m"
        if b!=5 and b!=a:
            v=v+"m"
        if c!=5 and c!=a and c!=b:
            v=v+"m"
        if d!=5 and d!=a and d!=b and d!=c:
            v=v+"m"
      
        return v


    def ase():      #function ase applies compare to cgs and user's input.
        q=3
        n=""
        while q>=0:
            n=n+str(compare(q))
            q=q-1

        return n 

   

    def rat():    # function rat supplements sing and bse for unaccounted 'm's.
        

        if ase()=="":
            v=""
           
            if z[0]==z[1]==r[2]==r[3]:
                v=v+"m"
            if r[0]==r[1]==z[2]==z[3]:
                v=v+"m"
            if z[0]==z[2]==r[1]==r[3]:
                v=v+"m"
           
            if z[0]==z[3]==r[1]==r[2]:
                v=v+"m"
            if r[0]==r[3]==z[1]==z[2]:
                v=v+"m"
            if r[0]==r[2]==z[1]==z[3]:
                v=v+"m"
            
        else:
            v=""
        
        return v
        

        
    d=ase()
    l=bse()
    f=rat()


    if z==r:
      life=0
    else:
        print(str(d)+str(l)+str(f))
        print("try again")
        z=input("Enter the pattern of the color:")
        life=life-1

if z==r:
    print("well done! you are a mastermind! restart to play again.")
else:
    print("game over.the correct patternre is  "+str(r)+".  start to play again.")


