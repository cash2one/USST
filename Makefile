default: help

clean: FORCE
	@find -name '*.py[co]' -delete

FORCE:


help:
	@echo 'Usage: make [command]'
	@echo ''
	@echo 'Available commands:'
	@echo ''
	@echo '  clean            - delete *.py[co] files'
	@echo '  flake8           - Check Python style based on flake8'
	@echo '  test             - Run command: python -m usst.runtests'
	@echo '  build            - Run command: python setup.py build'
	@echo '  install          - Run command: python setup.py install'
	@echo '  run              - Run command: python -m usst'
	@echo '  help             - Show this help message and exit'

# Check code convention based on flake8
CHECK_DIRS=.
FLAKE8_CONFIG_DIR=tox.ini

flake8:
	flake8 $(CHECK_DIRS) --config=$(FLAKE8_CONFIG_DIR)

run:
	python -m usst

build:
	python setup.py build

install:
	python setup.py install

test:
	python -m usst.runtests
