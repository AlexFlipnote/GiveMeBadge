NAME = GiveMeBadge

target:
	@echo "Hello World"

clean:
	@echo "Cleaning up..."
	rm -rf ./build
	rm -rf ./dist
	rm *.spec

install:
	pip install -r requirements.txt

compile-win:
    pyinstaller index.py --onefile --icon=logo.ico --name $(NAME).exe
    rm $(NAME).exe.spec

compile-linux:
    python3 -m PyInstaller index.py --onefile --icon=logo.ico --name $(NAME)
    rm $(NAME).spec
