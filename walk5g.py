import os, sys, re, string
rep = string.replace

if len(sys.argv) < 3:
  print
  print "Usage: walk5g.py <regex pattern> <filespec> [flags]"
  print
  print "Flags:"
  print " /i: ignore case"
  print " /s: search in subdirectories"
  print " /m: multiline mode (affects the behavior of ^ and $)"
  print ' /d: make "." also match newlines'
  sys.exit(1)

startdir, basename = os.path.split(sys.argv[2])
flags = 0
if "/m" in sys.argv or "/M" in sys.argv: flags = flags + re.M
if "/i" in sys.argv or "/I" in sys.argv: flags = flags + re.I
if "/d" in sys.argv or "/D" in sys.argv: flags = flags + re.S

if os.path.isdir(os.path.join(basename, startdir)):
  startdir=os.path.join(basename, startdir)
  basename=""

basename = rep(rep(rep(basename, ".", "\."), "*", ".*"), "?", ".") + "$"

if basename=="$": basename=".*"
if startdir=="": startdir = os.getcwd()

arg1 = re.compile(sys.argv[1], flags)
arg2 = re.compile(basename)

print startdir
print basename#########



def dopath(dir, files):
  for file in files:
    
     path = dir + "\\" + file
     if os.path.isfile(path):
       pos = 0
       if arg2.match(file):

         print path ###################################3


         text = open(path, "rb").read()
         
         found = arg1.search(text)
         if found:
           print "---"
           print dir + "\\" + file
           while found:
             print "-"
             p = string.rfind(text, "\n", 0, found.start())
             p = string.rfind(text, "\n", 0, p)
             if p == -1: p=0
             q = string.find(text, "\n", found.end())
             q = string.find(text, "\n", q+1)
             print text[p:q]
             pos = found.end()
             found = arg1.search(text,pos)

def visit(arg, dir, files):
  dopath(dir, files)

z = "blah"
if "/s" in sys.argv or "/S" in sys.argv:
  os.path.walk(startdir, visit, z)
else:
  dopath(startdir, os.listdir(startdir))

