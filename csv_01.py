## test functions of CSV library ##

import csv 
file_name = 'user_data_membership_card.csv'
arr = []
with open(file_name) as f:
    reader = csv.DictReader(f)
    #next(reader)    # skip over the first header row
    rows = [row for row in reader]
for i in enumerate(rows):
    ssn = str(i[1])
    arr.append(str(i))
#print(ssn)
splited = ssn.split(',')

ssn_ = splited[0]
gender_ = splited[1]
birth_date_ = splited[2]
maidenName_ = splited[3]
lastName_ = splited[4]
firstName_ = splited[5]
address_ = splited[6]
city_ = splited[7]
state_ = splited[8]
zip_ = splited[9]
phone_ = splited[10]
email_ = splited[11]
cc_type_ = splited[12]
ccn_ = splited[13]
cc_cvc_= splited[14]
cc_expiredate_ = splited[15]

personal = [] ## age - gender - birthday
name = [] ## maidenname - lastname - firstname 
location = [] ## address - city - zip
contact = [] ## phone - email
card_info = [] ## cc_type - ccn - cc_cvc - cc_expiredate 


def get_hashkey(key, arr):

    hash_key = 0
    key_len = len(arr)

    for char in key:
        hash_key += ord(char)
    return hash_key % key_len



def print_all():
    print(ssn_)
    print(gender_)
    print(birth_date_)
    print(maidenName_)
    print(lastName_)
    print(firstName_)
    print(address_)
    print(city_)
    print(zip_)
    print(phone_)
    print(email_)
    print(cc_type_)
    print(cc_cvc_)
    print(cc_expiredate_)
    print(len(arr))
#print(get_hashkey(ssn_, rows))
#print_all()
#print(arr)
details = str(arr[16]).split(',')
details_2 = str(arr[17].split(','))
#print(details)
x = []
y = []
x.append(details[4])
x.append(details[5])
x.append(details[6])

y.append(details_2[4])
y.append(details_2[5])
y.append(details_2[6])
z = rows[25]
personal.append(x)
personal.append(y)
print(z)