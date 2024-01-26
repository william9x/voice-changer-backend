install:
	apt-get update
	#apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
	apt-get install -y build-essential autoconf libtool pkg-config idle-python2.7 libqtgui4 libqtcore4 libgle3 python-dev
	apt-get install -y python3-pip python3.10-venv python-is-python3

	python -m venv .venv
	source .venv/bin/activate
	pip install pyworld
	pip install -r requirements.txt