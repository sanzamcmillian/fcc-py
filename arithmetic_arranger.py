
arr = []
def checkerrors(ar_):
    if len(ar_) > 5:
        print("too many problems ")
          
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
    if len(ar_) == 5:
        arithmetic_arranger(ar_,True)    
    return(ar_)
    
def string_count(str):
    count = 0
    for i in str:
        count = count + 1
    return count    
  
def arithmetic_arranger(lst,bool):
    solutions = []
    for problem in lst:
        x, op, y = problem.split(' ')
        z = ""
        if op == "+":
            z = str(int(x) + int(y))
        if op == "-":
            z = str(int(x) - int(y))
        width = max(map(len, [x, y, z]))
        solutions.append([op, x, y, z, width])
    print("    ".join("  %*s" % (width, x) for (op, x, y, z, width) in solutions))
    print("    ".join("%s %*s" % (op, width, y) for (op, x, y, z, width) in solutions))
    print("    ".join("-" * (2 + width) for (op, x, y, z, width) in solutions))
    if bool:
        print('    '.join('  %*s' % (width, z) for (op, x, y, z, width) in solutions))
     
checkerrors(arr)