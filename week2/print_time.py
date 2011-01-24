import time
import datetime

print '<html>'
print '<head><title>Print Time</title></head>'
print '<body><p>'
print "Here is the time: %s" % time.time()
print '<br />'
print "and again: %s" % datetime.datetime.now()
print '</p></body>'
print '</html>'
