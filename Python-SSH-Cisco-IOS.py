# Python SSH test using Paramiko.
# Configuring Cisco WS-C3750V2-48PS.
# Credit to David Bombal for the Paramiko configuration.

import paramiko
import time

ip_address = "10.10.10.10"
username = "MyUser"
password = "MyPass"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("interface Fa1/0/24\n")
remote_connection.send("description Link to LabSW5\n")
remote_connection.send("end\n")

for n in range (1,5):
    # show interfaces Fa1/0/1 | include load
    remote_connection.send("show interfaces Fa1/0/" + str(n) + " | include load\n")
    time.sleep(0.5)

# remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
