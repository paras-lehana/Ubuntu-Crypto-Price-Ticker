all:
	python3 app/main.py &

install:
	sudo apt-get install python3-gi python3-requests python3-yaml python3-notify2 python3-pip
	sudo pip3 install pygame
	sudo chmod u+x app/main.py
