from enum import Enum
from math import floor, ceil


result = ""
lines = []
output_fn_suffix = "_formatted"
supported_exts= [".c", ".h"]
ext = ""
output_fn = ""
fn = "C:/a-dubs/personal/github/py-code-tools/input.c"
line_wrap = 120
li = 0
max_adj_divs = 3

class Insert(Enum):
    PREPEND = -1
    REPLACE = 0
    APPEND = 1

"""
KERWORDS / DEFINITIONS:

divider:
/////////////////////////////////

header: 
////////// Header Text //////////



"""

def add_div(li, insert):
    global lines
    if insert == Insert.PREPEND:
        lines = lines[:li] + [line_wrap * '/' + '\n'] + lines[li:]
        li += 1
    elif insert == Insert.REPLACE:
        lines[li] = [line_wrap * '/' + '\n'] 
    elif insert == Insert.APPEND:
        lines = lines[:li+1] + [line_wrap * '/' + '\n']
    else:
        print("INVALID INSERT LOCATION GIVEN TO add_div()")
        exit()
    return li    


# ci = column index of final character
def add_trailing_div(li, spacing = 1):
    global lines
    lines[li] += lines[li].rstrip() + (" " * spacing) +  ("/" * (line_wrap - len(lines[li]) - spacing))
    


def format_header(li, spacing = 2):
    global lines
    lines[li] = (" " * spacing) + strip(strip(lines[li])[2:-2]) + (" " * spacing)
    ll = len(lines[li])
    lines[li] = ("/" * floor((line_wrap - ll) * 0.5)) + lines[li] + ("/" * ceil((line_wrap - ll) * 0.5))



with open() as file:
    for line in file:
        lines.append(line)
        print(line)
    
ext = fn[fn.rfind("."):]
output_fn = fn[:fn.find(ext)] + output_fn_suffix + ext


for li in range(len(lines)):
    line = lines[li]    # current line alias
    sl = line.split()    # split line alias 

    # dividers need inserted before this comment line
    

    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # divders need inserted after this comment line


    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # isolated dividers need inserted 
    if (len(sl) == 1) and ("///" in sl[0]):
        num_divs = len(sl)
        # replace this isolated '///' divider macro with a divider
        add_div(li, Insert.REPLACE) 
    
    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # format a header
    if (len(sl) >= 3) and ('//' == sl[0]) and ('//' == sl[-1]):
        format_header(li)
        
    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # inline comment 
    if ("//" != sl[0]) and ("//" != sl[0]):
        pass

    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # extend '/'s to col 0
    if "//<" == sl[0]:
        pass

    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # extend '/'s to EOL
    if "//>" == sl[-1]:
        pass

    line, sl = lines[li] , line.split()   # update current line alias (line) and split line alias (sl)
    # function needs dividers appended
    if "}/" in line:
        brackets_unclosed = 0
        for li2 in range(li,len(lines)):
            line2 = lines[li2]
            if "{" in line2:
                brackets_unclosed += 1
            if "}" in line2:
                if brackets_unclosed == 0:
                    func
                    break
                else:
                    brackets_unclosed -= 1
