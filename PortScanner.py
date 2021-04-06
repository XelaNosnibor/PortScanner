import socket
import sys
import os
from datetime import datetime

# Provide target
targetInput = input("Enter a remote host to scan: ")

# Provide lower port value to start at
portLowerValue = int(input("Enter first port in range to scan: "))

# Provide upper port value to finsih at
portUpperValue = int(input("Enter last port in range to scan: "))

target = socket.gethostbyname(targetInput)

timeBefore = datetime.now()

# Print banner
print("-" * 50)
print("Please wait, scanning remote host: " + target)
print("-" * 50)
try:
    for port in range(portLowerValue, portUpperValue):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Trying port: ", port)
        sock.settimeout(0.2)
        result = sock.connect_ex((target, port))
        if result == 0:
            ScannerLog = open('scanner.log', 'w')
            #print("Port {}: Open".format(port))
            ScannerLog.write("Port {}: Open".format(port),)
            ScannerLog.write("\n")
        sock.close()

except KeyboardInterrupt:
    print ("Scan aborted")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checks time again and calculates the difference of time to see how long it took to run the script
timeAfter = datetime.now()
timeTaken =  str(timeAfter - timeBefore)

# Printing the information to screen and to Scannerlog
print('Scanning Completed in: ', timeTaken)
print('\n')
ScannerLog.write('Scanning Completed in: ' + timeTaken)
ScannerLog.close()

# Printer banner
print("-" * 30)
print('Results of Port Scan')
print("-" * 30)

# Print contents of Scannerlog
ScannerLog = open('scanner.log', 'r')
contents = ScannerLog.read()
print (contents)
ScannerLog.close()