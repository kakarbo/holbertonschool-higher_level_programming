#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    stderr_fileno = sys.stderr
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr_fileno)
        return(False)
