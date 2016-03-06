class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""

		def checkLife(i, j):

			liveCellNum = 0
			
			for rd, cd in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
				if rd + i >= 0 and rd + i < len(board) and cd + j >= 0 and cd + j < len(board[0]):
					liveCellNum += board[rd+i][cd+j]

			if liveCellNum == 3:
				return 1
			elif liveCellNum == 2:
				return board[i][j] & 1
			else:
				return 0

		nextTurnBoard = [row[:] for row in board]

		for i in range(len(board)):
			for j in range(len(board[0])):
				nextTurnBoard[i][j] = checkLife(i,j)

		board = nextTurnBoard

		return board

Instance = Solution()
print(Instance.gameOfLife([[1]]))