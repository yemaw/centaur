import serial
import time

microbit = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def sendCommand(key, value = ''):
	microbit.write(key+' '+str(value)+"\n")
	time.sleep(0.01)
	
sendCommand('M1', 255)
sendCommand('M2', 255)
sendCommand('M3', 255)
sendCommand('M4', 255)
time.sleep(3)
sendCommand('M1', -255)
sendCommand('M2', -255)
sendCommand('M3', -255)
sendCommand('M4', -255)
time.sleep(3)
sendCommand('MOTORS_STOP')

'''microbit.write("motors 90 150 150 250 \n")
time.sleep(3)
microbit.write("motors 0 0 0 -150 \n")
time.sleep(3)
microbit.write("motors 0 0 0 0 \n")'''
microbit.close()



