CONVERT = preamble.py colorize.py sheexp.py

%.html:%.rst
	rst2html $*.rst $*.html

all:regtest colorize.js doc_colorize.html munix.html

RapydScript:
	git clone git://github.com/atsepkov/RapydScript.git
	cd RapydScript ; git checkout 0483fac4745bca9c531d29963f2daca5e3330e7c

xxx.py: $(CONVERT) Makefile
	cat $(CONVERT) >$@

colorize.js:RapydScript licence.txt xxx.py
	@if [ "$$(which node)" = "" ] ; \
         then echo "Ne trouve pas NodeJS sous le nom 'node'" >&2 ; exit 1 ; fi
	(cat licence.txt ; \
	 git log --pretty=format:'// GIT commit %H' -n 1 ; \
	 echo ; \
	 RapydScript/bin/rapydscript --prettify --bare xxx.py) >$@
	sed 's/ՐՏ/JS/g' <$@ | iconv -f utf-8 -t ISO8859-15 >colorize-latin1.js

install:clean all
	cp --update colorize.js colorize.css doc_colorize.html test.html munix.html munix.css ~/public_html/MUNIX

munix.html:munix.rst colorize.js

doc_colorize.html:colorize.py create_doc.py
	./create_doc.py >doc_colorize.html

fyp.js:fyp.py
	RapydScript/bin/rapydscript --prettify --bare $? >$@

install-fyp:fyp.js
	scp -p fyp.js fyp.html highscores.py munix@demo710.univ-lyon1.fr:FYP
	ssh munix@demo710.univ-lyon1.fr "pkill --exact -f 'python3 ./highscores.py' ; cd FYP ; nohup ./highscores.py 2>/dev/null >&2 & sleep 1"

regtest:colorize.js
	./colorize_regtest.py
	./help_regtest.py

clean:
	@echo "CLEANING"
	-rm colorize.js xxx.py *~ *.pyc munix.html 2>/dev/null

key.js:key.py
	RapydScript/bin/rapydscript --prettify --bare $? >$@
