lint-all:
        uv run ruff check .

lint-file filename:
        uv run ruff check {{filename}}

format-all:
        uv run ruff format .

format-file filename:
        uv run ruff format {{filename}}
