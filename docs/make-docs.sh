#!/usr/bin/env zsh

SCRIPT_DIR=${0:a:h}
cd $SCRIPT_DIR

rm -fr build generated-source
cp -R source generated-source
uv run sphinx-apidoc -o generated-source ../src
uv run sphinx-build generated-source build/html
