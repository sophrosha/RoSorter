#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.."

echo "1/5 : Cleaning build files.."
rm -rf build dist

echo "2/5 : Preparing environment.."
if [ "$CI" = "true" ]; then
    echo "-> CI detected.."
elif [ -d ".venv" ]; then
    echo "-> .venv found!"
    echo "-> Activating.."
    source .venv/bin/activate
else
    echo "-> Creating .venv.."
    echo "-> Activating..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo "-> Installing dependencies.."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
pip install pyinstaller --quiet

echo "3/5 : Building with PyInstaller.."
pyinstaller --noconfirm --clean packaging/pyinstaller_build.spec

echo "4/5 : Copying config.yaml to dist.."
if [ -d "dist/RoSorter" ]; then
    cp assets/config.yaml dist/RoSorter/
    echo "-> config.yaml copied.."
else
    echo "dist/RoSorter not found in dir.. Exit."
    exit 1
fi

echo "5/5 : Done! Check dist folder."