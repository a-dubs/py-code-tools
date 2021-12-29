# py-code-tools
First project: Auto comment formatting for common programming languages I use


## Auto-Formatting Macros 

C/C++, Javascript Comment Formatting:  
'//' = single line comment / inline comment  
n * '/' + '//' = single line comment with n # of dividers above(must be first non-whitespace char on its line)  
n * '/' + '///' = n+1 # horizontal divider lines  
n * '/' + '//' + text inside + '//' + m * '/' = header/title comment with n # of dividers before and m # of dividers after  
//| Hello means extend '/'s all the way to col 0  
'}' + n * '/' after function header will put n dividers at end of function  
