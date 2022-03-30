from re import ASCII


a="saurav"
b=b'saurav'

c=a.encode('ASCII')
if(b==c):
    print("encoding successful")
else:
    print('not encoded')