class Pattern:
    # data: a list of lists of ints ([[1,2,3], [4,5,6]])
    # Initializes the class, storing data in an instance variable
    def __init__(self, data):
      self.data = data

    # filename: a string (“image.txt”)
    # Create a PGM image from the data passed to the constructor, and write it to filename.
    # The image dimensions should match the size of data, and the depth should be 255.
    def make_image(self, filename):
        with open(filename, "w") as file:
            file.write(f"P2 {len(self.data[0])} {len(self.data)} 255\n")
            for row in self.data:
                for item in row:
                    file.write(str(item) + " ")
                file.write("\n")


class SquareFrame(Pattern):
    def __init__(self, size):
        data = []
        for y in range(size):
            row = []
            for x in range(size):
                if x == 0 or y == 0 or x == size-1 or y == size-1:
                    row.append(0)
                else:
                    row.append(255)
            data.append(row)

        super().__init__(data)

# square_frame = SquareFrame(100)
# square_frame.make_image("square_frame.pgm")

class Cross(Pattern):
    def __init__(self, size):
        data = []
        for y in range(size):
            row = []
            for x in range(size):
                if x == size // 2 or y == size // 2:
                    row.append(0)
                else:
                    row.append(255)
            data.append(row)

        super().__init__(data)

# cross = Cross(100)
# cross.make_image("cross.pgm")

class AnySizeCheckersBoard(Pattern):
    def __init__(self, size):
        data = []
        for y in range(size):
            row = []
            for x in range(size):
                if x % 2 == 0:
                    row.append(0 if y % 2 == 0 else 255)
                else:
                    row.append(255 if y % 2 == 0 else 0)
            data.append(row)

        super().__init__(data)

# any_size_checkers = AnySizeCheckersBoard(100)
# any_size_checkers.make_image("any_size_checkers.pgm")