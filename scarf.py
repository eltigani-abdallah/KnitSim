needle= ["-","-","-","-","-","-","-","-","-","-"]

def scarf():
    row=0
    while row<=10:
        for i in range(len(needle)):
            if i==0:
                needle[i]="sl"
            elif i%2!=0:
                needle[i]="p"
            else:
                needle[i]="k"
            if "-" not in needle:
                row+=1
                print(needle)
    
            

scarf()
    

