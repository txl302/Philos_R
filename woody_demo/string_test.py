import re

value = "Yes I am ready"

detected = re.findall("ready", value)

print detected

if detected:
	print 1
	