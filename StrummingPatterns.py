PATTERN_TEMPLATE = " 1 + 2 + 3 + 4 +"

class Strumming:
    _total_pattern_count: int = 0
    _down_starting_pattern_count: int = 0

    def printStrummingPattern(self, pattern: list[str]):
        print(PATTERN_TEMPLATE)
        pattern_str = " ".join(pattern)
        print(f" {pattern_str}")
        print("\n")

    def createStrummingPattern(self, pattern: list[str], index: int):
        if index == 8:
            self._total_pattern_count += 1
            if pattern[0] == 'D':
                self._down_starting_pattern_count += 1
                self.printStrummingPattern(pattern)
            return
        
        next_index = index+1
        strum = ""

        if index % 2 == 0:
            strum = "D"
        else:
            strum = "U"
        
        # Strum UP, Down, or Skip
        self.createStrummingPattern(pattern + [strum], next_index)
        self.createStrummingPattern(pattern + [" "], next_index)


strumming = Strumming()
strumming.createStrummingPattern([], 0)
print(f"Useful pattern count = {strumming._down_starting_pattern_count}\n Total pattern count = {strumming._total_pattern_count}")