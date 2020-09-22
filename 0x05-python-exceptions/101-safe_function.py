#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    stderr_fileno = sys.stderr
    result = 0
    try:
        resutl = fct(*args)
        return(resutl)
    except BaseException as err:
        print("Exception: {}".format(err), file=stderr_fileno)
        result = None
