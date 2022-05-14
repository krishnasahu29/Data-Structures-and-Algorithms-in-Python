from itertools import permutations


class Vendor:

    def __init__(self, string):
        self.string = string
        self.vowel_list = ['A', 'E', 'I', 'O', 'U']
        self.points_banta = 0
        self.points_santa = 0

    @staticmethod
    def split_string(word):
        return [char for char in word]

    def banta_score(self):
        for item in self.permutation():
            if item[0] in self.vowel_list:
                self.points_banta += 1

        print('Banta Scored: {}'.format(self.points_banta))

    def santa_score(self):
        for item in self.permutation():
            if item[0] not in self.vowel_list:
                self.points_santa += 1

        print('Santa Scored: {}'.format(self.points_santa))

    def permutation(self):

        for i in range(len(self.string)):
            for j in range(i):

                perm = permutations(self.string[j:i])
                return perm


if __name__ == '__main__':
    V = Vendor('BANANA')
    # print(V.permutation())
    V.banta_score()
    V.santa_score()
