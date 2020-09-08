#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx == "-":
            return(None)
        elif idx > 5:
            return(None)
        else:
            if i == idx:
                return(my_list[i])
