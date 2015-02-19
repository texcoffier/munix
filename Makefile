
%.html:%.rst
	rst2html $*.rst $*.html

install:munix.html
	cp munix.html munix.css $$HOME/public_html/MUNIX

munix.html:munix.rst

clean:
	@echo "CLEANING"
	-rm *~ *.pyc munix.html 2>/dev/null
