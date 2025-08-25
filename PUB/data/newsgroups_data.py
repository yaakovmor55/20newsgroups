import random
from sklearn.datasets import fetch_20newsgroups

class NewsgroupsData:
    def __init__(self):

        self.interesting_categories = [
            'alt.atheism',
            'comp.graphics',
            'comp.os.ms-windows.misc',
            'comp.sys.ibm.pc.hardware',
            'comp.sys.mac.hardware',
            'comp.windows.x',
            'misc.forsale',
            'rec.autos',
            'rec.motorcycles',
            'rec.sport.baseball'
        ]

        self.not_interesting_categories = [
            'rec.sport.hockey',
            'sci.crypt',
            'sci.electronics',
            'sci.med',
            'sci.space',
            'soc.religion.christian',
            'talk.politics.guns',
            'talk.politics.mideast',
            'talk.politics.misc',
            'talk.religion.misc'
        ]

        self.newsgroups_interesting = fetch_20newsgroups(
            subset='all',
            categories=self.interesting_categories
        )

        self.newsgroups_not_interesting = fetch_20newsgroups(
            subset='all',
            categories=self.not_interesting_categories
        )
        self.interesting = []
        self.not_interesting = []


    def get_data(self):

        for i in range(10):
            self.interesting.append(self.newsgroups_interesting.data[random.randint(0, len(self.newsgroups_interesting.data)-1)])
            self.not_interesting.append(self.newsgroups_not_interesting.data[random.randint(0, len(self.newsgroups_not_interesting.data)-1)])

