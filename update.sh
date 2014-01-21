#!/bin/sh

# update tpp.bib
#cp "/Users/niels/Documents/Repositories/tpp/tools/bibtex2html/tpp.bib" resources/bibtex

cd resources/python

./generate_academic.py
./generate_presentations.py
./generate_publications.py
./generate_teaching.py
./generate_tools.py
./generate_news.py

cd ../..

svn add publications/* 2> /dev/null

for FILE in publications.html presentations.html academic.html teaching.html tools.html index.html
do
#  xmllint --format $FILE --output $FILE~ 2>/dev/null
  tidy -asxhtml -indent  --indent-spaces 2 -wrap 0 --new-blocklevel-tags article,header,footer,nav,aside -utf8 --new-inline-tags video,audio,canvas,ruby,rt,rp,time -modify $FILE 2>/dev/null
  gsed -i '1,4d' $FILE
  cat resources/html/header.html $FILE > $FILE~
  mv $FILE~ $FILE
done

rm -fr resources/python/__pycache__
