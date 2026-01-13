class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calc_score(player):
            score = 0
            for i in range(len(player)):
                if (i >= 1 and player[i-1] == 10) or (i >= 2 and player[i-2] == 10):
                    score += 2 * player[i]
                else:
                    score += player[i]
            return score
        
        s1 = calc_score(player1)
        s2 = calc_score(player2)
        
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0