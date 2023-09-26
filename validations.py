import re
import datetime
def isNameValid(str):
    l = str.split()
    for i in l:
        if not i.isalpha() or not i[0].isupper():
            return False
    if len(l) == 3:
        return True
    
    return False

def isMobileValid(str):
    if len(str)==10:
        if str.isdigit():
            return True
        else:
            return False
    else:
        return False

def isIdValid(str):
    if str.isdigit():
        return True
    else:
        print("Employee id is:",str)
        return False

def isAgeValid(str):
    if int(str)>18 and str.isdigit and int(str)<100:
        return True
    return False

def isSalValid(str):
    if str.isdigit and int(str)>0:
        return True
        if sal==0:
            return False


def isDobValid(str):
    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(date_pattern,str):
        return False
    day, month, year = map(int, str.split('-'))
    current_year = datetime.datetime.now().year
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and ((year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28))) or (day > 31):
        return False
    if year > current_year:
        return False
    return True


def isAadharValid(adno):
    if adno.isdigit() and len(adno)==12:
        return True
    else:
        return False
        

def isPanValid(str):
    if len(str) == 10:
        if str[:5].isalpha() and str[:5].isupper() and str[5:9].isdigit() and str[9].isalpha() and str[9].isupper():
            return True
    return False

def isGenderValid(str):
    common_genders = ["Male", "Female", "Other"]

    if str in common_genders:
        return True
    else:
        return False

def isAddressValid(str):
    if str.isalnum() and len(str)>0:
        return True
    else:
        return False

def isCityValid(str):
    if str.isalpha() and len(str)>0:
        return True
    else:
        return False

def isDnameValid(str):
    if str.isalpha() and len(str.split())>0:
        return True
    else:
        return False

def isDesiValid(str):
    if str.isalpha() and len(str.split())>0:
        return True
    else:
        return False








    


    
