class Solution:
    def solveSudoku(self, board):

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # Store empty cells
        empty = []

        # Build masks from existing numbers
        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    empty.append((r, c))

                else:
                    num = int(board[r][c])
                    bit = 1 << (num - 1)

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + (c // 3)] |= bit

        def backtrack(index):

            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + (c // 3)

            # Numbers that are already used
            used = rows[r] | cols[c] | boxes[box]

            # Available numbers
            available = (~used) & 0x1FF

            while available:

                # Get the lowest available bit
                bit = available & -available

                # Remove this bit
                available -= bit

                # Convert bit to number
                num = bit.bit_length()

                # Place number
                board[r][c] = str(num)

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

                # Continue
                if backtrack(index + 1):
                    return True

                # Undo
                board[r][c] = '.'

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box] ^= bit

            return False

        backtrack(0)