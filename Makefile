run:
	@poetry run u2s
build:
	@poetry build
package-install:
	python -m pip install  dist/*.whl --force-reinstall