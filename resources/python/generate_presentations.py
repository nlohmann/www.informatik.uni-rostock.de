#!/usr/bin/env python3

import time
import sys
from utils import timeperiod, footer, placelink
from xml2dict import XML2Dict


def presentations():
    # add header template
    print("Generating presentations.html...")
    output = open('../html/presentations.html', 'r').read()

    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/presentations.xml', 'r').read())


    #########################
    # part 1: Invited Talks #
    #########################

    # transform date types
    for entry in data.presentations.invited.talk:
        entry.date = time.strptime(entry.date, '%d %b %Y')

    # sort by begin date
    data.presentations.invited.talk = sorted(data.presentations.invited.talk, key=lambda k: k.date, reverse=True)

    output += '<h2 class="first">Invited Presentations</h2>'
    output += '<ul class="talks">\n'

    for entry in data.presentations.invited.talk:

        output += '<li id="' + entry.id + '">'
        if 'slideshare' in entry:
            output += '<a href="' + entry.slideshare + '" title="slides of the talk at Slideshare"></a>'
        if 'vimeo' in entry:
            output += '<a href="' + entry.vimeo + '" title="video of the talk at Vimeo"></a>'
        output += '<strong>' + entry.title + '</strong><br/>'
        output += entry.detail + '<br/>'

        if entry.date > time.localtime():
            output += 'to be held on '

        output += timeperiod(entry.date, entry.date) + ' in ' + placelink(entry.venue)
        output += '</li>\n'

        # output for Slideshare.net
        stdoutput = '\nInvited presentation given by Niels Lohmann on ' + timeperiod(entry.date, entry.date)
        stdoutput += ' in ' + entry.venue + ' as ' + entry.detail
        if stdoutput[-1] != '.':
            stdoutput += '.\n'
        sys.stderr.write(stdoutput)

    output += '</ul>\n'


    ############################
    # part 2: Conference Talks #
    ############################

    # transform date types
    for entry in data.presentations.conferences.talk:
        entry.date = time.strptime(entry.date, '%d %b %Y')

    # sort by begin date
    data.presentations.conferences.talk = sorted(data.presentations.conferences.talk, key=lambda k: k.date, reverse=True)

    output += '<h2>Conference Presentations</h2>'
    output += '<ul class="talks">\n'

    for entry in data.presentations.conferences.talk:

        output += '<li id="' + entry.id + '">'
        if 'slideshare' in entry:
            output += '<a href="' + entry.slideshare + '" title="slides of the talk at Slideshare"></a>'
        if 'vimeo' in entry:
            output += '<a href="' + entry.vimeo + '" title="video of the talk at Vimeo"></a>'
        output += '<strong>' + entry.title + '</strong><br/>'
        if 'abbreviation' in entry:
            output += '<em>' + entry.conference + ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)</em><br/>'
        else:
            output += '<em><a href="' + entry.url + '">' + entry.conference + ' </a></em><br/>'

        if entry.date > time.localtime():
            output += 'to be held on '

        output += timeperiod(entry.date, entry.date) + ' in ' + placelink(entry.venue)
        output += '</li>\n'

        # output for Slideshare.net
        stdoutput = '\nConference presentation given by Niels Lohmann on ' + timeperiod(entry.date, entry.date)
        stdoutput += ' in ' + entry.venue + ' at the ' + entry.conference
        if 'abbreviation' in entry:
            stdoutput += ' (' + entry.abbreviation + ')'
        stdoutput += '.\n'
        sys.stderr.write(stdoutput)

    output += '</ul>\n'


    ##########################
    # part 3: Workshop Talks #
    ##########################

    # transform date types
    for entry in data.presentations.workshops.talk:
        entry.date = time.strptime(entry.date, '%d %b %Y')

    # sort by begin date
    data.presentations.workshops.talk = sorted(data.presentations.workshops.talk, key=lambda k: k.date, reverse=True)

    output += '<h2>Workshop Presentations</h2>'
    output += '<ul class="talks">\n'

    for entry in data.presentations.workshops.talk:

        output += '<li id="' + entry.id + '">'
        if 'slideshare' in entry:
            output += '<a href="' + entry.slideshare + '" title="slides of the talk at Slideshare"></a>'
        if 'vimeo' in entry:
            output += '<a href="' + entry.vimeo + '" title="video of the talk at Vimeo"></a>'
        output += '<strong>' + entry.title + '</strong><br/>'
        if 'abbreviation' in entry:
            if 'url' in entry:
                output += '<em>' + entry.conference + ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)'
            else:
                output += '<em>' + entry.conference + ' (' + entry.abbreviation.replace(" ", "&nbsp;") + ')'
        else:
            if 'url' in entry:
                output += '<em><a href="' + entry.url + '">' + entry.conference + '</a>'
            else:
                output += '<em>' + entry.conference
        if 'colocation' in entry:
            if 'courl' in entry:
                output += '; part of <a href="' + entry.courl + '">' + entry.colocation.replace(" ", "&nbsp;") + '</a>'
            else:
                output += '; part of ' + entry.colocation.replace(" ", "&nbsp;")
        output += '</em><br/>'

        if entry.date > time.localtime():
            output += 'to be held on '

        output += timeperiod(entry.date, entry.date) + ' in ' + placelink(entry.venue)
        output += '</li>\n'

        # output for Slideshare.net
        stdoutput = '\nWorkshop presentation given by Niels Lohmann on ' + timeperiod(entry.date, entry.date)
        stdoutput += ' in ' + entry.venue + ' at the ' + entry.conference
        if 'abbreviation' in entry:
            stdoutput += ' (' + entry.abbreviation + ')'
        if 'colocation' in entry:
            stdoutput += '; part of ' + entry.colocation
        stdoutput += '.\n'
        sys.stderr.write(stdoutput)

    output += '</ul>\n'


    ##########################
    # part 4: Demonstrations #
    ##########################

    # transform date types
    for entry in data.presentations.demonstrations.talk:
        entry.date = time.strptime(entry.date, '%d %b %Y')

    # sort by begin date
    data.presentations.demonstrations.talk = sorted(data.presentations.demonstrations.talk, key=lambda k: k.date, reverse=True)

    output += '<h2>Tool Demonstrations</h2>'
    output += '<ul class="talks">\n'

    for entry in data.presentations.demonstrations.talk:

        output += '<li id="' + entry.id + '">'
        if 'slideshare' in entry:
            output += '<a href="' + entry.slideshare + '" title="slides of the talk at Slideshare"></a>'
        if 'vimeo' in entry:
            output += '<a href="' + entry.vimeo + '" title="video of the talk at Vimeo"></a>'
        output += '<strong>' + entry.title + '</strong><br/>'
        if 'abbreviation' in entry:
            if 'url' in entry:
                output += '<em>' + entry.conference + ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)'
            else:
                output += '<em>' + entry.conference + ' (' + entry.abbreviation.replace(" ", "&nbsp;") + ')'
        else:
            if 'url' in entry:
                output += '<em><a href="' + entry.url + '">' + entry.conference + '</a>'
            else:
                output += '<em>' + entry.conference
        if 'colocation' in entry:
            if 'courl' in entry:
                output += '; part of <a href="' + entry.courl + '">' + entry.colocation.replace(" ", "&nbsp;") + '</a>'
            else:
                output += '; part of ' + entry.colocation.replace(" ", "&nbsp;")
        output += '</em><br/>'
        output += timeperiod(entry.date, entry.date) + ' in ' + placelink(entry.venue)
        output += '</li>\n'

        # output for Slideshare.net
        stdoutput = '\nTool demonstration given by Niels Lohmann on ' + timeperiod(entry.date, entry.date)
        stdoutput += ' in ' + entry.venue + ' at the ' + entry.conference
        if 'abbreviation' in entry:
            stdoutput += ' (' + entry.abbreviation + ')'
        if 'colocation' in entry:
            stdoutput += '; part of ' + entry.colocation
        stdoutput += '.\n'
        sys.stderr.write(stdoutput)

    output += '</ul>\n'



    #########################
    # part 5: Miscellaneous #
    #########################

    # transform date types
    for entry in data.presentations.miscellaneous.talk:
        entry.date = time.strptime(entry.date, '%d %b %Y')

    # sort by begin date
    data.presentations.miscellaneous.talk = sorted(data.presentations.miscellaneous.talk, key=lambda k: k.date, reverse=True)

    output += '<h2>Miscellaneous</h2>'
    output += '<ul class="talks">\n'

    for entry in data.presentations.miscellaneous.talk:

        output += '<li id="' + entry.id + '">'
        output += '<a href="' + entry.slideshare + '" title="slides of the talk at Slideshare"></a>'
        if 'vimeo' in entry:
            output += '<a href="' + entry.vimeo + '" title="video of the talk at Vimeo"></a>'
        output += '<strong>' + entry.title + '</strong><br/>'
        output += entry.detail + '<br/>'
        output += timeperiod(entry.date, entry.date) + ' in ' + placelink(entry.venue)
        output += '</li>\n'

        # output for Slideshare.net
        stdoutput = '\nPresentation given by Niels Lohmann on ' + timeperiod(entry.date, entry.date)
        stdoutput += ' in ' + entry.venue + '; ' + entry.detail
        stdoutput += '.\n'
        sys.stderr.write(stdoutput)

    output += '</ul>\n'



    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing presentations.html...")
    f = open('../../presentations.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()

def main():
    presentations()

if __name__ == "__main__": main()
