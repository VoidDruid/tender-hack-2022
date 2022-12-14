# Vars
CODE_DIR = server
TESTS_DIR = tests
COV_LEVEL=95
PYTHONPATH = PYTHONPATH=./:$(CODE_DIR)

# Executables
PYTHON = $(PYTHONPATH) python3
POETRY = $(PYTHONPATH) poetry run

.PHONY: run-script migrations pretty help lint validate

run-script:  ## Запустить скрипты
	${PYTHON} -m scripts

migrations:  ## Создать миграции
	$(ALEMBIC) revision --autogenerate -m "$(message)"

pretty:  ## "Причесать" код - isort, black, пр.
	isort .
	black .
	autoflake --in-place --verbose -r .

lint:  ## Линтинг
	black --check $(CODE_DIR) tests
	pylint --jobs 4 --rcfile=pyproject.toml $(CODE_DIR)
	mypy $(CODE_DIR)

help:  ## Показать это сообщение
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

validate: lint test
