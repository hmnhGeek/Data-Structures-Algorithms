def recursive():
    def solve(words, i, prev_consumed_space, k):
        if i == len(words):
            return 0

        # if we stay on the same line with words[i] word
        cost_for_being_on_same_line = 1e6
        consumed_spaces = prev_consumed_space + 1 + words[i]
        if consumed_spaces <= k:
            cost_for_being_on_same_line = solve(words, i + 1, consumed_spaces, k)

        # if we move to the next line with words[i] word, then compute the cost by using previous consumed space and
        # place the current word in the next line.
        cost_for_switching_lines = (k - prev_consumed_space)**2 + solve(words, i + 1, words[i], k)

        # get the minimum cost out of both.
        return min(cost_for_being_on_same_line, cost_for_switching_lines)

    def word_wrap(words, k):
        n = len(words)
        # start with 1st word and place 0th word in the first line.
        return solve(words, 1, words[0], k)

    print(word_wrap([3, 2, 2, 5], 6))
    print(word_wrap([3, 2, 2], 4))


recursive()