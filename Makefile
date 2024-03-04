install:
	sudo apt update && sudo apt install screen lsof nano ffmpeg && \

	python -m venv .venv && \
	source .venv/bin/activate && \
	pip install pyworld && \
	pip install -r requirements.txt