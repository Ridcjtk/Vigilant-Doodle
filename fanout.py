def difference_fanout(beans, fanout):
    endlist = []
    for x, value in enumerate(beans):
      newlist = []
      for val in beans[x+1: x+4]:
        newlist.append(val- value)

      endlist.append(newlist)

    return endlist



    
result = difference_fanout([3, 2, 4, 6, 1], 3)
print(result)