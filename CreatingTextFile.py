# importing library
import serial.tools.list_ports

Ports = serial.tools.list_ports.comports()

# list of no of ports
portList = []

# Adding all the available ports to list
for onePort in Ports:
    portList.append(str(onePort))
    print(str(onePort))

# Getting input from the user to connect to the port
val = input("Select port: COM")
print(val)

# checking whether the port is available or not
for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portvar = "COM" + str(val)
        print(portList[x])

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = portvar
serialInst.open()

temp = 0.0
while True:
    if serialInst.in_waiting:  # data in the buffer

        # decode to convert in unicode and rstrip is to delete new line for for decode
        packet = serialInst.readline().decode("utf").rstrip('\n')
        temp = packet
        if temp == packet:
            with open('analogData.txt', 'w') as txt_file:
                txt_file = txt_file.write(packet)
        print(packet)
