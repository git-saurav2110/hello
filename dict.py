d=dict({4:45,5:46 })
d[0]=123
d[1]=456

print("whole dictionary : ",d)
print("whole dictionary key  ->  ",d.keys())
print("whole dictionary values ->  ", d.values())
for i in d:
    print(i," : ",d[i])
