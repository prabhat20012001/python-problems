class Reverse:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        word=str(self.n)
        if 1 <= len(word) <= 10**4:
            return int(word[::-1])
        