#!/usr/bin/env python3

import time
from utils import timeperiod, footer
from xml2dict import XML2Dict


def academic():
    # add header template
    print("Generating academic.html...")
    output = open('../html/academic.html', 'r').read()

    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/academic.xml', 'r').read())

    output += '<h2 class="first">Steering Committee Membership</h2>\n'
    output += '<ul class="talks">\n'
    output += '<li><strong><a href="http://zeus-workshop.eu/">ZEUS Workshop Series</a></strong><br />Central European Workshop on Services and their Composition</li>'
    output += '</ul>\n'

    #####################################
    # part 1: Organization of Workshops #
    #####################################

    # transform date types
    for entry in data.scientific.organization.workshop:
        entry.begin = time.strptime(entry.begin, '%d %b %Y')
        entry.end = time.strptime(entry.end, '%d %b %Y')

    # sort by begin date
    data.scientific.organization.workshop = sorted(data.scientific.organization.workshop, key=lambda k: k.begin, reverse=True)

    # output
    output += '<h2>Organization of Workshops</h2>\n'
    output += '<ul class="talks">\n'

    for entry in data.scientific.organization.workshop:

        # title
        output += '<li><strong>'

        if 'abbreviation' in entry:
            output += entry.title
            if 'url' in entry:
                output += ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)'
            else:
                output += ' (' + entry.abbreviation.replace(" ", "&nbsp;") + ')'
        else:
            if 'url' in entry:
                output += '<a href="' + entry.url + '">' + entry.title + '</a>'
            else:
                output += entry.title

        output += '</strong><br/>\n'

        # colocation
        if 'kind' in entry:
            output += entry.kind
            if 'colocation' in entry:
                output += ', '
                if 'courl' in entry:
                    output += 'part of <a href="' + entry.courl + '">' + entry.colocation + '</a>'
                else:
                    output += 'part of ' + entry.colocation
        else:
            if 'colocation' in entry:
                if 'courl' in entry:
                    output += 'part of <a href="' + entry.courl + '">' + entry.colocation + '</a>'
                else:
                    output += 'part of ' + entry.colocation

        # date
        output += '<br/>'
        output += timeperiod(entry.begin, entry.end)

        # venue
        if 'venue' in entry:
            output += ' in ' + entry.venue

        output += '</li>\n'

    output += '</ul>\n'

    ##########################
    # part 2: PC memberships #
    ##########################

    # transform date types
    for entry in data.scientific.memberships.pc:
        entry.date = time.strptime(entry.date, '%d %b %Y')
        entry.begin = time.strptime(entry.begin, '%d %b %Y')
        entry.end = time.strptime(entry.end, '%d %b %Y')

    # sort by begin date
    data.scientific.memberships.pc = sorted(data.scientific.memberships.pc, key=lambda k: k.begin, reverse=True)

    # output
    output += '<h2>Program Committee Memberships</h2>\n'
    output += '<ul class="talks">\n'
    for entry in data.scientific.memberships.pc:

        # title
        output += '<li><strong>'

        if 'abbreviation' in entry:
            output += entry.title
            if 'url' in entry:
                output += ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)'
            else:
                output += ' (' + entry.abbreviation.replace(" ", "&nbsp;") + ')'
        else:
            if 'url' in entry:
                output += '<a href="' + entry.url + '">' + entry.title + '</a>'
            else:
                output += entry.title

        if 'role' in entry:
            output += ' &mdash; ' + entry.role

        output += '</strong><br/>\n'

        # colocation
        if 'kind' in entry:
            output += entry.kind
            if 'colocation' in entry:
                output += ', '
                if 'courl' in entry:
                    output += 'part of <a href="' + entry.courl + '">' + entry.colocation + '</a>'
                else:
                    output += 'part of ' + entry.colocation
        else:
            if 'colocation' in entry:
                if 'courl' in entry:
                    output += 'part of <a href="' + entry.courl + '">' + entry.colocation + '</a>'
                else:
                    output += 'part of ' + entry.colocation

        # date
        output += '<br/>'
        output += timeperiod(entry.begin, entry.end)

        # venue
        if 'venue' in entry:
            output += ' in ' + entry.venue

        # call for paper
        if 'cfp' in entry and entry.begin > time.localtime():
            output += '<br/><a href="' + entry.cfp + '">Call for papers</a>'

        output += '</li>\n'

    output += '</ul>\n'

    ###########################
    # part 3: Journal Reviews #
    ###########################

    # sort by journal title
    data.scientific.journalreviews.journal = sorted(data.scientific.journalreviews.journal, key=lambda k: k.title)

    # output
    output += '<h2>Journal Reviewing Activities</h2>\n'
    output += '<ul class="talks">\n'
    for entry in data.scientific.journalreviews.journal:

        # title
        output += '<li><strong>'

        if 'url' in entry:
            output += '<a href="' + entry.url + '">' + entry.title + '</a>'
        else:
            output += entry.title
        output += '</strong></li>\n'

    output += '</ul>\n'


    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing academic.html...")
    f = open('../../academic.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()

def main():
    academic()

if __name__ == '__main__':
    main()
