# Problem link - https://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/


from typing import List


def solve(i, n, sentence_list, list_of_sentences, word_lists):
    # add the words from last list, if index == n.
    if i == n:
        for w in word_lists[i]:
            sentence = sentence_list + [w,]
            list_of_sentences.append(" ".join(sentence))
        return

    # else recursively call for the next list and append the current word in sentence list.
    for w in word_lists[i]:
        solve(i + 1, n, sentence_list + [w,], list_of_sentences, word_lists)


def print_sentences(word_lists: List[List[str]]):
    """
        Overall time complexity is O(n^m) where n is the number of word lists and m is the
        number of words in a word list. Space complexity is O(n) for recursion stack.
    """

    # store a reference to an empty list which will hold the list of sentences.
    list_of_sentences = []
    n = len(word_lists)

    # start the recursion from 0th index and go till last list of words
    solve(0, n - 1, [], list_of_sentences, word_lists)

    for sentence in list_of_sentences:
        print(sentence)


print_sentences([["you", "we"], ["have", "are"], ["sleep", "eat", "drink"]])