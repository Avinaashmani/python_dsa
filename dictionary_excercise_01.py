## Membership card hash table ##

# use terminal to add, del, change and 
# access user information 

import csv 

class Membership:

    def __init__(self):

        self.file_name = 'user_data_membership_card.csv'
        self.new_member = {}
        self.rows = []
        self.flag = False
        self.command = None
    
    def compute_input(self):
        self.open_file()
        self.command = input("Action: ")
        
        self.command = str(self.command)
        if self.command == "a":
            self.add()
        elif self.command == "d":
            key = input("Enter Member Key: ")
            self.del_member(key=key)
        print(self.add())
    def open_file(self):
        
        with open(self.file_name, 'rw') as f:
            reader = csv.DictReader(f)
            self.rows = [row for row in reader]
        with open(self.file_name, "w") as write_file:
            if self.flag == True:
                writer = csv.DictWriter(write_file, fieldnames=list)
                for key, value in self.new_member.items():
                    writer.writerows([key, value])

    def add(self):
        
        #ssn = input("Enter SSN Number: ")
        #gender = input("Enter Gender: ")
        #birthdate = input("Enter Date of birth: ")
        #maiden_name = input("Enter Middle name: ")
        #first_name = input("Enter First name: ")
        #last_name = input("Enter Last name: ")
        #address = input("Enter Address: ")
        #city = input("Enter City: ")
        #state = input("Enter State: ")
        #zip_code = input("Enter Zip: ")
        #phone = input("Enter Phone No: ")
        #email = input("Enter Email Address: ")
        #cc_type = input("Enter CC Type: ")
        #ccn = input("Enter CCN No: ")
        #cc_cvc = input("Enter CC CVC No: ")
        #cc_expiredate = input("Enter CC Expiredate: ")
        
        self.new_member = {'city': "Tambaram", 'cc_expiredate':"2023/12/22", 'zip':"600059", 
                    'phone': "9150939405", 'last name': "Manivelan", 
                    'gender': "m", 'maiden name': "Srinivasan", 
                    'cc_cvc': "898", 'birthdate': "1998/14/07", 'first name': "Avinaash",
                     'state': "Tamil nadu", 'CCN': "898", '\xef\xbb\xbfSSN': "89823", 
                     'address': "Sri sai shisti apartments", 'cc_type': "v", 'email': "avinaash.mani@gmail.com"}

        self.rows.append(self.new_member)
        self.flag = True
        return self.rows 
    
    def del_member(self, key):
        for data in self.rows:
            if data[key] == key:
                del data[key]
if __name__=='__main__':
    
    membership = Membership()
    membership.compute_input()
    #print(membership.add())
