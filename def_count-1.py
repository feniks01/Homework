from tkinter import W


def count_words(arr):
    words_dict = {}
    for i in arr:
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return (words_dict)  


print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))


