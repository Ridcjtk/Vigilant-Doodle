
dict1 = ['bananas', 7, 'apples', 3, 'pears', 14]
dict2 = ['bananas', 3, 'apples', 6, 'grapes', 9]

#['bananas': 7, 'apples': 6, 'pears': 14, 'grapes': 9]


def merge_max_mappings(dict1, dict2):
    x = 0
    mergelist = []
    count = 0 
    compare = 1
    while x < len(dict1):
        if dict1[count] == dict2[count]:
            if dict1[compare] > dict2[compare]:
                 mergelist += [dict1[count] , dict1[compare]] 
            else:
                mergelist += [dict2[count] , dict2[compare]]

        elif dict1[count] != dict2[count]:
            mergelist += [dict1[count] , dict1[compare] , dict2[count] , dict2[compare]]

        count += 2
        compare +=2
        x += 2
    return mergelist
        


        
print(merge_max_mappings(dict1, dict2))