fname = "README.md"
with open(fname) as f:
    for c, value in enumerate(f):
        pass

num_lines = c +1
html_string = "<!DOCTYPE html><html><body>"
html_string += "Number of lines in " + fname + " is " + str(num_lines)
html_string += "</body></html>"

doc = open("index.html", "w")
doc.write(html_string)
doc.close()