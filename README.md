Script checks LibreNMS for IP-adresses in defined IP-networks and lists which switchports have connected devices in IP-subnet.


Define your LibreNMS API-token and which IP-networks to be checked in libreapi.py. If you want to check more networks, just add another function.

Run guestvlanports.py to run script.

Example output:

-----
Checking sw-distacc.
Switch                         Interface                      Description                   
switch1                        GigabitEthernet3/0/18          Interface description
switch2                        GigabitEthernet3/0/36          Interface description
switch3                        GigabitEthernet2/0/36          Interface description
switch4                        GigabitEthernet1/0/36          Interface description
switch5                        GigabitEthernet1/0/3           Interface description               
