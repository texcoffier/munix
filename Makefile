CONVERT = preamble.py colorize.py sheexp.py

%.html:%.rst
	rst2html $*.rst $*.html

all:regtest colorize.js doc_colorize.html munix.html


colorize.js:licence.txt $(CONVERT)
	(cat licence.txt ; \
         cat $(CONVERT) | RapydScript/bin/rapydscript --prettify --bare \
        ) >$@

install:all
	cp --update colorize.js colorize.css doc_colorize.html test.html munix.html munix.css ~/public_html/MUNIX

munix.html:munix.rst colorize.js

doc_colorize.html:colorize.py create_doc.py
	./create_doc.py >doc_colorize.html


regtest:
	./colorize_regtest.py

clean:
	@echo "CLEANING"
	-rm *~ *.pyc munix.html 2>/dev/null
