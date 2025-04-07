def calc_num_of_words(text):
    num = text.split()
    return len(num)

def count_characters(text):
    char_dic = {}
    lower = text.lower()
    for word in lower:
        if word not in char_dic:
            char_dic[word]= 1
        else:
            char_dic[word] += 1
    return char_dic

def sort_on(e):
    return e["value"]

def sort_dict(dict):
    order = []
    for i in dict:
        new = {}
        new["key"] = i
        new["value"] = dict[i]
        order.append(new)
    order.sort(reverse=True, key=sort_on)
    return order