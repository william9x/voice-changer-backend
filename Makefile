install:
	apt update && sudo apt upgrade
	apt-get install -y build-essential autoconf libtool pkg-config
	apt-get install -y python3-pip python3.10-venv python-is-python3

	python -m venv .venv
	source .venv/bin/activate
	pip install pyworld
	pip install -r requirements.txt