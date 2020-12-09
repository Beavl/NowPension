import itertools as it
import src.constants as constants

def generate_sentences(list_subject,list_predicate,list_object):
    """
        Function that returns an string with all the possible sentences that contains all the sentences in the alphabetical order that can be constructed using the provided subjects, predicates and objects as lists arguments.

        Args:
            list_subject: list. Contains the subjects of a sentence
            list_predicate: list. Contains the predicate of a sentence
            list_object: list. Contains the objects of a sentence
        Returns:
            result: sentences from the combination of the 3 lists as arguments
    """

    combined_lists = [(x, y, z) for x in sorted(list_subject) for y in sorted(list_predicate) for z in sorted(list_object)]
    result = ''
    for sentence in combined_lists:
        result=result+constants.SEPARATOR.join(sentence)+constants.END_LINE+constants.SEPARATOR

    # Takes out the last blank space which is not needed
    return result[:-1]

def generate_sentences_itertools(list_subject, list_predicate, list_object):
    """
        Function that returns an string with all the possible sentences that contains all the sentences in the alphabetical order that can be constructed using the provided subjects, predicates and objects as lists arguments.
        It uses optimization functions as itertools product or more legible functions as map.

        Args:
            list_subject: list. Contains the subjects of a sentence
            list_predicate: list. Contains the predicate of a sentence
            list_object: list. Contains the objects of a sentence
        Returns:
            sentences: sentences from the combination of the 3 lists as arguments
    """

    tuples_list = it.product(sorted(list_subject),sorted(list_predicate),sorted(list_object))
    sentences_list = map(lambda a:constants.SEPARATOR.join(a)+constants.END_LINE,tuples_list)
    sentences = (constants.SEPARATOR.join(map(str, sentences_list)))

    return sentences


if __name__ == "__main__":
    list_one = ["Vlad", "John"]
    list_two = ["drives"]
    list_three = ["car", "motorcycle", "bus"]
    generate_sentences_itertools(list_one,list_two,list_three)
