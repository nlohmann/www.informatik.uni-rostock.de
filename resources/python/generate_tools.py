#!/usr/bin/env python3

import time
from utils import timeperiod, footer
from xml2dict import XML2Dict
import generate_publications


def tools():
    # add header template
    print("Generating tools.html...")
    output = open('../html/tools.html', 'r').read()

    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/tools.xml', 'r').read())

    # fetch papers
    paperdata = generate_publications.init()

    first = True

    for entry in data.tooling.tools.tool:
        release = time.strptime(entry.release, '%d %b %Y')

        if first:
            output += '<h2 class="first">' + entry.name + '</h2>'
            first = False
        else:
            output += '<h2>' + entry.name + '</h2>'

        output += '<ul class="talks">\n'

        output += '<li>' + entry.description.replace(entry.name, '<strong>' + entry.name + '</strong>') + '</li>\n'

        if 'paper' in entry:
            output += generate_publications.formatentry(generate_publications.entrybyname(entry.paper, paperdata)) + '\n'

        if 'codevelopers' in entry:
            if entry.codevelopers.find('and') != -1:
                output += '<li>co-developers: ' + entry.codevelopers + '</li>\n'
            else:
                output += '<li>co-developer: ' + entry.codevelopers + '</li>\n'

        output += '<li>development status: ' + entry.status + '</li>\n'
        output += '<li>latest release: ' + timeperiod(release, release) + '</li>\n'
        output += '</ul>\n'


    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing tools.html...")
    f = open('../../tools.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()

def main():
    tools()

if __name__ == "__main__": main()
