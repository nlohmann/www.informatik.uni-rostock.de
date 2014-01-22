#!/usr/bin/env python3

import bibtex2xml
from xml2dict import XML2Dict
import time
from utils import footer
import os

###

def pdf_link(entry, id):
    pub_path = os.path.abspath('../../publications')
    if os.path.exists(pub_path + '/' + id + '.pdf'):
        return '<a class="icon" href="publications/' + id + '.pdf"></a>'
    
    if 'pdf' in entry:
        return '<a class="icon" href="' + entry.pdf.value + '"></a>'
    else:
        return ''

def pdf_iframe(entry, id):
    pub_path = os.path.abspath('../../publications')
    if os.path.exists(pub_path + '/' + id + '.pdf'):
        return '<iframe src="http://docs.google.com/gview?url=http://www.informatik.uni-rostock.de/~nl/publications/' + id + '.pdf&embedded=true" style="width:700px; height:1000px;" frameborder="0"></iframe>'

    if 'pdf' in entry:
        return '<iframe src="http://docs.google.com/gview?url=' + entry.pdf.value + '&embedded=true" style="width:700px; height:1000px;" frameborder="0"></iframe>'
    else:
        return ''

def entrybyname(id, data):
    for entry in data.file.entry:
        if entry.id == id:
            return entry


def formatentry(entry):
    if 'proceedings' in entry:
        return print_proceedings(entry.proceedings, entry.id)
    if 'inproceedings' in entry:
        return print_inproceedings(entry.inproceedings, entry.id)
    if 'phdthesis' in entry:
        return print_thesis(entry.phdthesis, 'PhD thesis', entry.id)
    if 'mastersthesis' in entry:
        return print_thesis(entry.mastersthesis, "Master's thesis", entry.id)
    if 'techreport' in entry:
        return print_techreport(entry.techreport, entry.id)
    if 'article' in entry:
        return print_article(entry.article, entry.id)
    if 'inbook' in entry:
        return print_inbook(entry.inbook, entry.id)
    else:
        print('unknown')


def print_techreport(entry, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.title.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">by ' + print_author(entry.author) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += '<p>Appeared as technical report at ' + entry.institution.value
    if 'address' in entry:
        output += ' in ' + entry.address.value
    output += '.</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.title.value))
    f.close()


    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_author(entry.author) + '. '
#    result += '<strong>' + entry.title.value + '</strong>. '
    result += '<strong><a href="publications/' + id + '.html">' + entry.title.value + '</a></strong>. '

    # type
    result += entry.type.value

    # volume and number
    if 'number' in entry:
        result += ' ' + entry.number.value

    # institution and address
    if 'institution' in entry:
        result += ', ' + entry.institution.value
    if 'address' in entry:
        result += ', ' + entry.address.value

    result += ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note

    result += '</li>'
    return result


def print_thesis(entry, thesistype, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.title.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">by ' + print_author(entry.author) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += '<p>' + thesistype + ' submitted to ' + entry.school.value
    if 'address' in entry:
        output += ' in ' + entry.address.value
    output += '.</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.title.value))
    f.close()



    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_author(entry.author) + '. '
    #result += '<strong>' + entry.title.value + '</strong>. '
    result += '<strong><a href="publications/' + id + '.html">' + entry.title.value + '</a></strong>. '

    # type
    if 'type' in entry:
        result += entry.type.value + '. '
    else:
        result += thesistype + '. '

    # school and address
    if 'school' in entry:
        result += entry.school.value
    if 'address' in entry:
        result += ', ' + entry.address.value
    result += ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note

    result += '</li>'
    return result


def print_article(entry, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.title.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">by ' + print_author(entry.author) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += '<p>Appeared in ' + entry.journal.value + '.</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.title.value))
    f.close()


    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_author(entry.author) + '. '
    result += '<strong><a href="publications/' + id + '.html">' + entry.title.value + '</a></strong>. '
    #result += '<strong>' + entry.title.value + '</strong>. '

    # journal
    result += '<em>' + entry.journal.value + '</em>'
    result += ', '

    # volume and number
    if 'volume' in entry:
        result += entry.volume.value
        if 'number' in entry:
            result += '(' + entry.number.value + ')'

    # pages
    if 'pages' in entry:
        if 'volume' in entry:
            result += ':' + entry.pages.value.replace("-", "&ndash;")
        else:
            result += entry.pages.value.replace("-", "&ndash;")

    if 'pages' in entry or 'volume' in entry:
        result += ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note.value

    result += '</li>'
    return result



def print_inbook(entry, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.chapter.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">by ' + print_author(entry.author) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += '<p>Appeared as chapter in ' + entry.title.value + '.</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.chapter.value))
    f.close()
    
    
    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_author(entry.author) + '. '
    result += '<strong><a href="publications/' + id + '.html">' + entry.chapter.value + '</a></strong>. In '

    # editors and booktitle
    if 'editor' in entry:
        result += print_editor(entry.editor) + ', '
    result += '<em>' + entry.title.value + '</em>'

    result += ', '

    # pages
    if 'pages' in entry:
        result += 'pages ' + entry.pages.value.replace("-", "&ndash;") + ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # publisher
    if 'publisher' in entry:
        result += ' ' + entry.publisher.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note.value

    result += '</li>'
    return result



def print_proceedings(entry, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.title.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">edited by ' + print_author(entry.editor) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.title.value))
    f.close()


    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_editor(entry.editor) + '. '
    #result += '<strong>' + entry.title.value + '</strong>'
    result += '<strong><a href="publications/' + id + '.html">' + entry.title.value + '</a></strong>'

    # volume and series
    if 'volume' in entry:
        result += ', volume ' + entry.volume.value + ' of '
    else:
        result += ', '
    if 'series' in entry:
        result += '<em>' + entry.series.value + '</em>'

    result += ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # publisher
    if 'publisher' in entry:
        result += ' ' + entry.publisher.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note.value

    result += '</li>'
    return result


def print_inproceedings(entry, id):
    output = open('../html/paper.html', 'r').read()
    f = open('../../publications/' + id + '.html', 'w')

    output += '<h2 class="first">' + entry.title.value.replace(":", ":<br>") + '</h2>'

    output += '<h3 style="margin-top: 1em;">by ' + print_author(entry.author) + '</h3>'
    
    if 'abstract' in entry:
        output += '<p style="margin-top: 1.5em;"><strong>Abstract.</strong> ' + entry.abstract.value + '</p>'

    output += '<p>Appeared as '

    if 'pubtype' in entry and entry.pubtype.value == 'workshop' and (not 'pubreviewed' in entry or entry.pubreviewed.value == 'no'):
        output += 'unreviewed '
    else:
        output += 'peer-reviewed '

    if 'pubtype' in entry and entry.pubtype.value == 'workshop':
        output += 'workshop paper'
    else:
        output += 'conference paper'

    output += ' in ' + entry.booktitle.value + '.</p>'

    output += pdf_iframe(entry, id)

    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; ").replace("%%PAPERTITLE%%", entry.title.value))
    f.close()
    
    
    result = '<li id="' + id + '">'

    # PDF
    result += pdf_link(entry, id)

    # author and title
    result += print_author(entry.author) + '. '
    result += '<strong><a href="publications/' + id + '.html">' + entry.title.value + '</a></strong>. In '

    # editors and booktitle
    if 'editor' in entry:
        result += print_editor(entry.editor) + ', '
    result += '<em>' + entry.booktitle.value + '</em>'

    # volume and series
    if 'series' in entry and not 'volume' in entry:
            result += ', '

    if 'volume' in entry:
        result += ', volume ' + entry.volume.value + ' of '
    if 'series' in entry:
        result += '<em>' + entry.series.value + '</em>'

    result += ', '

    # pages
    if 'pages' in entry:
        result += 'pages ' + entry.pages.value.replace("-", "&ndash;") + ', '

    # month and year
    if 'month' in entry:
        result += entry.month.value + ' '
    result += entry.year.value + '.'

    # publisher
    if 'publisher' in entry:
        result += ' ' + entry.publisher.value + '.'

    # note
    if 'note' in entry:
        result += ' ' + entry.note.value

    result += '</li>'
    return result


def print_author(entry):
    if 'person' in entry:
        result = ''
        authors = 0
        for x in entry.person:
            authors += 1
            if authors == len(entry.person):
                if authors > 2:
                    result += ','
                result += ' and '
            else:
                if authors > 1:
                    result += ', '
            result = result + x.value
        return result
    else:
        return entry.value


def print_editor(entry):
    result = print_author(entry)
    if result.find('and') != -1:
        return result + ', editors'
    else:
        return result + ', editor'


def is_reviewed(entry):
    assert('inproceedings' in entry)
    if 'pubreviewed' in entry.inproceedings and entry.inproceedings.pubreviewed.value == 'no':
        return False
    else:
        return True

from pprint import pprint

def is_workshop(entry):
    assert('inproceedings' in entry)
    if 'pubtype' in entry.inproceedings and entry.inproceedings.pubtype.value == 'workshop':
        return True
    else:
        return False


#############################################################################

def init():
    print("Reading tpp.bib...")

    filecontents_source = bibtex2xml.filehandler('../bibtex/tpp.bib')
    xml = XML2Dict()
    data = xml.fromstring(bibtex2xml.contentshandler(filecontents_source))
    return data

def main():
    # get data
    data = init()

    # add header template
    print("Generating publications.html...")
    output = open('../html/publications.html', 'r').read()

    filterauthor = 'Niels Lohmann'

    #######################
    # part 1: Proceedings #
    #######################
    output += '<h2 class="first">Proceedings</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'proceedings' in entry:
            if print_editor(entry.proceedings.editor).find(filterauthor) != -1:
                output += formatentry(entry)

    output += '</ul>\n'

    ##########################
    # part 1a: Book Chapters #
    ##########################
    output += '<h2>Book Chapters (reviewed)</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'inbook' in entry:
            if print_author(entry.inbook.author).find(filterauthor) != -1:
                output += formatentry(entry)

    output += '</ul>\n'

    ####################
    # part 2: Articles #
    ####################
    output += '<h2>Journal Articles (reviewed)</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'article' in entry:
            if print_author(entry.article.author).find(filterauthor) != -1:
                output += formatentry(entry)

    output += '</ul>\n'

    #############################
    # part 3: Conference Papers #
    #############################

    output += '<h2>Conference Papers (reviewed)</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'inproceedings' in entry:
            if print_author(entry.inproceedings.author).find(filterauthor) != -1:
                if not is_workshop(entry) and is_reviewed(entry):
                    output += formatentry(entry)

    output += '</ul>\n'

    ######################################
    # part 4: Workshop Papers (reviewed) #
    ######################################

    output += '<h2>Workshop Papers (reviewed)</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'inproceedings' in entry:
            if print_author(entry.inproceedings.author).find(filterauthor) != -1:
                if is_workshop(entry) and is_reviewed(entry):
                    output += formatentry(entry)

    output += '</ul>\n'

    ########################################
    # part 5: Workshop Papers (unreviewed) #
    ########################################

    output += '<h2>Workshop Papers (unreviewed)</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'inproceedings' in entry:
            if print_author(entry.inproceedings.author).find(filterauthor) != -1:
                if is_workshop(entry) and not is_reviewed(entry):
                    output += formatentry(entry)

    output += '</ul>\n'

    #############################
    # part 6: Technical Reports #
    #############################

    output += '<h2>Technical Reports</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'techreport' in entry:
            if print_author(entry.techreport.author).find(filterauthor) != -1:
                output += formatentry(entry)

    output += '</ul>\n'

    ##################
    # part 7: Theses #
    ##################

    output += '<h2>Theses</h2>\n'
    output += '<ul class="publications">\n'

    for entry in data.file.entry:
        if 'phdthesis' in entry:
            if print_author(entry.phdthesis.author).find(filterauthor) != -1:
                output += formatentry(entry)
        if 'mastersthesis' in entry:
            if print_author(entry.mastersthesis.author).find(filterauthor) != -1:
                output += formatentry(entry)

    output += '</ul>\n'


    # footer
    output += '</div></div>'
    output += footer()
    output += '</body></html>'

    print("Writing publications.html...")
    f = open('../../publications.html', 'w')
    f.write(output.replace(" & ", " &amp; ").replace(" - ", " &mdash; "))
    f.close()



if __name__ == "__main__": main()


#print(formatentry(entrybyname('AwadDL_2009_tr', data)))
