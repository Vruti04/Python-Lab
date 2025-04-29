#CP1
def lower_upper(x):
     s=0
     a=0
     for i in x:
          if (i.isupper()):
               s+=1
          if(i.islower()):
               a+=1
    return(s,a)
