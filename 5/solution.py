from typing import List


class Solution:
    def is_valid(self, score: str) -> bool:
        return score == 'X' or score == '/' or score.isdigit()

    def to_raw(self, score: str) -> int:
        if score == 'X':
            return 10
        if score == '/':
            return 10
        if score.isdigit():
            return int(score)


    def get_score(self, scores:List[str]):
        print(len(scores))
        scores = list(filter(self.is_valid,scores))
        raw_scores = list(map(self.to_raw,scores))
        scores_len = len(scores)

        print(scores)
        print(raw_scores)

        total = 0
        i = 0
        for score in scores:
            if score == 'X':
                total += sum(raw_scores[i:min(i+3,scores_len)])
            elif score == '/':
                total += sum(raw_scores[i:min(i+2,scores_len)]) - raw_scores[i-1]
            else:
                total += raw_scores[i]

            print(total)
            i += 1

        return total