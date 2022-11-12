NAME = GiveMeBadge

target:
	@echo "Hello World"

clean:
	@echo "Cleaning up..."
	rm -rf ./build
	rm -rf ./dist
	rm *.exe.spec

install:
	pip install -r requirements.txt

compile:
	pyinstaller index.py --onefile --icon="./assets/logo.ico" --name $(NAME).exe
