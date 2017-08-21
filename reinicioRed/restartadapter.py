import os
import configparser
import time


Config = configparser.ConfigParser()
Config.read("config")

interface = Config.get("PARAMS",'interfaceName')
deshabilitar = Config.get("COMANDS",'deshabilitar').replace('interfaceName', interface)
habilitar = Config.get("COMANDS",'habilitar').replace('interfaceName', interface)

ip1 = Config.get("TEST",'ip1')
ip2 = Config.get("TEST",'ip2')
#ip3 = Config.get("TEST",'ip3')

temp1 = Config.get("TEMP",'temp1')
temp2 = Config.get("TEMP",'temp2')
#temp3 = Config.get("TEMP",'temp3')

prueba1 = Config.get("TEST",'prueba1').replace('ip1', ip1).replace('temp1', temp1)
prueba2 = Config.get("TEST",'prueba2').replace('ip2', ip2).replace('temp2', temp2)
#prueba3 = Config.get("TEST",'prueba3').replace('ip3', ip3).replace('temp3', temp3)

try:
	comando1 = os.system(prueba1)
	result1 = Config.get("RESULTS",'r1')
	result2 = Config.get("RESULTS",'r2')
	with open(temp1) as f:
		read_data = f.read()

	if read_data.count(result1) >= 3 or read_data.count(result2)>= 3:
		comando2 = os.system(prueba2)
		with open(temp2) as f:
			read_data = f.read()
		if read_data.count(result1) >= 3 or read_data.count(result2)>= 3:
			os.system(deshabilitar)
			print("Reiniciando interfaz de red %s", interface)
			time.sleep(Config.getint("PARAMS",'sleeptime'))
			os.system(habilitar)
			print("interfaz de red %s reiniciada", interface)
			os.remove(temp2)
	os.remove(temp1)
#print(read_data.count(result1))
except Exception as e:
	print("Ejecucion Con Errores")
	print(e)
finally:
	print("Ejecucion Completada")


#comando2 = os.system(prueba2)
#comando3 = os.system(prueba3)

#print(comando2)
#print(comando3)
"""os.system(deshabilitar)
print("Reiniciando interfaz de red %s", interface)
time.sleep(Config.getint("PARAMS",'sleeptime'))
os.system(habilitar)
print("interfaz de red %s reiniciada", interface)"""