pip install -q pyinstaller
pip install -q chess
pip install -q random

python -m PyInstaller --onefile --noconfirm MoveGenerator.py

MOVE .\dist\MoveGenerator.exe .\

rmdir /s /q .\dist
rmdir /s /q .\build
del MoveGenerator.spec
