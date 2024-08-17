@echo off
python.exe -m PyInstaller --distpath res/dist --workpath res/build --name gmnl --onefile ../../src/main.py --add-data "../../res;res"