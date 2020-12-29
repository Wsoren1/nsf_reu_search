import pandas as pd


class database:
    def __init__(self, fpath):
        self.df = pd.read_csv(fpath)
        self.df['Research Topics/Keywords'] = self.df['Research Topics/Keywords'].apply(lambda x: x.lower())

    def get_unique_keywords(self):
        _uniques = []
        for keyword in self.df['Research Topics/Keywords']:
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

    def elim_keyword(self, keyword): # => dataframe
        keyword = keyword.lower()

        pre_query_len = self.df.shape[0]

        filt = self.df['Research Topics/Keywords'].str.contains(keyword)
        result = self.df[~filt]

        if pre_query_len == result.shape[0]:
            print(f'{keyword} not found in keywords')
        self.df = result
        return result

    def save(self):
        self.df.to_csv('search_results.csv', index=False)