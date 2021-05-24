""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5


def lines_from_file(path):
    doc = open(path, "r")
    if doc.readable():
        lines = doc.readlines()
        lines = [line.strip() for line in lines]
    else:
        return "Error. Not readable object"
    return lines


def new_sample(path, i):
    lines = lines_from_file(path)
    paragraph = lines[i]
    return paragraph


def analyze(sample_paragraph, typed_string, start_time, end_time):
    def words_per_minute(typed, start, end):
        time_gap = abs(start - end)
        string_size = len(typed)
        words_per_minute = (string_size/5) / (time_gap/60)
        return words_per_minute

    def accuracy_percentage(sample, typed):
        count = 0
        sample = sample.split()
        typed = typed.split()
        if len(sample) == 0 or len(typed) == 0:
            return 0.0
        if len(sample) > len(typed):
            size = len(typed)
        else:
            size = len(sample)
        for i in range(size):
            if typed[i] == sample[i]:
                count += 1
        return count / size * 100

    words_p_m = words_per_minute(typed_string, start_time, end_time)
    accuracy = accuracy_percentage(sample_paragraph, typed_string)
    return [words_p_m, accuracy]


def pig_latin(word_to_convert):
    import re
    regex = "^[^aeiou]+"
    match_obj = re.search(regex, word_to_convert)
    if bool(match_obj):
        matched_str = match_obj.group()
        word_to_convert = re.sub(matched_str, "", word_to_convert)
        word_to_convert = word_to_convert + matched_str + "ay"
    else:
        word_to_convert = word_to_convert + "way"
    return word_to_convert


def autocorrect(user_input, words_list, score_function):
    def make_dictionary():
        score_dictionary = {}
        for word in words_list:
            dif = score_function(user_input, word)
            score_dictionary[word] = dif
        print(score_dictionary["gomez"])
        print(score_dictionary["gore"])
        return score_dictionary

    if user_input in words_list:
        return user_input
    else:
        score_dictionary = make_dictionary()
        return min(score_dictionary, key=lambda x: score_dictionary[x])


def swap_score(word_1, word_2):
    if word_1 == "":
        return 0
    elif word_2 == "":
        return len(word_1)
    else:
        if word_1[0] == word_2[0]:
            return 0 + swap_score(word_1[1:], word_2[1:])
        else:
            return 1 + swap_score(word_1[1:], word_2[1:])

        # END Q1-5

        # Question 6


words_list = lines_from_file("./data/words.txt")
print(autocorrect("goje", words_list, swap_score))


def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2.
    >>> score_function("tesng", "testing")
    2
    >>> score_function("rlogcul", "logical")
    3
    >>> score_function("misspelled", "spelling")
    6
    """

    if word1 == "" or word2 == "":  # Fill in the condition
        # BEGIN Q6
        if (word1):
            return len(word1)
        if (word2):
            return len(word2)
        return 0
        # END Q6

    elif word1[0] == word2[0]:  # Feel free to remove or add additional cases
        # BEGIN Q6
        return score_function(word1[1:], word2[1:])
        # END Q6

    else:
        # Fill in these lines
        add_char = score_function(word2[0] + word1, word2)
        remove_char = score_function(word1[1:], word2)
        substitute_char = score_function(word2[0] + word1[1:], word2)
        # BEGIN Q6
        return 1 + min(add_char, remove_char, substitute_char)
        # END Q6


KEY_DISTANCES = get_key_distances()
# BEGIN Q7-8


def score_function_accurate(word1, word2):
    if word1 == "":
        if (word2):
            return float(len(word2))
        return 0.0

    elif word2 == "":
        if (word1):
            return float(len(word1))
        return 0.0

    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])

    else:
        add_char = 1 + score_function_accurate(word2[0] + word1, word2)
        remove_char = 1 + score_function_accurate(word1[1:], word2)
        substitute_char = 1 + score_function_accurate(
            word2[0] + word1[1:], word2) + KEY_DISTANCES[word1[0], word2[0]]
        return min(add_char, remove_char, substitute_char)


print(score_function_accurate("tesng", "testing"))
print(score_function_accurate("rlogculu", "logicala"))
print(score_function_accurate("misspelled", "spelling"))


# print(KEY_DISTANCES["u", "a"])
# print(KEY_DISTANCES["d", "g"])
# print(KEY_DISTANCES["d", "g"]+KEY_DISTANCES["e", "n"])
# print(KEY_DISTANCES["d", "g"]+KEY_DISTANCES["e", "n"]+6)
memo_dict = {}


def score_function_final(word1, word2):
    global memo_dict
    value = 0
    if word1 in memo_dict.keys() and word2 in memo_dict[word1].keys():
        value = memo_dict[word1][word2]
    elif word2 in memo_dict.keys() and word1 in memo_dict[word2].keys():
        value = memo_dict[word2][word1]
    else:
        value = score_function_accurate(word1, word2)

        memo_dict[word1] = {word2: value}

    print(value)
    return value


    # END Q7-8
print("first: " + str(score_function_final("cuetara", "cuotoro")))
print(score_function_final("cuetara", "cuotore"))
print(score_function_final("amaranto", "amaramstsa"))
