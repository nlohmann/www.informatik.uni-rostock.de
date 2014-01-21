#!/usr/bin/env python3

import time
from utils import timeperiod, footer
from xml2dict import XML2Dict


def teaching():
    # add header template
    print("Generating teaching.html...")
    output = open('../html/teaching.html', 'r').read()

    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/teaching.xml', 'r').read())


    #################################
    # part 1: Supervision of Theses #
    #################################

    output += '<h2 class="first">Supervision of Theses</h2>'
    output += '<ul class="talks">\n'

    for entry in data.teaching.supervisions.thesis:

        output += '<li>' + entry.author + '. '
        output += '<strong>' + entry.title + '</strong><br/>'
        output += entry.type + ', ' + entry.institution
        if 'date' in entry:
            entry.date = time.strptime(entry.date, '%d %b %Y')
            output += ', submitted ' + timeperiod(entry.date, entry.date)
        else:
            output += ', expected ' + entry.expected
        output += '</li>\n'

    output += '</ul>\n'


    ####################
    # part 2: Lectures #
    ####################

    output += '<h2>Lectures</h2>'
    output += '<ul class="talks">\n'

    for entry in data.teaching.lectures.lecture:

        output += '<li>'
        output += '<strong>' + entry.title
        if 'byProxy' in entry:
            output += ' &mdash; by proxy'
        output += '</strong><br/>'
        if 'detail' in entry:
            output += entry.detail + ', '
        output += entry.institution + ' (' + entry.term + ')'
        output += '</li>\n'

    output += '</ul>\n'


    ####################
    # part 3: Seminars #
    ####################

    output += '<h2>Seminars</h2>'
    output += '<ul class="talks">\n'

    for entry in data.teaching.seminars.seminar:

        output += '<li>'
        output += '<strong>' + entry.title
        if 'byProxy' in entry:
            output += ' &mdash; by proxy'
        output += '</strong><br/>'
        if 'detail' in entry:
            output += entry.detail + ', '
        output += entry.institution + ' (' + entry.term + ')'
        output += '</li>\n'

    output += '</ul>\n'


    #####################
    # part 4: Exercises #
    #####################

    output += '<h2>Exercises</h2>'
    output += '<ul class="talks">\n'

    for entry in data.teaching.exercises.exercise:

        output += '<li>'

#        if 'evaluation' in entry:
#            output += '<a href="files/' + entry.evaluation + '" class="evaluation"></a>'

        output += '<strong>'
        
        if 'page' in entry:
            output += '<a href="teaching/' + entry.page + '.html">' + entry.title + '</a>'
        else:
            output += entry.title

        output += '</strong><br/>'
        if 'detail' in entry:
            output += entry.detail + ', '
        output += entry.institution + ' (' + entry.term + ')'
        output += '</li>\n'

    output += '</ul>\n'




    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing teaching.html...")
    f = open('../../teaching.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()

def main():
    teaching()

if __name__ == "__main__": main()
