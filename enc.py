a='saurav'
b=b'saurav'
c=a.encode('ASCII')
d=c.decode('ASCII')
if(c==b):
    print('encoding successful')
else:
    print("not successful")
if(d==a):
    print('decode successful')
else:
    print("decode usuccessful")