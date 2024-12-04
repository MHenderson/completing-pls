png: png/pls-3.png

png/pls-3.png: src/pls-3.py
	poetry run python $<

install:
	poetry install
