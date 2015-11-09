default: help

clean: FORCE
	@find -name '*.py[co]' -delete

# Check code convention based on flake8
CHECK_DIRS=.
FLAKE8_CONFIG_DIR=tox.ini

flake8:
	flake8 $(CHECK_DIRS) --config=$(FLAKE8_CONFIG_DIR)

run:
	python wsgi.py