# importing library
import serial.tools.list_ports
import requests

Ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in Ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select port: COM")
print(val)

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portvar = "COM" + str(val)
        print(portList[x])


serialInst.baudrate = 9600
serialInst.port = portvar
serialInst.open()

packet = "0.0"
while True:
    if serialInst.in_waiting:  # data in the buffer

        # decode to convert in unicode and rstrip is to delete new line for for decode
        temp = packet
        packet = serialInst.readline().decode("utf").rstrip('\n')

        print(packet, temp)
        print(type(packet), type(temp))
        if temp != packet:
            URL = 'https://egarbage.herokuapp.com/admin'
            data = float(packet)
            client = requests.session()

            # Retrieve the CSRF token first
            client.get(URL)  # sets cookie
            if 'csrftoken' in client.cookies:
                csrftoken = client.cookies['csrftoken']
            post_url = 'https://egarbage.herokuapp.com/addweight/'+str(data)
            token = dict(csrfmiddlewaretoken=csrftoken)
            r = client.post(post_url, data=token,
                            headers=dict(Referer=post_url))

            
