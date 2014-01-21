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
