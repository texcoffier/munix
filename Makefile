CONVERT = preamble.py colorize.py sheexp.py

%.html:%.rst
	rst2html $*.rst $*.html

all:regtest colorize.js doc_colorize.html munix.html

RapydScript:
	git clone git://github.com/atsepkov/RapydScript.git
	cd RapydScript ; git checkout e2c8b247a5b1a1024a8e7adae188b7bb78a77ede

colorize.js:RapydScript licence.txt $(CONVERT)
	@if [ "$$(which node)" = "" ] ; \
         then echo "Ne trouve pas NodeJS sous le nom 'node'" >&2 ; exit 1 ; fi
	(cat licence.txt ; \
         git log --pretty=format:'// GIT commit %H' -n 1 ; \
	 echo ; \
         cat $(CONVERT) | tee xxx.py | \
         RapydScript/bin/rapydscript --prettify --bare \
        ) >$@
	sed 's/ՐՏ/JS/g' <$@ | iconv -f utf-8 -t ISO8859-15 >colorize-latin1.js

install:clean all
	cp --update colorize.js colorize.css doc_colorize.html test.html munix.html munix.css ~/public_html/MUNIX

munix.html:munix.rst colorize.js

doc_colorize.html:colorize.py create_doc.py
	./create_doc.py >doc_colorize.html


regtest:colorize.js
	./colorize_regtest.py

clean:
	@echo "CLEANING"
	-rm colorize.js *~ *.pyc munix.html 2>/dev/null
