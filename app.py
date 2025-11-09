# Datenstructure 
import math
import random
import json

corner1 = {
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


# GenerateData(A=1000)

def LoadData(A="DummData.json",B=0): # A= file to load from, B = corner numer
  with open(A,"r") as f:
    data = json.load(f)
    data = data[f"corner{B}"]
  return data

# print(LoadData(B=1))

def Vectorlenth(A): # A = [x,y,z]
  a = math.sqrt(pow(A[0],2)+pow(A[1],2)+pow(A[2],2))
  return a

def Angle3D(A,B,C=0): # A = [x,y,z] , B = [x,y,z] , c = 0 => radians 1 => Degrees
  s = A[0]*B[0]+A[1]*B[1]+A[2]*B[2]
  a = math.acos(s/(Vectorlenth(A)*Vectorlenth(B)))
  if C != 0:
    a = math.degrees(a)
  return a

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

def GenrateAngles(A,B="D",C=0): # = Dictonary , C =  0 => radians 1 => Degrees 
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


AssoiativeAngles(A=corner1,B="D",)

def test(A):
  pass
  

test(corner1)