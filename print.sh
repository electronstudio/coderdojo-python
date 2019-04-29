#!/bin/bash
enscript *.py -p print.ps  --color -Epython -r -U2 --font=Courier18 --header-font=Courier-Bold22 --header='||$n'
