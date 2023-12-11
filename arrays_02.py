import sys
inp1 = None
arr1 = [3,3]
while True:
    if inp1 == 'stop':
        arr1.pop()
        print(arr1)
        sys.exit(0)
    else:
        inp1= str(input("Enter Data "))
        arr1.append (inp1)

