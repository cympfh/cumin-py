pip-publish:
	pandoc --from markdown --to rst README.md -o README.rst
	python setup.py sdist upload
