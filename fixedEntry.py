#IMPORT FROM PYTHON
import json
import sys
import logging
from datetime import datetime,date
import string
import random
import time
#IMPORT FROM IQOPTIONAPI
from iqoptionapi.stable_api import IQ_Option, IQOptionAPI
#IMPORT FROM PROJECT
import readJson
import websocketsend
import teste

#READ AND DESTROY FILES JSON
fileJson = readJson.readFile(sys.argv[1])
readJson.deleteFile(sys.argv[1])

#CONNECTION AND VALIDATION THE IQOPTION
logging.disable(level=(logging.DEBUG))
Iq= IQ_Option(fileJson['user']['login'],fileJson['user']['password'])
Iq.connect()

#SELECTION ACOUNT TYPE REAL/PRACTICE
Iq.change_balance(fileJson['mode'])

#ORDER SHIPPING
check,id =Iq.buy(fileJson['order']['value'],fileJson['order']['pair'] ,fileJson['order']['direct'], fileJson['order']['duration'])
dataTimeNow = datetime.now().strftime('%H:%M:%S')
orderID = fileJson['order']['idorder']

#CHECK RESULT
result= Iq.check_win_v3(id)
result_value = float(result[1])

#RESULTS VERIFICATION LOOP 
if result_value == result_value > 0:
    stop = "Win"
    balance =result
    hour = dataTimeNow
    id_order = fileJson['order']['idorder']
    
else:
    stop ="Loss"
    balance =result
    hour =dataTimeNow
    id_order = fileJson['order']['idorder']

#GENERATION OF TXT FLE FOR STRING DAILY ORDERS 
date= date.today()
year= date.year
month = date.month
day= date.day
nameFileDate= "{}{}{}".format(year,month,day)

generalExtract= "\n {};{};{};{}".format(stop,balance[1],hour,fileJson['order']['idorder'])
arquivo = open(nameFileDate+"_codrobot.txt", 'a')
arquivo.write(str(generalExtract))
arquivo.close()

#REQUEST TO SEND INFORMATION TO WEBSOCKET 
dataRequest= {
	"date_to_orders":str(date),
	"hour":str(hour),
	"balance":float(balance[1]),
	"codRobot":str(fileJson['order']['idorder']),
	"pair":str(fileJson['order']['pair']),
	"duration":float(fileJson['order']['duration']),
	"value":float(fileJson['order']['value']),
	"status":str(stop),
	"direction":str(fileJson['order']['direct'])
}
websocketsend.sendInformation(dataRequest)