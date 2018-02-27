class Test(object):

    def __getitem__(self, key):
        return 5

print Test()[1]
