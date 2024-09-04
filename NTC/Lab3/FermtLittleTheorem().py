import math
def checkprime(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if(a%(i+1) == 0):
            return 0
    return 1


def fermtlittle(a,p):
    if(checkprime(p)==1):
            
        if(int((a**(p-1))% p)==1):
            return("it follows Fermt Little")
        else:
            return ("doesnt follow fermt little")
    else:
        return ("Doesent Follow the Required conditions")

print(fermtlittle(2,3))