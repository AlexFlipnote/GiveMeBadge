NAME = GiveMeBadge

target:
	@echo "Hello World"

compile:
	pyinstaller index.py --onefile --icon=logo.ico --name $(NAME).exe
	rm $(NAME).exe.spec
