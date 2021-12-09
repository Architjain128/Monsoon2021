import math
import numpy as np
import matplotlib.pyplot as plt

rna=["7d12.pdb",  "7eaf.pdb",  "7jrr.pdb",  "7jrt.pdb",  "7kuk.pdb",  "7kun.pdb",  "7kup.pdb",  "7lne.pdb",  "7lyj.pdb",  "7oaw.pdb",  "7dd4.pdb",  "7eag.pdb",  "7jrs.pdb",  "7k4l.pdb",  "7kum.pdb",  "7kuo.pdb",  "7l0z.pdb",  "7lyf.pdb",  "7mky.pdb",  "7oax.pdb"]

RNA=[]

for i in rna:
    
    file_path="./rna/"+i
    print(file_path)
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
        RNA.append(deg)

    for line in fp:
        ll=line.strip()
        ll=ll.split()
        if(ll[0]=='MODEL'):
            if(ll[1]!='1'):
                # print(">> # Error: Encountered multplie models using details form model 1 only")
                break
        if(ll[0]=='TER'):
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

plt.plot(RNA)
plt.title("RNA")
plt.xlabel("Residue Number")
plt.ylabel("Angle")
plt.show()