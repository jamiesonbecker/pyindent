# pyindent
Super simple indent function for python that indents existing text

It doesn't get much simpler:

    from pyindent import indent
    from pprint import pformat
    
    product = {
        "id": 1,
        "name": "A blue door This could be a really long line as well and it could optionally be truncated (handy for output on screen)",
        "price": 12.50,
        "tags": ["home", "blue"]
    }
    
    print indent(pformat(product), indent=4, truncate=80)
    
    # produces nicely indented output, with long lines truncated as needed.

