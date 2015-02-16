# pyindent
Super simple indent function for python that indents existing text

It doesn't get much simpler:

    from pyindent import pyindent
    from pprint import pformat
    
    product = {
        "id": 1,
        "name": "A blue door This could be a really long line as well and it could optionally be truncated (handy for output on screen)",
        "price": 12.50,
        "tags": ["home", "blue"]
    }
    
    print pyindent(pformat(product), indent=4, truncate=80)
    
    # produces nicely indented output, with long lines truncated as needed.

Read all two lines of the source code to see what it does. ;)

If you need something bigger, check out
https://github.com/scottt/scottt-bin/blob/master/pyindent
