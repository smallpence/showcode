class Solution:

    def devvie(self, input: str):
        if not input:
            return 0

        if not isinstance(input, str):
            return 0

        input = filter(lambda char: (char == "F") | (char == "L") | (char == "R"), input)

        x = 0
        y = 0
        directions = ['E', 'N', 'W', 'S']
        direction = 'N'

        for instruction in input:
            print(instruction)

            if instruction == 'F':
                if direction == 'E':
                    x += 1

                if direction == 'N':
                    y += 1

                if direction == 'W':
                    x -= 1

                if direction == 'S':
                    y -= 1

            if (instruction == 'R') | (instruction == 'L'):
                turn = 1 if instruction == 'L' else -1

                direction = directions[directions.index(direction) + turn]

            print(f"now x:{x} y:{y} d:{direction}")

        cost = 2

        if (direction == 'E') & (x <= 0):
            if y == 0:
                cost -= 2
            else:
                cost -= 1

        if (direction == 'N') & (y <= 0):
            if x == 0:
                cost -= 2
            else:
                cost -= 1

        if (direction == 'W') & (x >= 0):
            if y == 0:
                cost -= 2
            else:
                cost -= 1

        if (direction == 'S') & (y >= 0):
            if x == 0:
                cost -= 2
            else:
                cost -= 1

        return cost + x + y
