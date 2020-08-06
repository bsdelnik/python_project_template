clean:
	python setup.py clean --all
	rm -rf *.pyc __pycache__ build dist sod_client.egg-info sod_client/__pycache__ tests/__pycache__ .pytest_cache .tox .mypy_cache sod_client/.mypy_cache tests/.mypy_cache app_status app_error