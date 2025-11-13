# Datenstructure 
from math_utils import Angle3D
from math_utils import OrthoPro
from math_utils import CrossP
from helper import LoadData
from math_utils import Norm
from math_utils import RotateThroughAxis

Knot1 = {
    "D0":{
    "Profiltype" : "20x20",
    "Vector" : [-1,1,0]
    },
    "D1":{
    "Profiltype" : "20x20",
    "Vector" : [0,1,0]
    },
     "D2":{
    "Profiltype" : "20x20",
    "Vector" : [0,-1,0]
    },
     "D3":{
    "Profiltype" : "20x20",
    "Vector" : [0,-1,1]
    }
}

V1 = [1,2,3]
V2 = [2,3,4]
Axis = [2,5,1]
alpha = 10
V1p = RotateThroughAxis(V1,Axis,alpha)
V2p = RotateThroughAxis(V2,Axis,alpha)


# This Functions gets the Axis and Angle with which Matching Families of Knots can be Transformed in to each other
def AlineRotaion(A1,B1,A2,B2): # ALL = [X,Y,Z]
  A1,B1,A2,B2 = Norm(A1),Norm(B1),Norm(A2),Norm(B2) #Normalizes all the Input Vectors
  def TestMatch(A1,B1,A2,B2,tol): #tol = toleranz
    a = Angle3D(A1,A2,1)
    b = Angle3D(B1,B2,1)
    c = a - b
    print(c)
    if c < tol:
      print("Match")
      return True
    else:
      print("Not a Match")
      return False
  if not TestMatch(A1,B1,A2,B2,10e-7):
    return
  N1 = CrossP(A1,B1)
  N2 = CrossP(A2,B2)
  

AlineRotaion(V1,V1p,V2,V2p)

# Could probably be substetudeded with the combinations from itertools
def PearElementMaker(N): # N = Elements to generate unique pears out of
  i = int(0)
  n = int(0)
  A = []
  N = N - 1 # Ausgleich für Zählen bei null Beginnen
  while i < N:
    n = i
    while n < N:
      n=n+1
      # b = str(i)+"x"+str(n)
      b = [i,n]
      A.append(b)
    i=i+1
  return A

def GetKeys(A,B="A"): # A = Dictonary , B = Starting letter of Key
  k = list(A.keys())
  i = 0
  K = []
  while i < len(k):
    # print(k[i])
    if k[i].startswith(B) :
      K.append(k[i])
    i = i + 1
  # print(K)
  return(K)

def GenrateAngles(A,B="D",C=0): # A = Dictonary , C =  0 => radians 1 => Degrees 
  k = GetKeys(A,B)
  ko = PearElementMaker(len(k))
  i = int(0)
  Angles = []
  while len(ko) > i:
    a1 = B + str(ko[i][0])
    b1 = B + str(ko[i][1])
    a = A[a1]["Vector"]
    b = A[b1]["Vector"]
    alpha = Angle3D(a,b,C)
    # print(alpha)
    Angles.append(alpha)
    i = i + 1
  return Angles # Unsorted list of Relavie Angels

def AssoiativeAngles(A,B="D",C=0):  # A = Dictonary ,B = Key Starting Letter, C =  0 => radians 1 => Degrees 
  AssoiativeAngles = {}


# AssoiativeAngles(A=Knot1,B="D",)

def test(A):
  pass
  

# test(Knot1)