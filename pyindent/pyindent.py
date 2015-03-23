def pyindent(text, amt=4, truncate=0, delim=" "):
    return ("\n").join(
        [(amt * delim + line[:truncate]
            if truncate else amt * delim + line)
                for line in text.split("\n")])

def pydedent(t, amt=4, delim=" "): 
    return "\n".join([l[amt:] if l.startswith(delim * amt) else l
        for l in t.split("\n")])

