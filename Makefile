.PHONY: all develop install clean test

all:
	python setup.py build

develop:
	python setup.py develop

install:
	python setup.py install

clean:
	rm -Rf *.egg-info
	rm -Rf jinja2_getenv_extension/__pycache__
	rm -Rf tests/__pycache__
	rm -Rf .pytest_cache

test:
	flake8 .
	pytest
