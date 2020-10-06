f=open("test.txt")
d=dict()
num=0

for line in f:

    for words in line.split():
        if words in d.keys():
            d[words]=d[words]+1
            if d[words]>num:
                num=d[words]
        else:
            d[words]=1
f.close()

f=open("test.txt","a")
f.write("\n" +str(d)),

f.close()

