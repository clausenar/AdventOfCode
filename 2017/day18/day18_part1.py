data=open("./data/18.txt")

register=[]

for i in data:
    if len(i.split())==2:
        inst,key=i.split()
        register.append([inst,key])
    else:
        inst,key,val=i.split()
        register.append([inst,key,val])

index=0
freq=0
value=0
song={}

while index>=0 and index<len(register):
    if len(register[index])==2:
        inst=register[index][0]
        key=register[index][1]
    if len(register[index])==3:
        inst=register[index][0]
        key=register[index][1]
        val=register[index][2]
    if inst=="snd":
        key_last=key
        val_last=song[key]
        index+=1
    elif inst=="set" and val.isdigit():
        song[key]=val
        index+=1
    elif inst=="set":
        song[key]=song[val]
        index+=1
    elif inst=="add":
        song[key]=int(song[key])+int(val)
        index+=1
    elif inst=="mul" and val.isdigit():
        song[key]=int(song.get(key,0))*int(val)
        index+=1
    elif inst=="mul" and not val.isdigit():
        song[key]=int(song.get(key,0))*int(song.get(val,0))
        index+=1
    elif inst=="mod" and val.isdigit():
        song[key]=int(song[key])%int(val)
        index+=1
    elif inst=="mod" and not val.isdigit():
        song[key]=int(song[key])%int(song[val])
        index+=1
    elif inst=="rcv" and song[key]!=0:
        print ("this is last played",val_last)
        break
    elif inst=="jgz" and int(song[key])>0:
        index=index+int(val)
    elif inst=="jgz" and int(song[key])==0:
        index=index+1
