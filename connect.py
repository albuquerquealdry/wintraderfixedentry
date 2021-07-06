from iqoptionapi.stable_api import IQ_Option
import time, json, logging, configparser
from datetime import datetime, date, timedelta
from dateutil import tz

logging.disable(level=(logging.DEBUG))

API = IQ_Option('randane@gmail.com', 'rafa321321')
API.connect()
API.change_balance('PRACTICE') # PRACTICE / REAL


while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		
		API.connect()
	else:
		print('\n\nConectado com sucesso')
		break