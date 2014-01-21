import time

# returns nice representation of time period
def timeperiod(begin, end):
    output = ''
    
    if begin == end:
        # only one date
        output += time.strftime('%B ', begin) + str(begin.tm_mday) + time.strftime(', %Y', begin)
    else:
        if begin.tm_year == end.tm_year:
            if begin.tm_mon == end.tm_mon:
                # same year and month - only have period in days
                output += time.strftime('%B ', begin) + str(begin.tm_mday) + '&ndash;' + str(end.tm_mday) + time.strftime(', %Y', end)
            else:
                # same year - only have period in months
                output += time.strftime('%B ', begin) + str(begin.tm_mday) + '&ndash;' + time.strftime('%B ', end) + str(end.tm_mday) + time.strftime(', %Y', end)
        else:
            # completely different dates
            output += time.strftime('%B ', begin) + str(begin.tm_mday) + time.strftime(', %Y', begin) + '&ndash;' + time.strftime('%B ', end) + str(end.tm_mday) + time.strftime(', %Y', end)

    return output

# creater a page footer
def footer():
    now = time.localtime()
#    result = '<footer><script src="http://static.getclicky.com/js" type="text/javascript"></script> <script type="text/javascript">try{ clicky.init(66375501); }catch(err){}</script> <noscript><img alt="Clicky" width="1" height="1" src="http://in.getclicky.com/66375501ns.gif" /></noscript>'
    result = '<footer>'
    result += '''<script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
    </script>
    <script type="text/javascript">
    try{ 
    var pageTracker = _gat._getTracker("UA-21282237-2");
    pageTracker._trackPageview();
    } catch(err) {} 
    </script>'''
    result += 'Last updated <time datetime="' + time.strftime('%Y-%m-%d', now) + '" pubdate="pubdate">' + time.strftime('%B ', now) + str(now.tm_mday) + time.strftime(', %Y', now) + '</time>.</footer>'
    return result

def placelink(place):
    result = '<a class="info" href="http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=berlin&aq=&ie=UTF8&hq=&hnear=' + place.replace(" ", "+") + '&z=10&iwloc=A">' + place
    result += '<span><img src="http://maps.google.com/maps/api/staticmap?center='
    result += place.replace(' ', '+')
    result += '&zoom=9&size=400x200&sensor=false"></span></a>'
    return result
