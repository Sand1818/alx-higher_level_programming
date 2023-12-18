#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        import sys
        s = fct(*args)
    except Exception as err:
        s = None
        print("Exception:", err, file=sys.stderr)
    return s
