#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return(None)
        '''for a, b in a_dictionary.items():
            max_key = max(a_dictionary)
            if a == max_key:
                return(max_key)'''
    else:
        return(max(a_dictionary))
