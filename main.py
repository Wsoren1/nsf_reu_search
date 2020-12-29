from time import sleep
import keyboard
from search_keywords import database


nsf_reus = database('search_results.csv')

print('Up == Yes, Down == No')
for keyword in nsf_reus.get_unique_keywords():
    print(f'Keep keywords {keyword}?')
    while True:
        sleep(0.05)

        if keyboard.is_pressed('down'):
            sleep(0.75)
            nsf_reus.elim_keyword(keyword)
            break

        if keyboard.is_pressed('up'):
            sleep(0.75)
            break

        if keyboard.is_pressed('escape'):
            nsf_reus.save()
            exit()

nsf_reus.save()
