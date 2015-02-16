def pyindent(text, indent=4, truncate=0):
    return ("\n").join([(indent * " " + line[:truncate] if truncate else line)
        for line in text.split("\n")])
