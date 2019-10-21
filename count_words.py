import re


def count_words(text):
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)
    text = text.split(" ")
    my_dict = {}
    for word in text:
        try:
            my_dict[word] += 1
        except:
            my_dict[word] = 1
    return my_dict
