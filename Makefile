clean:
	touch lol.pyc
	touch lol.lol~
	find . -name "*.pyc" | xargs rm 
	find . -name "*~" | xargs rm

push: clean
	git add *
	git rm --cache ~/Projects/c0nradsc0rner/c0nradsc0rner/settings.py
	git rm --cache ~/Projects/c0nradsc0rner/c0nradc0rnerDB
	git commit -m "auto push"
	git push origin master
