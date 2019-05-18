#!/bin/bash
enscript *.py -p print.ps  --color -Epython -r -U2 --font=Courier13 --header-font=Courier-Bold20 --header='||$n'
