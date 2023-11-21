#!/usr/bin/env python 
import random

class ArrayImplemntation:

    def __init__(self) -> None:
        
        self.array_ = []
        self.value = 0.0
        
        self.prev_01 = 0.0
        self.prev_02 = 0.0
        self.current = 0.0

        self.error_thresh = 1.0
        self.error = 0.0

    def generate_value (self):
        while True:
            self.value = random.randint(100, 200)
            #print (self.value)
            return self.value

    def store_value(self):

        for i in range(0, 3):
            self.array_.append(self.generate_value())
        #print(self.array_)

    def error_check(self):

        for i in range (0, 3):
            self.array_.append(self.generate_value())
        self.prev_01 = self.array_[0]
        self.prev_02 = self.array_[1]
        self.current = self.array_[2]

        #if self.prev_01 and self.prev_02 is not None:

        self.error = abs(self.prev_01 - self.prev_02)
        while self.current >= 150:
            if self.prev_02 != 150 and self.prev_02 <150:
                print("HERE 1")
                self.current = self.prev_02
            elif self.prev_01 != 150 and self.prev_01 <150:
                print ("HERE 2")
                self.current = self.prev_01 
            else:
                pass
            break
        print(self.current) 
        print(self.array_)                     

if __name__ == '__main__':

    array_imply = ArrayImplemntation()
    try:
        array_imply.error_check()
    except IndexError as e:
        print (e)
        pass