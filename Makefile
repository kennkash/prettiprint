setup:
	pip install --upgrade -r dev-requirements.txt

build:
	python -m build

local-install:
	pip install -e .

install:
	pip install dist/*-py3-none-any.whl

uninstall:
	pip uninstall prettiprint

clean:
	rm -rf dist/

test:
	pytest demo/demo.py



REPOSITORY_URL := https://gitlab.smartcloud.samsungds.net/api/v4/projects/6621/packages/pypi
upload:

	twine upload --verbose --repository prettiprint dist/*


.PHONY: build local-install install uninstall clean test upload


bump-minor:
	@tbump "$$(tbump current-version | awk -F. '{printf "%d.%d.%d", $$1, $$2+1, 0}')"

bump-patch:
	@tbump "$$(tbump current-version | awk -F. '{printf "%d.%d.%d", $$1, $$2, $$3+1}')"

bump-major:
	@tbump "$$(tbump current-version | awk -F. '{printf "%d.%d.%d", $$1+1, 0, 0}')"


# Dry-run bump for MINOR version (no changes made)
dry-run-minor:
	@version=$$(tbump current-version); \
	next=$$(echo $$version | awk -F. '{printf "%d.%d.%d", $$1, $$2+1, 0}'); \
	echo "Dry running minor bump: $$version → $$next"; \
	tbump --dry-run $$next

# Dry-run bump for PATCH version
dry-run-patch:
	@version=$$(tbump current-version); \
	next=$$(echo $$version | awk -F. '{printf "%d.%d.%d", $$1, $$2, $$3+1}'); \
	echo "Dry running patch bump: $$version → $$next"; \
	tbump --dry-run $$next

# Dry-run bump for MAJOR version
dry-run-major:
	@version=$$(tbump current-version); \
	next=$$(echo $$version | awk -F. '{printf "%d.%d.%d", $$1+1, 0, 0}'); \
	echo "Dry running major bump: $$version → $$next"; \
	tbump --dry-run $$next