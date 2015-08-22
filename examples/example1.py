import sys, os
from cmdline import Option, FileOption, Commandline


options = [
    Option( "-s", "string", "lalala", "some string"),
    Option( "-r", "rvec", [1.,2.,-3.], "some list with floats"),
    Option( "-b", "bool", True, "bool"),
    Option( "-c", "svec", ["red","blue","green"], "vector of strings")
    ]

files = [
    FileOption("-i", "r/m",["doc","docx"],"xx.doc", "input word files"),
    FileOption("-excel", "r/m",["xls","xlsx"],"a.xlsx", "one or more excel files"),
    FileOption("-o", "w",["csv"],"out.csv", "outfile in csv format")
    ]

help_text = ['does a lot of useful stuff',
             'most of the time'
             ]

cmdl = Commandline( sys.argv, options = options, fileoptions = files, program_desc = help_text, check_for_existing_files = False, verbose = True)


print cmdl['-i']
print cmdl['-excel']
