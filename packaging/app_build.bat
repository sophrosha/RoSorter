@echo off
setlocal

cd ..

echo 1/5 : Clean build files..
if exist build rd /s /q build
if exist dist rd /s /q dist

echo 2/5 : Check venv..
if not exist .venv (
    echo ^-^> ^: ^Creating venv...
    python -m venv venv
    call .venv\Scripts\activate
    echo ^-^> ^: ^Installing dependencies..
    pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

echo 3/5 : Build started..
pyinstaller --noconfirm --clean packaging\pyinstaller_build.spec

echo 4/5 : Coping config.yaml to build..
copy assets\config.yaml dist\RoSorter\

echo 5/5 Done! Check dist folder.
pause