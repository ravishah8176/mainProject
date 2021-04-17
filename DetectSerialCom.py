#importing library
import serial.tools.list_ports

Ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in Ports:
    portList.append(str(onePort))
    print(str(onePort))
