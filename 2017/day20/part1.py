import pandas as pd

data=pd.read_csv("input",sep=",",header=None)
data=data.replace("p=<","",regex=True).replace("v=<","",regex=True).replace("a=<","",regex=True).replace(">","",regex=True)
data=data.astype(int)

def find_closest():

    for i in range(2000):
        old_data=data
        data[0]+=data[3]
        data[1]+=data[4]
        data[2]+=data[5]
        data[3]+=data[6]
        data[4]+=data[7]
        data[5]+=data[8]
        data['sum']=abs(data[0])+abs(data[1])+abs(data[2])
        #data.drop_duplicates([0,1,2],keep=False,inplace=True)
        #data=data.append(old_data)
    particle= (data[data['sum']==data['sum'].min()].index.values.astype(int)[0])
    print ("The closest particle is:",particle)
