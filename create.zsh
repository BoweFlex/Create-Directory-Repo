#!/bin/zsh

function create() {	
	cd ~/Projects
	mkdir $1
	cd ~/Projects/$1

	python ~/Projects/CreateProj/main.py $1
	
	git init
	touch README.md
	echo "# $1" >> README.md

	sleep 1
	git add .
	git commit -m "First Commit"
	git remote add origin https://github.com/BoweFlex/$1.git
	git push -u origin master

	code .
}
