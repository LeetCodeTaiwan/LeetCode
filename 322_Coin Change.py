class Solution(object):
    # BFS + Branch and bound

    def __init__(self):
        self.level_queue = []
        self.next_level_queue = []
        # record whether is traveled or not
        self.dic = {}

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not coins:
            return -1
        if amount == 0:
            return 0

        coin_numbers = 1
        self.level_queue.append(amount)

        while self.level_queue != []:
            for new_amount in self.level_queue:
                for number in coins:
                    if new_amount - number == 0:
                        return coin_numbers
                    elif new_amount - number in self.dic:
                        pass
                    elif new_amount - number > 0:
                        self.next_level_queue.append(new_amount - number)
                        self.dic[new_amount - number] = coin_numbers
                    else:
                        pass
                self.level_queue = self.level_queue[1:]
                if self.level_queue == []:
                    coin_numbers += 1
                    self.level_queue = list(self.next_level_queue)
                    self.next_level_queue = []
        return -1
