# Problem link - https://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/

class Solution:
    @staticmethod
    def _solve(words, i, sentence, sentences, n):
        if i >= n:
            sentences.append(" ".join(sentence))
            return
        for j in range(len(words[i])):
            Solution._solve(words, i + 1, sentence + [words[i][j]], sentences, n)

    @staticmethod
    def get_sentences(words):
        """
            Time complexity is O(n ^ m) and space complexity is O(m).
        """

        sentences = []
        n = len(words)
        Solution._solve(words, 0, [], sentences, n)
        for sentence in sentences:
            print(sentence)
        print()


Solution.get_sentences(
    [
        ["you", "we"],
        ["have", "are"],
        ["sleep", "eat", "drink"]
    ]
)

Solution.get_sentences(
    [
        ["you", "we"],
        ["have", "are"]
    ]
)

Solution.get_sentences(
    [
        ["I", "you"],
        ["do", "do not like"],
        ["walking", "eating"]
    ]
)

Solution.get_sentences(
    [
        ["work", "live"],
        ["easy", "happily"]
    ]
)