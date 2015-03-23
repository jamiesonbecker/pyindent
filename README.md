# pyindent
Super simple indent function for python that indents existing text

    pip install pyindent

It doesn't get much simpler:

~~~python
    from pyindent import pyindent
    from pprint import pformat
    
    product = {
        "id": 1,
        "name": "A blue door This could be a really long line as well and it could optionally be truncated (handy for output on screen)",
        "price": 12.50,
        "tags": ["home", "blue"]
    }
    
    # produces nicely indented output, with long lines truncated as needed.
    # handy for reading voluminous output from a data store
    print pyindent(pformat(product), indent=4, truncate=60)
        {'id': 1,
         'name': 'A blue door This could be a really long line as we
         'price': 12.5,
         'tags': ['home', 'blue']}

    pydedent(pformat(product), amt=4, delim=" ") will have the opposite effect.

~~~

Read all four lines of the source code to see what it does.

If you need something fancier, check out
https://github.com/scottt/scottt-bin/blob/master/pyindent
