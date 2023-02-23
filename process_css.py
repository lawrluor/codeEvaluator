import re
from cssutils import CSSParser

parser = CSSParser()
sheet = parser.parseFile('testFiles/style.css', 'ascii')
cssText = str(sheet.cssText)

# 1. No universal selector allowed
if '*' in cssText:
	print("No using universal selector *")

# 2. No !important
if '!important' in cssText:
	print("No using !important")

# 3. Values of 0 should not have units
# zeros = [match.start() for match in re.finditer('0', cssText)]
# for i in zeros:  # list of indices
# 	if cssText[i+1] != ';' or cssText[i+1] != ' ' or cssText[i+1] != '\n':
# 		print("Values of 0 should not have units assigned to them")

css_units = ['em', 'ex', 'ch', 'rem', 'vw', 'vh', 'vmin', 'vmax', 'cm', 'mm', 'in', 'pt', 'pc', 'px', 'deg', 'grad', 'rad', 'turn', 's', 'ms', 'Hz', 'kHz', '%', 'fr', 'dpi', 'dpcm', 'dppx']
css_units_prefixed = ['0'+unit for unit in css_units]
for unit in css_units_prefixed:
	if unit in cssText:
		print("Values of 0 should not have units assigned to them")

# 4. No px units allowed
if 'px;' in cssText:
	print("No using px units")
