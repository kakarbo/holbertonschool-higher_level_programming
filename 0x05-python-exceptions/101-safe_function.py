#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    stderr_fileno = sys.stderr
    result = 5.0
    try:
        resutl = fct(args[0], args[1])
    except BaseException as err:
        print("Exception: {}".format(err), file=stderr_fileno)
        return(None)
    return(result)
