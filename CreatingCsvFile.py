# importing library
import datetime
import pytz
import csv
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

header = 0
while True:
    if serialInst.in_waiting:  # data in the buffer

        # decode to convert in unicode and rstrip is to delete new line for for decode
        packet = serialInst.readline().decode("utf").rstrip('\n')
        # time
        dt_now = datetime.datetime.now()
        dt_tz_now = dt_now.astimezone(pytz.timezone('Asia/Calcutta'))

        with open('analogData.csv', 'a+', newline='') as csv_file:
            fieldnames = ['Reading']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames,)

            if header == 0:
                csv_writer.writeheader()
                header = 1

            # reading no of lines
            csv_writer.writerow({'Reading': packet})
        print(packet)