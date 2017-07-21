rst: README.md
	# on a mac, install pandoc with brew install pandoc
	pandoc --from=markdown --to=rst --output=README.rst README.md

html: README.rst
	python setup.py --long-description | rst2html.py > output.html
