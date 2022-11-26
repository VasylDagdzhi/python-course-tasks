.PHONY: all \
		setup \
		lint \
		unittest \
		pytest \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup_dev: ## project setup
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install wheel setuptools
	. venv/bin/activate; pip install -r dev_requirements.txt

setup_prod: ## project setup
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install wheel setuptools
	. venv/bin/activate; pip install -r prod_requirements.txt

lint: ## Check code quality
	. venv/bin/activate; black ./
	. venv/bin/activate; flake8

unittest: ## Check code quality
	. venv/bin/activate; python -m unittest unittests.py

pytest: ## Start testing with pytest
	. venv/bin/activate; pytest pytests.py

run_enc_pyjwt: ## Run encode by pyjwt for the input.json and save the result in output.json
	. venv/bin/activate; python3 main.py  --secret="A" --salt="B" --using="pyjwt" --action="encode" --input_file="input.json" --output_file="output.json"
run_enc_itsdan: ## Run encode by itsdangerous for the input.json and save the result in output.json
	. venv/bin/activate; python3 main.py  --secret="A" --salt="B" --using="itsdangerous" --action="encode" --input_file="input.json" --output_file="output.json"

run_dec_pyjwt: ## Run decode by pyjwt for the output.json and save the result in output2.json
	. venv/bin/activate; python3 main.py  --secret="A" --salt="B" --using="pyjwt" --action="decode" --input_file="output.json" --output_file="output2.json"
run_dec_itsdan: ## Run decode by itsdangerous for the output.json and save the result in output2.json
	. venv/bin/activate; python3 main.py  --secret="A" --salt="B" --using="itsdangerous" --action="decode" --input_file="output.json" --output_file="output2.json"
