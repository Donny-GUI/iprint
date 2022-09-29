from pprint import pprint

term = '\033['
colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white' ]
texts = ['', 'bold', 'dim', 'italic', 'underline', 'blink', 'doubleblink', 'crossout']

themes = []
styles = {}
styles['black'] = f"{term}30m"
styles['red'] = f"{term}31m"
styles['green'] = f"{term}32m"
styles['yellow'] = f"{term}33m"
styles['blue'] = f"{term}34m"
styles['cyan'] = f"{term}36m"
styles['magenta'] = f"{term}35m"
styles['white'] = f"{term}37m"
styles['bgblack'] = f"{term}40m"
styles['bgred'] = f"{term}41m"
styles['bggreen'] = f"{term}42m"
styles['bgyellow'] = f"{term}43m"
styles['bgblue'] = f"{term}44m"
styles['bgcyan'] = f"{term}46m"
styles['bgmagenta'] = f"{term}45m"
styles['bgwhite'] = f"{term}47m"

for idx, x in enumerate(colors):
	for index, color in enumerate(colors):
		styles[f'{x} on {color}'] = f"{term}0;3{idx};4{index}m"
		new_theme = f"{x} on {color}"
		themes.append(new_theme)
		for dex, text in enumerate(texts):
			if text == "":
				continue
			styled_theme = f"{text} {new_theme}"
			themes.append(styled_theme)
			styles[f'{styled_theme}'] = f"{term}{dex};3{idx};4{index}m"
for index, text in enumerate(texts):
	xx = text
	for idx, x in enumerate(colors):
		if text == "":
			continue
		xxx = f"{xx} {x}"
		themes.append(xxx)
		styles[f'{xxx}'] = f"{term}{index};3{idx}m"


class Inline(str):

	def inline(self, end=None):
		
		string = str(Inline(self))
		start_index = 0
		current_tag = ""
		matches = []
		the_string = []
		for index, value in enumerate(self):
			current_tag = ''
			current_string = ''
			char = ''
			if value == '<':
				my_it = iter(self[int(index):])
				while (char != ">"):
					try:
						char = next(my_it)
						current_tag = current_tag + char
						if char == ">":
							if current_tag[1] == "/":
								my_tag = match(current_tag, end=True)
							else:
								my_tag = match(current_tag)
							the_string.append(my_tag)
							char = ""
							break
					except:
						char = ""
						break
			if value == '>':
				my_it = iter(self[int(index):])
				while(char != "<"):
					try:
						char = next(my_it)
						current_string = current_string + char
						if char == "<":
							char = ""
							break
					except:
						char = ""
						break
				if current_string.startswith(">"):
					current_string = current_string[1:-1]
					the_string.append(current_string)
					
		try:
			my_string = "".join(the_string)
			_end = end
			if _end == None:
				print(my_string)
			else:
				print(my_string, end=_end)
		except:
			print(the_string)

iprint = Inline.inline



def match(tag, end=False):
	tag = tag[1:-1]
	if end == False:
		for key, value in styles.items():
			if tag == key:
				return value
	else:
		return "\033[0m"

def inline(self, end=None):
		string = self
		start_index = 0
		current_tag = ""
		matches = []
		the_string = []
		for index, value in enumerate(self):
			current_tag = ''
			current_string = ''
			char = ''
			if value == '<':
				my_it = iter(self[int(index):])
				while (char != ">"):
					try:
						char = next(my_it)
						current_tag = current_tag + char
						if char == ">":
							if current_tag[1] == "/":
								my_tag = match(current_tag, end=True)
							else:
								my_tag = match(current_tag)
							the_string.append(my_tag)
							char = ""
							break
					except:
						char = ""
						break
			if value == '>':
				my_it = iter(self[int(index):])
				while(char != "<"):
					try:
						char = next(my_it)
						current_string = current_string + char
						if char == "<":
							char = ""
							break
					except:
						char = ""
						break
				if current_string.startswith(">"):
					current_string = current_string[1:-1]
					the_string.append(current_string)
					
		try:
			my_string = "".join(the_string)
			_end = end
			if _end == None:
				print(my_string)
			else:
				print(my_string, end=_end)
		except:
			print(the_string)


class Examples:

	def display():
		longest = 30
		for theme in themes:
			length = int(len(theme))
			pad = longest - length
			padding = " " * pad
			print(f"theme: {theme} {padding}",end="")
			inline(f"<{theme}> Hi Mom! </{theme}>")

	def example():
		print("""\033[36miprint\033[0m("\033[33m<bold yellow> ello mum </bold yellow>\033[0m")""")
		print("produces this...")
		iprint("<bold yellow> ello mum </bold yellow>")
		print("""\033[36minline\033[0m("\033[33m<green> hi guido </green>\033[0m")""")
		print("produces this...")
		inline("<green> hi guido </green>")

display_themes = Examples.display
iprint_example = Examples.example




