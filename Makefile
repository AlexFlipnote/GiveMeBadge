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
    pyinstaller index.py --onefile --icon="./assets/logo.ico" --name $(NAME).exe
    rm $(NAME).exe.spec

compile-linux:
    python3 -m PyInstaller index.py --onefile --icon="./assets/logo.png" --name $(NAME)
    rm $(NAME).spec
