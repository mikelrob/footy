#!/bin/bash
source $HOME/footy/py_env/bin/activate

xvfb-run --auto-servernum --server-num=1 -a -s "-screen 0 1900x1200x24" python $HOME/footy/footy.py

