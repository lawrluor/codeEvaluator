from bs4 import BeautifulSoup

# 3. Helper for character encoding
def find_char_encoding(content):
	tags = content.find_all("meta")
	for tag in tags:
		if tag.get("charset"):
			return
	print("charset attribute not found.")

# 2. Each image needs an alt tag
def check_img_tags(content):
	tags = content.find_all("img")
	for tag in tags:
		if not tag.get("alt"):
			print("Each img needs an alt tag.")

# 1. No block tags inside inline tags
def check_inline_tags(content):
	block_tags = [
    "address", "article", "aside", "blockquote", "canvas", "dd", "div", "dl",
    "dt", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3",
    "h4", "h5", "h6", "header", "hr", "li", "main", "nav", "noscript", "ol", "p",
    "pre", "section", "table", "tfoot", "ul", "video"
	]

	inline_tags = ['a', 'abbr', 'acronym', 'b', 'bdo', 'big', 'br', 'button', 'cite', 'code', 'dfn', 'em', 'i', 'img', 'input', 'kbd', 'label', 'map', 'object', 'output', 'q', 'samp', 'script', 'select', 'small', 'span', 'strong', 'sub', 'sup', 'textarea', 'time', 'tt', 'var']

	for tag in inline_tags:
		inline_elements = content.find_all(tag)
		for inline_element in inline_elements:
			for child in inline_element.children:
				# Note: Most inline tags might not have children
				# print("Parent: ", inline_element.name, "Child:", child.name)
				if child.name and child.name in block_tags:  # note that children only refers to direct children.
					print("No block elements inside inline elements.")
					return

file_to_parse = "testFiles/homepage.html.txt"

with open(file_to_parse) as f:
	content = BeautifulSoup(f, 'html.parser')
	# print(content.prettify())
	# print(content.head)

	 # Minified and remove all whitespace
	raw_content = str(content).strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\v', '').replace('\r', '').replace('\f', '')

	# 1. Check No block elements inside inline tags
	check_inline_tags(content)

	# 2. Check image alt tags
	check_img_tags(content)

	# 3. Missing character encoding
	find_char_encoding(content)

	# 4.
	# <DOCTYPE> is transformed into a single string: html
	# TODO: make case insensitive using re
	if not ('<!DOCTYPE' in raw_content or '<!doctype' in raw_content):
		print("Doctype not found")

	# 5. No using adjacent/multiple line breaks
	# Siblings doesn't work for some reason
	# br_tags = content.find_all("br")
	# for i, tag in enumerate(br_tags):
	# 		next_sibling = tag.next_sibling
			# print(tag.name, next_sibling.name)

	if '<br/><br/>' in raw_content or '<br/><br>' in raw_content or '<br><br/>' in raw_content or '<br><br>' in raw_content:
		print("No multiple <br> tags in a row.")

	if not content.head:
		print("No <head> tag found.")

	if content.b or content.i:
		print("Don't use the <b> tag or the <i> tag")
