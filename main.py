from time import sleep
import keyboard
from search_keywords import database


nsf_reus = database('search_results.csv', 'keywords.data')

print('Up == Yes, Down == No')
for keyword in nsf_reus.uniques:
    print(f'Keep keyword {keyword}?')
    while True:
        sleep(0.05)
        pre_len = nsf_reus.df.shape[0]
        if keyboard.is_pressed('left'):
            sleep(0.75)
            nsf_reus.elim_keyword(keyword)
            break

        if keyboard.is_pressed('right'):
            sleep(0.75)
            break

        if keyboard.is_pressed('escape'):
            nsf_reus.save()
            exit()
        if pre_len != nsf_reus.df.shape[0]:
            print(f'Reduced {pre_len} entries to {nsf_reus.df.shape[0]}')
nsf_reus.save()
