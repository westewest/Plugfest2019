Plugfest
Demonstration of IEEE P21451-1-6 for 2019 IEEE IES IECON PlugFest
====

In this plugfest2019, the main concept of this demonstration is Use 1451-1-6 with MQTTv5 over Edge AI and IoT.

===

IEEE P21451-1-6 Working Group (WG) Development Meeting on STANDARD FOR A SMART TRANSDUCER INTERFACE FOR SENSORS, ACTUATORS AND DEVICES – MESSAGE QUEUE TELEMETRY TRANSPORT (MQTT)FOR NETWORKED DEVICE COMMUNICATION. 

IEEE P21451-1-6 is included in IEEE 1451 Standards family. An event, IEEE 1451 Standards Plugfest, is achieved at INTEROP 1451, IECON '18. The objectives are as follows.

- Provide the IEEE 1451/21451 standards community with verification and validation platforms for the standards so the community can test the development of their applications to these benchmarks, ensuring compliance and interoperability to their systems.
- The standards and platforms will provide compliance and interoperability to the IoT applications and its industrial components (IIoT)
- Encourage industry partners to make sure of the verification and validation platforms for IEEE Standards compliance in the industry context.
- Verification and developing platforms are being implemented following several different approaches, allowing coverage of specific sensor transducer applications conforming to the IEEE P1451 standards.
- The goal of these platforms is to support users with “turn-key” approaches for their applications, by providing relatively easy initial start-up processes, allowing easy installation and configuration.

This demonstration program shows the typical example of IEEE P21451-1-6.

## Presentation Material

This document focuses on installation.
To know about this design model, please use the following URL.
https://gitpitch.com/westewest/Plugfest2019

The last Plugfest2018 demonstration environment is explained in the following URL.
https://gitpitch.com/westlab/PlugFest/

## Requirements

- Required libraries and python packages must be installed. Follow the description of Install section.
- You may use BLE-based Smart IoT Sensor Module manufactured by ALPS ELEC Co.Ltd. If you don’t have the module, you can use a pseudo sensor mode.
- TIM and NCAP emulation are run on Intel-based conventional PC. Native Linux environment is recommended.
- For the minimum environment, one conventional PCs is enough if it has enough performance. As a recommendation, four conventional PC should be prepared; one for TIM/NCAP emulation to connect IoT sensors (hostname:iot), one for Face Detection using Deep Learning (hostname:ai), one for MQTT v5 broker (hostname:srv), and one for service client as a node-red host are required.  All these services can be executed on one server.
- MQTT v5 broker is required to use new features of MQTT v5. For IEEE P21451-1-6, MQTT v5 will be mandatory to implement all needed functions for IEEE1451.
- (IMPORTANT) There are two versions of GitHub design: westlab/Plugfest2019 and  westewest/Plugfest2019. At this moment westewest is the correct model. Please replace all the source URL of git command line.

## Installation

- Preparation
When installing Ubuntu first, it is convenient to install the following models.
```
	# apt update
	# apt upgrade
	# apt install mailtools
	# apt install build-essential
	# apt install openssh-server
```

It is better to register all machines to /etc/hosts

```
	# vi /etc/hosts
```

add the following lines to the end of /etc/hosts file.

```
192.168.0.10    srv
192.168.0.20    ai
192.168.0.21    iot
```

### MQTT broker installation (srv)

#### Install Mosquitto MQTTv5 broker

- Install the newest mosquitto as MQTT v5 broker

Mosquitto is one of the most popular MQTT brokers, and it supports MQTTv5 now. 

Eclipse Mosquitto is an open-source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 5.0, 3.1.1 and 3.1. Mosquitto is lightweight and is suitable for use on all devices from low power single board computers to full servers.

https://mosquitto.org/

Download the newest mosquitto and install to the Linux machine.
```
	# apt install git
	# apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
	# apt upgrade
	# systemctl start mosquitto
	# systemctl enable mosquitto
```
The command line starts with # means it requires sudo environment to get root account.
The mosquitto server will be started and will be executed automatically when your system boots.

You may install mosquitto by using the following packages; however, the following installation installs Mosquitto v1.4 which does not support MQTTv5.

```
	# apt install mosquitto [Not Supported]
```

To confirm the installation and execution, do the following commands in different terminals.
Open two terminals.

1st terminal:
```
    # mosquitto_sub -d -t test
```

2nd terminal:
```
    # mosquitto_pub -d -t test -m hogehoge
```

You can see messages in the 1st terminal. Here, -d is the debug option. You can omit it. -t specifies topic, and -m specifies messages. To connect another MQTT broker host, use –h option.

#### Install Mosquitto MQTTv5 broker into Windows (Option)

You may also install MQTT server into Windows 10 machine.

Download the newest Mosquitto from the eclipse site.
https://mosquitto.org/download/

At this moment, mosquitto-1.6.6-install-windows-x64.exe is the newest design. 34bit build model is also available. It is compiled by using Visual Studio Community 2017)

You may also install the following libraries.

From [ http://slproweb.com/products/Win32OpenSSL.html ], download [ install Win32OpenSSL_Light-1_0_2k.exe ] and execute it.
Copy libeay32.dll and ssleay32.dll in C:¥OpenSSL-Win32¥bin of OpenSSL to C:\Program Files (x86)\mosquitto
Get pthreadVC2.dll from ftp://sources.redhat.com/pub/pthreads-win32/dll-latest/dll/x86/

And, copy it to C:\Program Files (x86)\mosquitto

If you want to execute Mosquitto Broker, it only can be executed as a Windows service.
Use the Services menu of Windows Management tool and enable it.

#### Install Docker-based MQTT broker

Docker is a light-weight virtual machine environment. This installation method can encapsulate mosquitto environment into virtual machine. If you are not familiar with using Docker, the normal installation given above is preferable.

- MQTT broker server on Docker

+ Installation of Docker

Install docker by following commands. This is just what you do. However, it takes time.

```
    # apt install curl
    # curl -sSL https://get.docker.com | sh
```

Otherwise, you can install docker from packages.

```
	# sudo apt install -y apt-transport-https ca-certificates \
		curl software-properties-common
```

Install GPG key of Docker.

```
	# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Set apt repository to stable.

```
	# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
		$(lsb_release -cs)    stable"
```

Install Docker-ce.

```
	# apt upgrade
	# apt install -y docker-ce
```

You may have some troubles when resolving DNS of get.docker.com or getting PGP keys. In this case, IP address and the canonical name of get.docker.com by using nslookup command, and directly write the address and name to /etc/hosts. You also add download.docker.com to the hosts file.

+ Docker installation test

As a test, execute hypriot image. This hypriot is a very nice site, which preparing many kinds of Docker images.

```
    # docker run -d -p 80:80 hypriot/rpi-busybox-httpd
```

This command executes httpd web server in a docker. Check a test site is open in your raspberry-pi by accessing a web browser in your network.

```
    # docker ps
    # docker stop [NAME] (This name will be changed at any time)
```

- Install Mosquitto on Docker

Then install docker image of mosquitto MQTT server

```
    # docker run -tip 1883:1883 -p 9001:9001 pascaldevink/rpi-mosquitto
```

If you execute mosquitto docker image by changing its configurations, do following commands.

```
    mkdir -p /srv/mqtt/config/
    mkdir -p /srv/mqtt/data/
    mkdir -p /srv/mqtt/log/
```

place your mosquitto.conf in /srv/mqtt/config/

NOTE: You have to change the permissions of the directories to allow the user to read/write to data and log and read from config directory For TESTING purposes you can use the following command

```
    # chmod -R 777 /srv/mqtt/*
    # docker run -ti -p 1883:1883 -p 9001:9001 \
		-v /srv/mqtt/config:/mqtt/config:ro \
		-v /srv/mqtt/log:/mqtt/log \
		-v /srv/mqtt/data/:/mqtt/data/ \
		--name mqtt pascaldevink/rpi-mosquitto
```

#### Windows 10 mosquitto clients (Option)

Check your config file

```
    C:\Program Files (x86)\mosquitto\mosquitto.conf
    >cd "C:\Program Files (x86)\mosquitto"
    >mosquito_sub –t test
```

In another window

```
    >cd "C:\Program Files (x86)\mosquitto"
    >mosquito_pub –t test –m hoge
```

It shows “hoge”.

You may change your Firewall configuration. Check system and security menu in control panel.
And change the mosuquitto.exe, mosquitt_pub.exe,mosquitto_sub.exe as public functions.

One important point. Windows mosquitto cannot send and receive UTF coded messages. This is a serious problem.

#### Paho mqtt client (Option)

Paho MQTT client is a popular MQTT client library for Python. However, it does not MQTTv5 at this moment. Please install gmqtt. This paho-mqtt, as well as gmqtt, is available for Python v3. Install the paho library.

```
    # pip3 install paho-mqtt
```

### NCAP/TIM emulator installation

#### Installation of Ubuntu 19.04
Install the newest Ubuntu.
After installation, make it updated.
```
# apt install git
# apt -y upgrade
# apt -y update
# apt -y dist-upgrade
```

All the installation model will be installed at /export/install

```
# mkdir -p /export/install && cd $_
```

Prepare installation models from GitHub.

```
# git clone https://github.com/westlab/Plugfest2019
```

Here, it will be better to reboot.

```
    # reboot
```

- Install gmqtt

# gmqtt is an early implementation of MQTTv5 client for python3.

```
# apt install python3-pip
# pop3 install pytest
# pip3 install uvloop
# pip3 install gmqtt
```

You can install pip for python2 if you want.



#### ALPS ELEC Smart IoT BLE Sensor Module

If you don’t have the module, you can skip this installation. In this case, you will use a dummy sensor, which generates random values. You can skip this installation if you use a dummy sensor. You can also use any sensors replacing the description abut ALPS sensor.

Blog of TomoSoft (as given below) explains how to install the ALPS module. This is a very simple way for us to connect sensors to Raspberry Pi via Bluetooth.
http://tomosoft.jp/design/?p=8104
http://www.hiramine.com/physicalcomputing/raspberrypi3/wlan_howto.html
These pages are written in Japanese. Use google translator. Simply, it is enough to follow the process below.

(Note) The code in the site has a bug in handling sign of values. Acceleration sensor value and geomagnetic sensor value are signed values. The original code handles these values as unsigned values. Our design does not have this bug.

- Set time

Fix the clock of your machine. ALPS IoT module requires correct time because it refers the clock of mother machine.

```
# systemctl stop ntp		#(If ntp is already installed, stop it)
# apt install ntpdate
# timedatectl set-timezone Asia/Tokyo 	#(select your timezone)
# ntpdate ntp.nict.jp		#(select your closest ntp server)
# apt install ntp
```

Edit ntp configuration file to add ntp server.


```
	# vi /etc/npt.conf
```

Optionally, to get the precise clock in Japan, edit the config file as follows. You have to edit according to your time zone and time server. As a default, Ubuntu Pool time server project is described and is useful in many cases.

```
#server 0.ubuntu.pool.ntp.org
#server 1.ubuntu.pool.ntp.org
#server 2.ubuntu.pool.ntp.org
#server 3.ubuntu.pool.ntp.org
server ntp.nict.jp
```

Execute ntp

```
	# systemctl start ntp
```

To confirm the status of time synchronization of ntp service, use the following command.

```
	# ntpq -p
```

- Install the required modules.

The alps modules required Bluetooth helper module and some part of bluepy sources.

Firstly, install blupy, which is a python interface to communicate via Bluetooth

```
    # apt-get install python3-pip libglib2.0-dev
    # apt-get install git build-essential
    # cd
    # pip3 install bluepy
    # pip3 install pybluez
```

+ we need some part of bluepy sources. Extract sources from git.
+ It is better to set a working directory. Here, we set /export as a working directory.

In the working directory, install bluepy.

```
    # mkdir -p /export/install
    # cd /export/install
    # git clone https://github.com/IanHarvey/bluepy.git
    # cd bluepy
```
Now you are in the directory of /export/install/bluepy
Update the blupy. It is preferable.

```
    # python3 setup.py build
    # python3 setup.py install
    # cd bluepy
    # ls btle.py 		#(check the existence of the file)
    # cd /export/install
```

+ download our design

Our all design is available in GitHub.

```
    # git clone https://github.com/westlab/Plugfest2019
    # cd /export/install/bluepy/bluepy
    # cp ../../Plugfest2019/P21451-1-6/alps/alps_sensor.py .
    # python3 alps_sensor.py
```

Check it does not report any errors, and it will be quiet.

Then, type Ctrl-C

```
    # ls 
```

Check btle.py btle.pyc and bluepy-helper. These files are important to communicate with the Bluetooth sensor module.

```
    # cd /export
    # ln -s install/Plugfest2019/P21451-1-6/alps .
    # cp install/bluepy/bluepy/{btle.py,bluepy-helper} alps
    # cd alps
    # python3 alps_sensor.py
```

Again, Check it does not report any errors, and just quiet. If it is Ok, then type Ctrl-C.

Edit the following line of the alps.py source file to fit your sensor module address. You can specify the sensor module address by using -m option.

```
    alps = AlpsSensor("28:A1:83:E1:59:48")
```

The address is printed on the surface of the sensor module. You can also check the address by using the following command.

```
    # hciconfig
```

Run the python script. You can add -h option to check the options of the script.

```
    # python3 alps_sensor.py
```

Then, you can get the sensor values. It takes about 10 seconds to get sensor data from when you run the script.

The program uses Hybrid Mode of sensor module and set all sensors ON.
The sampling rate of the acceleration sensor and the geomagnetic sensor is 100 mil seconds.
Others are 1 second.

#### Other Bluetooth sensors (Option and is not confirmed)

ALPS IoT module uses Bluetooth Low Power (BLE), and the operation code uses special method of bluepy. Generally, pybluez and gattlib are used to connect Bluetooth sensors.
There are many kinds of Bluetooth-based sensors such as TI SensorTag CC2650.

If you want to use it, you have to install BlueZ and GATT (Generic Attribute Profile). The following installation process is an example and was not checked in an Ubuntu environment.

```
	# apt install python-dev libbluetooth3-dev
	# pip3 install pybluez
	# apt install libglib2.0 libboost-python-dev libboost-thread-dev
	# pip3 install gattlib
```

If you failed in installing gattlib, you have to install it from the source repository.

```
    # cd /export/install
    # pip3 download gattlib
    # tar xvzf ./gattlib-0.20150805.tar.gz
    # cd gattlib-0.20150805/
    # sed -ie 's/boost_python-py34/boost_python-py35/' setup.py
    # pip3 install . (Do not miss the last period)
```

As sample codes, scan.py can search SensorTag.

```
	# python3 pybluez/examples/ble/scan.py
```

To get sensor data, refer the following sample code.

```
    # python3 pybluez/examples/ble/read_name.py
```

- Reload daemon process
Now reload the daemon processes.

```
    # systemctl daemon-reload
    # systemctl restart bluetooth
```

## Applications

### Node-RED

Elasticsearch+kibana works but is very heavy.

Dashing application is Ok but is just a “dashboard.”

Here, install Node-red as IoT application.

```
    # apt install –y nodejs
	# apt install npm
    # systemctl start nodered
	# npm install -g --unsafe-perm node-red node-red-admin
```

Open firewall for permitting the remote access to the node-red server.

```
	# ufw allow 1880
	# ufs reload
```

Execute node-red

```
	# node-red
```

Access to the following site.
http://localhost:1880
localhost is your installed machine name or IP address.

It has many functions to connect IoT services.
One important function for demonstration is drawing graphs.
In the installation above, dashboard will be automatically installed.
If it is not installed, see the last Plugfest2018 installation document to install it.

To use the dashboard, select the menu button (right-top) and select “setting,” “pallet,” and search node-red-dashboard. Then press install button on the node-red-dashboard tab. You may find many plugin applications for Node-RED.

You can access the dashboard panel by the following URL.
http://localhost:1880/ui

### To make node-red as a service

If you want to use node-red, you have to execute node-red firstly anytime by typing node-red to the command console.

If you want to execute node-red automatically when the system boots, pm2 service will help it.

Register the node-red service to pm2.

```
	# npm install -g pm2
	# pm2 start /usr/local/bin/node-red -- -v
	# pm2 save
```

register pm2 to systemd service. The following command executes systemctl enable pm2-root.

```
	# pm2 startup
```

If you want to see the logfile of node-red, do like this.

```
	# pm2 logs node-red
```

If you want to restart node-red, do like this.

```
	# pm2 restart node-red
```

If you want to install node, you can use pallet manager. If you want to add nodes from a command line, do like this.

```
	# cd ~/.node-red
	# npm install {path to the target node project}
	# pm2 restart node-red
```


### Authentication of Node-red (Option)

It does not have authorization as it’s original configuration.
It is better to install an authentication function for Node-RED.

```
    # npm i bcrypt
```

You have to implement an encoded password into the configuration file.
Use the following command to get the encoded password.

```
    # node -e "console.log(require('bcryptjs').hashSync(process.argv[1], 8));" PASSWORD
```

Type the code into setting.js

```
    # vi ~pi/node-red/settings.js
```

Edit the appropriate section of the file as follows.

```
adminAuth: {
    type: "credentials",
    users: [{
        username: "admin",
        password: "$2a$08$zZWtXTja0fB1pzD4sHCMyOCMYz2Z6dNbM6tl8sJogENOMcxWV9DN.",
        permissions: "*"
    }]
}
```

### Wind speed and direction sensor

This model is applicable to use SGLab wind speed and direction sensor.
NodeMCU was used to read data from the sensor. Use Arduino IDE to design NodeMCU. To install NodeMCU, you may install required libraries to design NodeMCU on Arduino IDE.

To depict the graphical image of the measured data,  use the python script in GL directory.

## Other topics

### Prevent Darkout

If you want to use the dashboard like KIOSK, which means to prevent the screen darkout, use the following command.

```
    $ xset s 0 0
    $ xset s noblank
    $ set s noexpose
    $ xset dpms 0 0 0
```

You may think these commands are automatically executed. Then, edit the following file.

```
    $ vi ~pi/.config/lxsession/LXDE-pi/autostart
```

Then, insert the following lines to the end of the file.

```
@xset s 0 0
@xset s noblank
@xset s noexpose
@xset dpms 0 0 0
```

The screen will not go to sleep.
