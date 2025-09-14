class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters_dict = {c: i for i, c in enumerate(order)}

        def in_correct_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if letters_dict[c1] < letters_dict[c2]:
                    return True    # correct order
                elif letters_dict[c1] > letters_dict[c2]:
                    return False   # wrong order
            return len(w1) <= len(w2)  # prefix case

        # check all consecutive pairs
        for i in range(len(words) - 1):
            if not in_correct_order(words[i], words[i + 1]):
                return False

        return True