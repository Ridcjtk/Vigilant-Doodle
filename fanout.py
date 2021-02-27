def difference_fanout(list, fanout):
    newlist = []
    first = 0
    while first < len(list):
     for val in list[first+1 : ]:
       newlist.append(val-fanout)
       first+1
    return newlist
