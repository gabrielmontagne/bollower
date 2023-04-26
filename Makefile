NAME := bollower
VERSION := 0.0.1
AUTHOR := Gabriel Montagné Láscaris-Comneno
AUTHOR_EMAIL := gabriel@tibas.london
YEAR := $(shell date +%Y)

init:
	pip3 install -r requirements.txt

test:
	nosetests
