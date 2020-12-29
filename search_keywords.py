import pandas as pd
import re
import pickle


class database:
    def __init__(self, fpath, keywords_fpath=None):
        self.df = pd.read_csv(fpath)
        self.df['Research Topics/Keywords'] = self.df['Research Topics/Keywords'].apply(lambda x: x.lower())
        if keywords_fpath is None:
            self.uniques = self.get_unique_keywords()
        else:
            with open('keywords.data', 'rb') as f:
                self.uniques = pickle.load(f)


    def get_unique_keywords(self):
        _uniques = []
        for entry in self.df['Research Topics/Keywords']:
            for keyword in entry.split(','):
                if keyword not in _uniques:
                    _uniques.append(keyword)
        return _uniques

    @staticmethod
    def tar_in_arr(arr, target):
        if target.isin(arr):
            return True
        else:
            for string in arr:
                if target.isin(string):
                    return True
        return False

    def elim_keyword(self, keyword):  # => dataframe
        keyword = keyword.lower()

        if keyword not in self.uniques:
            print(f'{keyword} not found')
            return self.df

        self.uniques.remove(keyword)

        reg_search = re.escape('|'.join(self.uniques).replace('||', '|'))
        # df["TrueFalse"] = df['col1'].apply(lambda x: 1 if any(i in x for i in searchfor) else 0)
        filt = self.df['Research Topics/Keywords'].apply(lambda x: True if any(i in x for i in self.uniques) else False)
        result = self.df[filt]

        self.df = result
        return result

    def save(self):
        with open('keywords.data', 'wb') as f:
            pickle.dump(self.uniques, f)
        self.df.to_csv('search_results.csv', index=False)
