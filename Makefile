NAME = GiveMeBadge

target:
	@echo "say hello to everyone"

clean:
	@echo "Cleaning up junk files..."
	rm -rf ./build
	rm -rf ./dist
	rm *.exe.spec

install:
	pip install -r requirements.txt

compile:
	pyinstaller index.py --onefile --icon="./assets/logo.ico" --name $(NAME).exe
