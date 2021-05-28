.PHONY: mouse

all: mouse

run:
	python3 main.py

mouse:
	cd computervisionzone 
	python3.8 ./computervisionzone/virtual_mouse.py