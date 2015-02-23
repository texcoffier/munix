
%.html:%.rst
	rst2html $*.rst $*.html

install:munix.html
	cp munix.html munix.css $$HOME/public_html/MUNIX

munix.html:munix.rst colorize.js

regtest:
	./colorize_regtest.py

CONVERT = preamble.py colorize.py

colorize.js:regtest $(CONVERT)
	cat $(CONVERT) | RapydScript/bin/rapydscript --prettify --bare >$@

clean:
	@echo "CLEANING"
	-rm *~ *.pyc munix.html 2>/dev/null
