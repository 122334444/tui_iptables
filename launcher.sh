#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SOURCE="${DIR}/.virtualenvs/cli/bin/activate"
MAINSCRIPT="${DIR}/main.py"

source $SOURCE
python $MAINSCRIPT