#!/usr/bin/env python3

import time
from utils import timeperiod, footer, placelink
from xml2dict import XML2Dict
import generate_publications
import re

##############################################################################

def print_paper_accepted(entry, paperdata):
    paper = generate_publications.formatentry(generate_publications.entrybyname(entry.paper, paperdata))

    foo = generate_publications.entrybyname(entry.paper, paperdata)
    if 'inproceedings' in foo:
        title = foo['inproceedings']['title']['value']
        venue = 'for the ' + foo['inproceedings']['booktitle']['value']

    if 'article' in foo:
        title = foo['article']['title']['value']
        venue = 'for ' + foo['article']['journal']['value']

    result = 'The paper “<a href="publications.html#' + foo.id + '">' + title + '</a>”'
    result += ' has been accepted ' + venue + '.'
    result += ' (' + timeperiod(entry.begin, entry.end) + ').'
    return result

def print_pc(entry):
    result = 'I was nominated as '

    if 'role' in entry:
        result += entry.role
    else:
        result += 'member'

    result += ' of the program committee of the '

    if 'kind' in entry:
        result += entry.kind + ' '

    result += '“'
    
    if 'abbreviation' in entry:
        result += entry.title
        if 'url' in entry:
            result += ' (<a href="' + entry.url + '">' + entry.abbreviation.replace(" ", "&nbsp;") + '</a>)'
        else:
            result += ' (' + entry.abbreviation.replace(" ", "&nbsp;") + ')'
    else:
        if 'url' in entry:
            result += '<a href="' + entry.url + '">' + entry.title + '</a>'
        else:
            result += entry.title

    result += '”'
    
    result += ' (' + timeperiod(entry.begin, entry.end) + ').'
    return result


def print_visit(entry):
    result = ''
    if entry.end > time.localtime():
        result += 'I shall visit '
    else:
        result += 'I visited '

    result += entry.text
    result += ' (' + timeperiod(entry.begin, entry.end) + ').'

    return result

def print_lecture(entry):
    result = ''
    if entry.end > time.localtime():
        result += 'I shall give a talk '
    else:
        result += 'I gave a talk '

    if 'talkid' in entry:
        result += 'on “<a href="presentations.html#' + entry.talkid + '">' + entry.title + '</a>” at the '
    else:
        result += 'on “' + entry.title + '” at the '

    if 'url' in entry:
        result += '<a href="' + entry.url + '">' + entry.text + '</a>'
    else:
        result += entry.text

    result += ' in ' + placelink(entry.venue)
    result += ' (' + timeperiod(entry.begin, entry.end) + ')'

    return result

def print_venue(entry):
    result = ''
    if entry.end > time.localtime():
        result += 'I shall attend '
    else:
        result += 'I attended '

    result += 'the '
    if 'url' in entry:
        if 'abbreviation' in entry:
            result += entry.text + ' (<a href="' + entry.url + '">' + entry.abbreviation + '</a>)'
        else:
            result += '<a href="' + entry.url + '">' + entry.text + '</a>'
    else:
        result += entry.text
        if 'abbreviation' in entry:
            result += ' (' + entry.abbreviation + ')'

    result += ' in ' + placelink(entry.venue)
    result += ' (' + timeperiod(entry.begin, entry.end) + ')'

    if 'talkid' in entry:
        # read data XML file
        xml = XML2Dict()
        data = xml.fromstring(open('../xml/presentations.xml', 'r').read())

        # transform date types
        for entry2 in data.presentations.conferences.talk:
            entry2.date = time.strptime(entry2.date, '%d %b %Y')
        for entry2 in data.presentations.workshops.talk:
            entry2.date = time.strptime(entry2.date, '%d %b %Y')

        # look for talk with given id
        for entry2 in data.presentations.conferences.talk:
            if entry2.id == entry.talkid:
                t = entry2.title
                d = entry2.date
        for entry2 in data.presentations.workshops.talk:
            if entry2.id == entry.talkid:
                t = entry2.title
                d = entry2.date

        result += ' and '
        if entry.end > time.localtime():
            result += 'give '
        else:
            result += 'gave '
        result += 'a talk on “<a href="presentations.html#' + entry.talkid + '">' + t + '</a>.”'

        # only print presentation date if venue is longer than one day
        if entry.begin != entry.end:
            result += ' (' + timeperiod(d, d) + ')'

    result += '.'
    return result

def print_free(entry):
    result = ''
    if 'url' in entry:
        result += '<a href="' + entry.url + '">'

    result += entry.text

    if 'url' in entry:
        result += '</a>'

    result += ' (' + timeperiod(entry.begin, entry.end) + ').'
    return result

##############################################################################

def read_academic():
    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/academic.xml', 'r').read())

    # transform date types
    for entry in data.scientific.memberships.pc:
        entry.begin = time.strptime(entry.date, '%d %b %Y')
        entry.end = time.strptime(entry.date, '%d %b %Y')
        entry.type = {'value': 'pc'}

    return data.scientific.memberships.pc

##############################################################################

def news():
    # add header template
    print("Generating index.html...")
    output = open('../html/index.html', 'r').read()

    # read data XML file
    xml = XML2Dict()
    data = xml.fromstring(open('../xml/news.xml', 'r').read())

    # fetch papers
    paperdata = generate_publications.init()

    past = []
    past_images = []
    past_sticky = 0

    max_entries = 6

    present = []
    future = []

    # add academic services
    everything = data.newsentries.entries.news + read_academic()

    for entry in data.newsentries.entries.news:
        entry.begin = time.strptime(entry.begin, '%d %b %Y')
        if 'end' in entry:
            entry.end = time.strptime(entry.end, '%d %b %Y')
        else:
            entry.end = entry.begin

    # sort by begin date
    everything = sorted(everything, key=lambda k: k.begin, reverse=True)

    # get sticky entries, images and sort into past and future

    for entry in everything:
        if entry.end > time.localtime():
            future.append(entry)
            continue

        if entry.begin < time.localtime():
            past.append(entry)
            if 'image' in entry:
                past_images.append([entry.image, entry.text])
            if 'sticky' in entry:
                past_sticky += 1
            continue

        present.append(entry)

    future.reverse()

    ########################################################################

    if len(future) > 0:
        output += '<h2 style="margin-top: 1em;">Soon&hellip;</h2>\n'
        output += '<ul class="news">\n'
        count = 0
        for entry in future:
            count += 1
            if count > max_entries and 'sticky' not in entry:
                continue

            output += '<li>'

            if entry.type == 'free':
                output += print_free(entry)
            if entry.type == 'visit':
                output += print_visit(entry)
            if entry.type == 'lecture':
                output += print_lecture(entry)
            if entry.type == 'venue':
                output += print_venue(entry)

            output += '</li>\n'

        output += '</ul>\n'

    ########################################################################

    if len(past) > 0:
        output += '<h2 style="margin-top: 1em;">Recently&hellip;</h2>\n'

        for img in past_images:
            output += '<img src="resources/img/' + img[0] + '" alt="' + img[1] + '" style="padding-left:10px; padding-bottom:10px; float: right;" />'

        output += '<ul class="news">\n'
        count = 0
        for entry in past:
            count += 1
            if count > (max_entries-past_sticky) and 'sticky' not in entry:
                continue

            output += '<li>'

            if entry.type == 'pc':
                output += print_pc(entry)
            if entry.type == 'free':
                output += print_free(entry)
            if entry.type == 'visit':
                output += print_visit(entry)
            if entry.type == 'lecture':
                output += print_lecture(entry)
            if entry.type == 'venue':
                output += print_venue(entry)
            if entry.type == 'paper_accepted':
                output += print_paper_accepted(entry, paperdata)

            output += '</li>\n'
        output += '</ul>\n'

    ########################################################################

    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing index.html...")
    f = open('../../index.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()

def main():
    news()

if __name__ == "__main__": main()
