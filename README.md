Usage: walk5g.py &lt;regex pattern> &lt;filespec> [flags]

Flags:
 /i: ignore case
 /s: search in subdirectories
 /m: multiline mode (affects the behavior of ^ and $)
 /d: make "." also match newlines

I don't remember if this program actually works. I guess it does because I apparently made 10 revisions of it.

I don't know why you'd need this, since grep and findstr alread do the same thing and more (and there are greps available for Windows). I guess it's useful if you want to customize the behavior in some way that grep/findstr's command-line parameters don't allow. I probably made this program because at the time I couldn't find a grep for Windows that has option to recurse subdirectories. Tim Charron's win32 port does it: http://www.interlog.com/~tcharron/grep.html






