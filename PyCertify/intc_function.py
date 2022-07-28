# Certify a previously defined integer:

def intc(input, positive = True, zero = True, keep = False):

    string = str(input) 

    number = []

    digits = ["9","8","7","6","5","4","3","2","1","0"]

    for i in string:
       number.append(i)

    number_copy = number[:]

    try:
        int(input)
    except:
        if not keep:
            return False

        if keep:
            for i in number:
                if i not in digits:
                    number_copy.remove(i)
            return int("".join(number_copy))
                    
     
    if positive:
        if int(input) < 0:
            if keep:
                string = str(input * -1)
                
            if not keep:
                return False


    if not zero:
        if not keep: 
            if int(input) == 0:
                return False


    if keep:
        return int(string)
    else:
        return True