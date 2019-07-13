#练习
def break_words(stuff):
    '''分离字符串'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''对列表排序'''
    return sorted(words)

def print_first_word(words):
    '''弹出弹出分离成列表的words的第一个元素'''
    first_word = words.pop(0)
    print(first_word)

def print_last_word(words):
    '''打印最后一个元素'''
    last_word = words.pop(-1)
    print(last_word)

def sort_sentence(sentence):
    '''分离'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''直接打印第一个和最后一个元素'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    '''排序后打印第一个和最后一个元素'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

