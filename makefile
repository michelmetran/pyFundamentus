# ------------------------------------------------------------------------------
#  Name: makefile
#  Version: 0.0.1
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------

build:
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade twine
	python3 -m build
	python3 -m twine upload dist/* --verbose


clean:
	rm -rf build
	rm -rf dist
	rm -rf fundamentus.egg-info


test:
	clear
	pytest ./fundamentus/* -v -s -r X --color=yes --cache-clear --code-highlight=yes


coverage:
	clear
	coverage run -m pytest ./fundamentus/* -v -s -r X --color=yes --cache-clear --code-highlight=yes
	coverage report -m
	coverage html


pylint:
	clear
	pylint ./fundamentus/* --load-plugins=pylint.extensions.docparams --rcfile=.pylintrc


.PHONY: build clean test coverage pyliny
