import pandas as pd

def load_data():
    data=pd.read_csv("input_20",sep=",",header=None)
    data=data.replace("p=<","",regex=True).replace("v=<","",regex=True).replace("a=<","",regex=True).replace(">","",regex=True)
    data=data.astype(int)
    return data

def find_closest():
    data=load_data()

    for i in range(400):
        data[5]+=data[8]
        data[4]+=data[7]
        data[3]+=data[6]
        data[2]+=data[5]
        data[1]+=data[4]
        data[0]+=data[3]

        data['sum']=abs(data[0])+abs(data[1])+abs(data[2])

    particle= (data[data['sum']==data['sum'].min()].index.values.astype(int)[0])
    print ("The closest particle is:",particle)

def find_closest_collision():

    data=load_data()

    for i in range(400):
        data.drop_duplicates(subset=[0,1,2],keep=False,inplace=True)
        data[5]+=data[8]
        data[4]+=data[7]
        data[3]+=data[6]
        data[2]+=data[5]
        data[1]+=data[4]
        data[0]+=data[3]
        #data['sum']=abs(data[0])+abs(data[1])+abs(data[2])

    print ("The remaining number of particles is:",data.shape[0])
