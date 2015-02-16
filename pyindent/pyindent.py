def pyindent(text, indent=4, truncate=0, delim=" "):
    return ("\n").join(
        [(indent * delim + line[:truncate]
            if truncate else indent * delim + line)
                for line in text.split("\n")])
