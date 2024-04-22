install:
	poetry install

update:
	poetry update

lock:
	poetry lock

build: 
	poetry export --format requirements.txt --output requirements.txt
	docker build -t ${BUILD_TAG} .
	rm -rf requirements.txt

run:
	poetry run uvicorn app.app.main:app --reload

typecheck:
	poetry run mypy --strict source/app 

format:
	poetry run ruff format  

lint:
	poetry run ruff check

fix:
	poetry run ruff check --fix
	poetry run ruff format

scan:
	poetry run bandit source/app

test:
	poetry run pytest --cov=app 


.PHONY: build