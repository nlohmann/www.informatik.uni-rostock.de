#!/bin/sh

svn commit --message "automatic update"
ssh ekas "cd public_html ; svn update ; chmod a+r *.html ; chmod a+x files resources teaching publications ; find resources -type d -exec chmod 755 {} \; ; find resources -type f -exec chmod 644 {} \; ; find publications -type f -exec chmod 644 {} \; ; find teaching -type f -exec chmod 644 {} \; ; find files -type d -exec chmod 755 {} \; ; find files -type f -exec chmod 644 {} \;"
