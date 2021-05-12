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
    if user_input in words_list:
        return user_input
    else:

        # END Q1-5

        # Question 6


def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________:  # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________:  # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________
        substitute_char = ______________
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6


KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
