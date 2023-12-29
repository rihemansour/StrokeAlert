def encode_gender(x):
    if(x=="Male"):
        return 1
    if (x=="Female"):
        return 0
    return x

def encode_work_type(x):
    if(x=="Private"):
        return 4
    if(x=="Self employed"):
        return 3
    if(x=="Government job"):
        return 2
    if(x=="I'm a child"):
        return 1
    if(x=="Never worked"):
        return 0
    
def encode_residence_type(x):
    if(x=="Urban"):
        return 1
    if(x=="Rural"):
        return 0

def encode_yes_no(x):
    if(x=="Yes"):
        return 1
    if(x=="No"):
        return 0
    