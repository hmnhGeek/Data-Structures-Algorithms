# Problem link - https://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/


from typing import List


def solve(word, sentence_list, n, i, list_of_sentences, word_lists):
    if i == n:
        for w in word_lists[i]:
            sentence = sentence_list + [w,]
            list_of_sentences.append(" ".join(sentence))
        return

    for w in word_lists[i]:
        solve(w, sentence_list + [w,], n, i + 1, list_of_sentences, word_lists)


def print_sentences(word_lists: List[List[str]]) -> List[str]:
    list_of_sentences = []
    start_list = word_lists[0]
    n = len(word_lists)
    for word in start_list:
        solve(word, [word,], n - 1, 1, list_of_sentences, word_lists)

    for sentence in list_of_sentences:
        print(sentence)


print_sentences([["you", "we"], ["have", "are"], ["sleep", "eat", "drink"]])