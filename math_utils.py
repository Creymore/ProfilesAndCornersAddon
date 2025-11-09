import math

T1=[1,2,3]
T2=[4,5,6]

#Could use the General defintion with the sum
def DotP(A,B): # A =[a1,a2,a3] B=[b1,b2,b3]
    dot = A[0]*B[0]+A[1]*B[1]+A[2]*B[2]
    return dot

# print(DotP(T1,T2))

def CrossP(A,B): # A =[a1,a2,a3] B=[b1,b2,b3]
    cross = [ 
            A[1]*B[2] - A[2]*B[1],
            A[2]*B[0] - A[0]*B[2],
            A[0]*B[1] - A[1]*B[0]
            ]
    return cross

# print(CrossP(T1,T2))

def Scale(A,B): # A = [X,Y,Z] B = n
    scaled = [
            A[0]*B,
            A[1]*B,
            A[2]*B
            ]
    return scaled

def Add(A,B): # A = [a1,a2,a3] B = [b1,b2,b3]
    added = [
        A[0]+B[0],
        A[1]+B[1],
        A[2]+B[2]
    ]
    return added

def OrthoPro(P,N,R=[0,0,0]): #P = [X,Y,Z] , Point to Projekt N = [n1,n2,n3] , Normal of Plane R=[x,y,z] ,
    a = DotP(Add(P,Scale(R,-1)),N)
    b = DotP(N,N)
    c = Scale(N,a/b)
    Projected = Add(P,Scale(c,-1))
    return Projected

# print(OrthoPro(T1,T2))

def Vectorlenth(A): # A = [x,y,z]
  a = math.sqrt(pow(A[0],2)+pow(A[1],2)+pow(A[2],2))
  return a

def Angle3D(A,B,C=0): # A = [x,y,z] , B = [x,y,z] , c = 0 => radians 1 => Degrees
  s = DotP(A,B)
  a = math.acos(s/(Vectorlenth(A)*Vectorlenth(B)))
  if C != 0:
    a = math.degrees(a)
  return a

def RotateThroughAxis(P,K,alpha): # P = [X,Y,Z] , Point K = [X,Y,Z] , alpha = Angle
   a = Scale(P,math.cos(alpha))
   b = Scale(CrossP(K,P),math.sin(alpha))
   c = Scale(K,DotP(K,P)*(1-math.cos(alpha)))
   d = Add(a,b)
   roteted = Add(d,c)
   return roteted