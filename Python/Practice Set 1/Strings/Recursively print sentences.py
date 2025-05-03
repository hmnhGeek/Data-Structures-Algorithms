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