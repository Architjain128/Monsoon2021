import numpy as np

# delta dihaderal angle is between C5'-C4'-C3'-O3'
DNA_PDB="7SB9"

# ATOM    167  C5'  DA A   9     -20.689 -11.841  -3.237  1.00 13.77           C  
# ATOM    168  C4'  DA A   9     -21.483 -11.025  -2.247  1.00 10.99           C  
# ATOM    170  C3'  DA A   9     -22.869 -10.619  -2.724  1.00 18.11           C  
# ATOM    171  O3'  DA A   9     -23.810 -11.661  -2.512  1.00 11.43           O  


a=[-20.689 ,-11.841 , -3.237 ]
b=[ -21.483 ,-11.025 , -2.247]
c=[-22.869, -10.619, -2.724]
d=[-23.810 ,-11.661 , -2.512]


# Given the coordinates of the four points, obtain the vectors b1, b2, and b3 by vector subtraction.
b1=[a[0]-b[0],a[1]-b[1],a[2]-b[2]]
b2=[c[0]-b[0],c[1]-b[1],c[2]-b[2]]
b3=[d[0]-b[0],d[1]-b[1],d[2]-b[2]]
# Normailzation of vectors
b1=b1/np.linalg.norm(b1)
b2=b2/np.linalg.norm(b2)
b3=b3/np.linalg.norm(b3)
# Compute n1=⟨b1×b2⟩ and n2=⟨b2×b3⟩, the normal vectors to the planes containing b1 and b2, and b2 and b3 respectively. The angle we seek is the same as the angle between n1 and n2.
n1=np.cross(b1,b2)
n2=np.cross(b2,b3)
# The three vectors n1, ⟨b2⟩, and m1:=n1×⟨b2⟩ form an orthonormal frame. Compute the coordinates of n2 in this frame: x=n1⋅n2 and y=m1⋅n2.
m1=np.cross(n1,b2)
x=np.dot(n1,n2)
y=np.dot(m1,n2)
# The dihedral angle, with the correct sign, is atan2(y,x).
angle=np.arctan2(y,x)
print(">> angle in DNA",DNA_PDB,angle)


RNA_PDB="7msv"

# ATOM     35  C5'  DA X   2      35.678  22.744  18.125  1.00  0.00           C  
# ATOM     36  C4'  DA X   2      35.163  24.164  18.445  1.00  0.00           C  
# ATOM     38  C3'  DA X   2      36.259  25.148  18.893  1.00  0.00           C  
# ATOM     39  O3'  DA X   2      36.095  26.454  18.310  1.00  0.00           O  


a=[35.678,  22.744,  18.125 ]
b=[35.163,  24.164,  18.445]
c=[36.259,  25.148,  18.893]
d=[36.095,  26.454,  18.310]


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
angle=np.arctan2(y,x)
print(">> angle in RNA",RNA_PDB,angle)
print(">> answer is in form of arctan2 not in degrees")