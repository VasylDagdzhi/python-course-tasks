.PHONY: all \
		setup \
		lint \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup: ## project setup
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

lint: ## Check code quality
	. venv/bin/activate; black ./
	. venv/bin/activate; flake8  --ignore=E501,W503 ./classes.py ./decorator.py ./main.py


run: ## Run
	. venv/bin/activate; python main.py