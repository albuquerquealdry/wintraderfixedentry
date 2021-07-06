import json
import os

def readFile(fileName):
    with open(r'C:\\Users\\Aldry Davyson\\Documents\\jsons\\'+ fileName) as f:
        order=json.load(f)
        return(order)
        
def deleteFile(fileName):
    os.remove('C:\\Users\\Aldry Davyson\\Documents\\jsons\\'+ fileName)