#!/usr/bin/python3


def safe_function(fct, *args):
    """
    simple function for excuting a certain function
    """
    try:
        res = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: "+e.__str__() + "\n")
        return None
    else:
        return res
