png: png/pls-3.png png/pls-10-before.png png/pls-10-after.png

png/pls-3.png: src/pls-3.py
	poetry run python $<

png/pls-10-before.png: src/pls-10-before.py
	poetry run python $<

png/pls-10-after.png: src/pls-10-after.py
	poetry run python $<

install:
	poetry install
