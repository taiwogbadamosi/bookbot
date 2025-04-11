def get_num_words(string):
    arr = string.split()
    return len(arr)
def get_num_chars(string):
    string = string.lower()
    h1 = {}
    for i in range(len(string)):
        if string[i] in h1:
            h1[string[i]] += 1
        else:
            h1[string[i]] = 1
    return h1
def sort_dict(d):
    arr = []
    for k in d:
        arr.append([k, d[k]])
    arr.sort(key=lambda x:x[1] , reverse=True)
    arr = [{x[0]: x[1]} for x in arr]
    return arr