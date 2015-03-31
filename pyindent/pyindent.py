from textwrap import wrap

def pyindent(text, amt=4, truncate=0, delim=" ", linestart="", maxwidth=0):
    return linestart + ("\n" + linestart).join(
        [(amt * delim + line[:truncate]
            if truncate else amt * delim + line)
                for line in
                    [ l1 for l2 in [
                            (wrap(line, maxwidth) if maxwidth else [line])
                            for line in 
                            text.split("\n")]
                    for l1 in l2 ]
                ])

def pydedent(t, amt=4, delim=" "): 
    return "\n".join([l[amt:] if l.startswith(delim * amt) else l
        for l in t.split("\n")])

