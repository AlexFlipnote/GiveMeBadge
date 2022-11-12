NAME = GiveMeBadge

target:
	@echo "Hello World"

install:
	pip install -r requirements.txt

compile:
	pyinstaller index.py --onefile --icon=logo.ico --name $(NAME).exe
	rm $(NAME).exe.spec
