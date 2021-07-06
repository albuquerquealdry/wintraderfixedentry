from iqoptionapi.stable_api import IQ_Option
import time, json, logging, configparser
import websocketsend




logging.disable(level=(logging.DEBUG))
order={'pair':'','direction':'','duration':0.0}
API = IQ_Option('randane@gmail.com', 'rafa321321')
API.connect()#connect to iqoption


while True:
    #please open website iqoption and buy some binary option
    if API.get_option_open_by_other_pc()!={}:
        break
    time.sleep(1)
print("Get option from other Pc and same account")
status = API.get_option_open_by_other_pc()
mylist = list(status.values())

n1=float((mylist[0]['msg']['expired'] - mylist[0]['msg']['created']) / 60)
t=1
order['pair'] = mylist[0]['msg']['active']
order['direction'] = mylist[0]['msg']['dir']
order['duration'] = int(n1 * 10**t)/10**t
websocketsend.sendOrder(order)
print(order)


