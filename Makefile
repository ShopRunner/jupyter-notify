clean:
	rm -rf dist/

rst: README.md
	# on a mac, install pandoc with brew install pandoc
	pandoc --from=markdown --to=rst --output=README.rst README.md

html: README.rst
	python setup.py --long-description | rst2html.py > output.html

pypi-test: clean rst
	python setup.py sdist
	# twine upload dist/* -r testpypi
	python setup.py sdist upload -r testpypi

pypi-prod: clean rst
	python setup.py sdist
	# twine upload dist/*
	python setup.py sdist upload
