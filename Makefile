SHELL := /bin/bash

all: build

clean:
	rm -rf *.egg-info/
	rm -rf dist/
	rm -rf build/
	rm -rf test_env/

validate:
	pylint *.py

test:
	python3 -m unittest tests/test.py

build:
	python3 setup.py sdist bdist_wheel

install:
	python3 -m venv test_env/
	source test_env/bin/activate
	pip3 install bitcoinaddress

deploy:
	clean
	validate
	test
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

