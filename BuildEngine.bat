pip install -q pyinstaller
pip install -q chess
pip install -q random

python -m PyInstaller --noconfirm MoveGenerator.py

MOVE .\dist\MoveGenerator\MoveGenerator.exe .\

rmdir /s /q .\dist;
rmdir /s /q .\build;
del MoveGenerator.spec
