class TenGrades(object):
    def __init__(self, argv=[]):
        # self.array = gen
        self.score_dice(self)

    @staticmethod
    def score_dice(argv=[]):
        if len(argv) > 5:
            return 0

        result = 1000 * (argv.count(1) // 3) \
                 + 100 * (argv.count(1) % 3) \
                 + 200 * (argv.count(2) // 3) \
                 + 300 * (argv.count(3) // 3) \
                 + 400 * (argv.count(4) // 3) \
                 + 500 * (argv.count(5) // 3) \
                 + 50 * (argv.count(5) % 3)
        print("result:", result)
        return result

# A = TenGrades()
TenGrades.score_dice([1,1,1,5,1])
# A.score_dice([2,3,6])
# A.score_dice([3,4,5,3,3])
# A.score_dice([1,5,1,4])