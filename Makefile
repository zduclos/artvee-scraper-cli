build: dependencies
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist .coverage .pytest_cache .mypy_cache *.egg-info
	find artvee_scraper_cli tests \( -name "*.py[co]" -o -name __pycache__ -o -name "*.egg-info" \) -exec rm -rf {} +

test: dependencies
	coverage run --source=artvee_scraper_cli -m pytest -rP -v tests && coverage report -m

format: dependencies
	python -m black artvee_scraper_cli

lint: dependencies
	python -m mypy --install-types artvee_scraper_cli
	python -m mypy artvee_scraper_cli

dependencies:
	pip install -r requirements.txt

.PHONY: build clean test dependencies
