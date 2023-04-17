
arr = []
def checkerrors(ar_):
    try:
        len(ar_) < 5
    except:
        print("Too many problems ")    
    while(len(ar_) < 5): 
        usr = input("please enter an arithmetic problem: ")
        if usr == "True":
            arithmetic_arranger(ar_,True)
            break
        lst = usr.split()
        
        try:
            num_1 = int(lst[0])
            num_2 = int(lst[2])
        except:
            print("numbers must only contain digits") 
            continue   
        if lst[1] == "+" or lst[1] == "-":
            True
        else:
            print("operator must be + or - " )
            continue
        if string_count(lst[0]) <= 4 and string_count(lst[2]) <= 4:
            True
        else:
            print("numbers cannot be more than 4 digits ")
            continue        
        ar_.append(usr)
    arithmetic_arranger(ar_,True)    
    return(ar_)
    
def string_count(str):
    count = 0
    for i in str:
        count = count + 1
    return count    
  
def arithmetic_arranger(lst,bool):
    inde = 0
    c = 0
    d = 0
    num_1 = 0
    num_2 = 0
    op = 0
    for i in lst:
        inde = i.split()
        if string_count(inde[0]) > string_count(inde[2]):
            c = string_count(inde[0])
            d = string_count(inde[2])
            num_1 = int(inde[0])
            num_2 = int(inde[2])
            if inde[1] == "+":
                ans = num_1 + num_2
                op = str(ans)
                op = len(op)
            else:
                ans = num_1 - num_2  
                op = str(ans)
                op = len(op)
            print("  ", inde[0],"\n",inde[1]," "*(c-d-1),inde[2],"\n","_"*(c+2),"\n"," "*(c+1-op),ans,"\n")
        else:
            num_1 = int(inde[0])
            num_2 = int(inde[2])
            c = string_count(inde[2])
            d = string_count(inde[0])
            if inde[1] == "+":
                ans = num_1 + num_2
                op = str(ans)
                op = len(op)
            else:
                ans = num_1 - num_2
                op = str(ans)
                op = len(op)    
            print(" "*(c-d+2), inde[0],"\n",inde[1],inde[2],"\n","_"*(c+2),"\n"," "*(c+1-op),ans,"\n")         
checkerrors(arr)
