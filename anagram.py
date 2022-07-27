import string

def is_anagram(fst_word, snd_word):
    fst_word = fst_word.lower()
    snd_word = snd_word.lower()
    if(len(fst_word) == len(snd_word)):
        sorted_fst_word = sorted(fst_word)
        sorted_snd_word = sorted(snd_word)
        if(sorted_fst_word == sorted_snd_word):
            print(fst_word + " and " + snd_word + "are anagram")
        else:
            print(fst_word + " and " + snd_word + " are not anagram ")
    
is_anagram("BRADE", "BeaRD")
is_anagram("TOP_CODER", "COTO_PRODE")
