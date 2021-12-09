import math
import numpy as np
import matplotlib.pyplot as plt


aaa=["5zas.pdb",  "6dwt.pdb",  "6dxj.pdb",  "6gn2.pdb",  "6gn3.pdb",  "6l75.pdb",  "6ror.pdb",  "6ros.pdb",  "6rou.pdb",  "6s7d.pdb"]
bbb=["6wjk.pdb",  "6x5d.pdb",  "6xah.pdb",  "7b4z.pdb",  "7b71.pdb",  "7b72.pdb",  "7bfs.pdb",  "7cuk.pdb",  "7jlh.pdb",  "7kci.pdb"]
ccc=["4fs6.pdb",  "6a1o.pdb",  "6a1q.pdb",  "6aqv.pdb",  "6aqx.pdb",  "6aqt.pdb",  "6aqw.pdb",  "6bst.pdb",  "7atg.pdb",  "7jy2.pdb"]
A=[]
B=[]
Z=[]

for i in aaa:
    file_path="./A/"+i
    fp=open(file_path,"r")
    arr=[-1]*1000
    brr=[-1]*1000
    crr=[-1]*1000
    drr=[-1]*1000

    def cal_angle(a,b,c,d,i):
        b1=[a[0]-b[0],a[1]-b[1],a[2]-b[2]]
        b2=[c[0]-b[0],c[1]-b[1],c[2]-b[2]]
        b3=[d[0]-b[0],d[1]-b[1],d[2]-b[2]]
        b1=b1/np.linalg.norm(b1)
        b2=b2/np.linalg.norm(b2)
        b3=b3/np.linalg.norm(b3)
        n1=np.cross(b1,b2)
        n2=np.cross(b2,b3)
        m1=np.cross(n1,b2)
        x=np.dot(n1,n2)
        y=np.dot(m1,n2)
        angle=math.pi-np.arctan2(y,x)
        deg=(math.degrees(angle))
        A.append(deg)

    for line in fp:
        ll=line.strip()
        ll=ll.split()
        if(ll[0]=='MODEL'):
            if(ll[1]!='1'):
                # print(">> # Error: Encountered multplie models using details form model 1 only")
                break
        if(ll[0]=='ATOM'):
            ll[5]=int(ll[5])
            ll[6]=float(ll[6])
            ll[7]=float(ll[7])
            ll[8]=float(ll[8])
            if(ll[2]=="C5'"):
                arr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C4'"):
                brr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C3'"):
                crr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="O3'"):
                drr[ll[5]]=[ll[6],ll[7],ll[8]]

    for i in range(len(arr)):
        if(arr[i]!=-1 and brr[i]!=-1 and crr[i]!=-1 and drr[i]!=-1):
            cal_angle(arr[i],brr[i],crr[i],drr[i],i)


for i in bbb:
    file_path="./B/"+i
    fp=open(file_path,"r")
    arr=[-1]*1000
    brr=[-1]*1000
    crr=[-1]*1000
    drr=[-1]*1000

    def cal_angle(a,b,c,d,i):
        b1=[a[0]-b[0],a[1]-b[1],a[2]-b[2]]
        b2=[c[0]-b[0],c[1]-b[1],c[2]-b[2]]
        b3=[d[0]-b[0],d[1]-b[1],d[2]-b[2]]
        b1=b1/np.linalg.norm(b1)
        b2=b2/np.linalg.norm(b2)
        b3=b3/np.linalg.norm(b3)
        n1=np.cross(b1,b2)
        n2=np.cross(b2,b3)
        m1=np.cross(n1,b2)
        x=np.dot(n1,n2)
        y=np.dot(m1,n2)
        angle=math.pi-np.arctan2(y,x)
        deg=(math.degrees(angle))
        B.append(deg)

    for line in fp:
        ll=line.strip()
        ll=ll.split()
        if(ll[0]=='MODEL'):
            if(ll[1]!='1'):
                # print(">> # Error: Encountered multplie models using details form model 1 only")
                break
        if(ll[0]=='ATOM'):
            ll[5]=int(ll[5])
            ll[6]=float(ll[6])
            ll[7]=float(ll[7])
            ll[8]=float(ll[8])
            if(ll[2]=="C5'"):
                arr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C4'"):
                brr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C3'"):
                crr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="O3'"):
                drr[ll[5]]=[ll[6],ll[7],ll[8]]

    for i in range(len(arr)):
        if(arr[i]!=-1 and brr[i]!=-1 and crr[i]!=-1 and drr[i]!=-1):
            cal_angle(arr[i],brr[i],crr[i],drr[i],i)





for i in ccc:
    file_path="./Z/"+i
    fp=open(file_path,"r")
    arr=[-1]*1000
    brr=[-1]*1000
    crr=[-1]*1000
    drr=[-1]*1000

    def cal_angle(a,b,c,d,i):
        b1=[a[0]-b[0],a[1]-b[1],a[2]-b[2]]
        b2=[c[0]-b[0],c[1]-b[1],c[2]-b[2]]
        b3=[d[0]-b[0],d[1]-b[1],d[2]-b[2]]
        b1=b1/np.linalg.norm(b1)
        b2=b2/np.linalg.norm(b2)
        b3=b3/np.linalg.norm(b3)
        n1=np.cross(b1,b2)
        n2=np.cross(b2,b3)
        m1=np.cross(n1,b2)
        x=np.dot(n1,n2)
        y=np.dot(m1,n2)
        angle=math.pi-np.arctan2(y,x)
        deg=(math.degrees(angle))
        Z.append(deg)

    for line in fp:
        ll=line.strip()
        ll=ll.split()
        if(ll[0]=='MODEL'):
            if(ll[1]!='1'):
                # print(">> # Error: Encountered multplie models using details form model 1 only")
                break
        if(ll[0]=='ATOM' or ll[0]=='HETATM'):
            kk=0
            if(ll[5].isnumeric()==False):
                kk=1
            ll[5]=int(ll[5+kk])
            ll[6]=float(ll[6+kk])
            ll[7]=float(ll[7+kk])
            ll[8]=float(ll[8+kk])
            if(ll[2]=="C5'"):
                arr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C4'"):
                brr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="C3'"):
                crr[ll[5]]=[ll[6],ll[7],ll[8]]
            if(ll[2]=="O3'"):
                drr[ll[5]]=[ll[6],ll[7],ll[8]]

    for i in range(len(arr)):
        if(arr[i]!=-1 and brr[i]!=-1 and crr[i]!=-1 and drr[i]!=-1):
            cal_angle(arr[i],brr[i],crr[i],drr[i],i)




plt.plot(A,label="A",color="red")
plt.plot(B,label="B",color="green")
plt.plot(Z,label="Z",color="blue")
plt.legend(["A","B","Z"])
plt.title("DNA")
plt.xlabel("Residue Number")
plt.ylabel("Angle")
plt.show()