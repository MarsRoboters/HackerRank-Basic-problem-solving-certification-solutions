def stringAnagram(dictionary, query):
    #write your code here
    
    final = []
    for i in range(len(query)):
        counter = 0
        for j in range(len(dictionary)):
            
            s1 = sorted(query[i])
            s2 = sorted(dictionary[j])
            
            if s1 == s2:
                counter = counter + 1
                #print(s1)
        final.append(counter)
    
    return final
            
            
    
if __name__ == '__main__':
    
    dictionary = ['hack','a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
    query      = ['a', 'nark', 'bs', 'hack', 'stair']

    final = stringAnagram(dictionary, query)
    print(final)
