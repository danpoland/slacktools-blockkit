# Makefile
# @author dan@crispy.dev

.PHONY: build

default: build

build:
	python setup.py sdist bdist_wheel

publish::
	twine upload dist/*
