#!/bin/sh

rm -fr _publish

FILES=`ls -1`

mkdir -p _publish

for FILE in $FILES; do
    cp -r $FILE _publish
done

cd _publish

rm -fr resources/bibtex resources/html resources/python resources/teaching resources/xml
rm -fr *.sh

find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

rm -fr /users/teo00/nl/public_html/*
cp -r * /users/teo00/nl/public_html

cd ..
rm -fr _publish
