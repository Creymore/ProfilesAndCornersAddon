import math
import random
import json


#Helper funktion to generate Test data could be in a diffrent file
def GenerateData(A=1,B=4,C = "20x20",D = "DummData.json" ): # A = Number of Corners , B = Direktions in Corners 
  def GenerateVectors(A=3):
    V = []
    for i in range(A):
      V.append(random.randrange(-100,100,1))
    return V
  jcorners = {}
  for n in range(A):
    corner = {}
    for i in range(B):
        Vec = GenerateVectors()
        Direction = {
          "Profilerype" : C ,
          "Vector" : Vec
        }
        corner.update({f"D{i}":Direction})
       # print(Direction)
    # print(corner)
    jcorners.update({f"corner{n}" : corner})
  Data = json.dumps(jcorners, sort_keys=False, indent=2)
  with open(D, "w") as f:
    f.write(Data)

def LoadData(A="DummData.json",B=0): # A= file to load from, B = corner numer
  with open(A,"r") as f:
    data = json.load(f)
    data = data[f"corner{B}"]
  return data

