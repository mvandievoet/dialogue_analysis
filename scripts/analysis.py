'''
This file will produce a JSON file and will make a selection and analysis of the relevant dialog
The 5 ponies are Twilight Sparkle, Applejack, Rarity, Pinkie Pie, Rainbow Dash, Fluttershy
'''

import json
import pandas as pd
import sys
import argparse
from hw3.set_mentions import set_mentions
from hw3.dialog_by_non_pony import dialog_by_non_pony
from hw3.ponies_without import ponies_without
from hw3.set_data import set_data
from hw3.create_dfs import create_dfs 
from hw3.to2decimal import to2decimal
from hw3.get5words import get5words
from hw3.create_wordlist import create_wordlist
from hw3.len_nested import len_nested
from hw3.pony_i import pony_i
from hw3.equals_either import equals_either

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src_file', help='the link to the clean dialog file that will be used')
    parser.add_argument('-o', help='the potential JSON output file ... should end in .json')
    args = parser.parse_args()
    src_file = args.src_file

    dialog = pd.read_csv(src_file)
    dialog = dialog[['pony', 'dialog']]

    ponies = ["twilight", "applejack", "rarity", "pinkie", "rainbow", "fluttershy"]
    ponies_cap = ["Twilight", "Applejack", "Rarity", "Pinkie", "Rainbow", "Fluttershy"]

    data, verbosity, mentions, follow_on_comments = {}, {}, {}, {}
    twilight, applejack, rarity, pinkie, rainbow, fluttershy = {}, {}, {}, {}, {}, {}
    twilight1, applejack1, rarity1, pinkie1, rainbow1, fluttershy1 = {}, {}, {}, {}, {}, {}
    non_dictionary_words = {}

    # verbosity elements
    twilight_dfs = equals_either(dialog,"Twilight Sparkle","Everypony")
    applejack_dfs = equals_either(dialog,"Applejack","Everypony")
    rarity_dfs = equals_either(dialog,"Rarity","Everypony")
    pinkie_dfs = equals_either(dialog,"Pinkie Pie","Everypony")
    rainbow_dfs = equals_either(dialog,"Rainbow Dash","Everypony")
    fluttershy_dfs = equals_either(dialog,"Fluttershy","Everypony")

    sum_pony_dialog = twilight_dfs['pony'].size + applejack_dfs['pony'].size + rarity_dfs['pony'].size
    sum_pony_dialog += pinkie_dfs['pony'].size + rainbow_dfs['pony'].size + fluttershy_dfs['pony'].size

    ponies_dfs = [twilight_dfs, applejack_dfs, rarity_dfs, pinkie_dfs, rainbow_dfs, fluttershy_dfs]

    # creating the verbosity dictionary
    j = 0
    for i in ponies_dfs:
        verbosity[ponies[j]] = to2decimal(i['pony'].size/sum_pony_dialog)
        j = j+1

    data['verbosity'] = verbosity

    # mentions element
    # df of pony that mentions any other ponies
    mentions_twilight = twilight_dfs[twilight_dfs['dialog'].str.contains(ponies_without("Twilight Sparkle"))]
    mentions_applejack = applejack_dfs[applejack_dfs['dialog'].str.contains(ponies_without("Applejack"))]
    mentions_rarity = rarity_dfs[rarity_dfs['dialog'].str.contains(ponies_without("Rarity"))]
    mentions_pinkie = pinkie_dfs[pinkie_dfs['dialog'].str.contains(ponies_without("Pinkie Pie"))]
    mentions_rainbow = rainbow_dfs[rainbow_dfs['dialog'].str.contains(ponies_without("Rainbow Dash"))]
    mentions_fluttershy = fluttershy_dfs[fluttershy_dfs['dialog'].str.contains(ponies_without("Fluttershy"))]

    mentions_by = [[], [], [], [], [], []]

    sum1 = 0
    for i in range(1, 6):
        mentions_by[0].append(mentions_twilight[mentions_twilight['dialog'].str.contains(ponies_cap[i])])
        twilight1[ponies[i]] = mentions_by[0][-1].size
        sum1 = sum1 + mentions_by[0][-1].size

    for i in range(1, 6):
        twilight1[ponies[i]] = to2decimal(twilight1[ponies[i]]/sum1)

    sum1 = 0
    for i in [0, 2, 3, 4, 5]:
        mentions_by[1].append(mentions_applejack[mentions_applejack['dialog'].str.contains(ponies_cap[i])])
        applejack1[ponies[i]] = mentions_by[1][-1].size
        sum1 = sum1 + mentions_by[1][-1].size

    for i in [0, 2, 3, 4, 5]:
        applejack1[ponies[i]] = to2decimal(applejack1[ponies[i]]/sum1)

    sum1 = 0
    for i in [0, 1, 3, 4, 5]:
        mentions_by[2].append(mentions_rarity[mentions_rarity['dialog'].str.contains(ponies_cap[i])])
        rarity1[ponies[i]] = mentions_by[2][-1].size
        sum1 = sum1 + mentions_by[2][-1].size

    for i in [0, 1, 3, 4, 5]:
        rarity1[ponies[i]] = to2decimal(rarity1[ponies[i]]/sum1)

    sum1 = 0
    for i in [0, 1, 2, 4, 5]:
        mentions_by[3].append(mentions_pinkie[mentions_pinkie['dialog'].str.contains(ponies_cap[i])])
        pinkie1[ponies[i]] = mentions_by[3][-1].size
        sum1 = sum1 + mentions_by[3][-1].size

    for i in [0, 1, 2, 4, 5]:
        pinkie1[ponies[i]] = to2decimal(pinkie1[ponies[i]]/sum1)

    sum1 = 0
    for i in [0, 1, 2, 3, 5]:
        mentions_by[4].append(mentions_rainbow[mentions_rainbow['dialog'].str.contains(ponies_cap[i])])
        rainbow1[ponies[i]] = mentions_by[4][-1].size
        sum1 = sum1 + mentions_by[4][-1].size

    for i in [0, 1, 2, 3, 5]:
        rainbow1[ponies[i]] = to2decimal(rainbow1[ponies[i]]/sum1)

    sum1 = 0
    for i in [0, 1, 2, 3, 4]:
        mentions_by[5].append(mentions_fluttershy[mentions_fluttershy['dialog'].str.contains(ponies_cap[i])])
        fluttershy1[ponies[i]] = mentions_by[5][-1].size
        sum1 = sum1 + mentions_by[5][-1].size

    for i in [0, 1, 2, 3, 4]:
        fluttershy1[ponies[i]] = to2decimal(fluttershy1[ponies[i]]/sum1)

    ponies_data = [twilight1, applejack1, rarity1, pinkie1, rainbow1, fluttershy1]
    data['mentions'] = set_mentions(ponies, ponies_data, mentions)

    # non-dictionary words start
    real_words = set(pd.read_csv("../data/words_alpha.txt", sep=" ", header=None)[0])
    c = 0
    for i in ponies:
        non_dictionary_words[i] = get5words(ponies_dfs[c], real_words)
        c += 1

    # follow on comments started
    # creation of data structure for others
    dialog_by_others = dialog_by_non_pony(dialog)
    dialog_by_others.to_csv('dialog_by_others.csv')

    # add function create new dfs
    arr = ["Twilight|Sparkle", "Applejack", "Rarity", "Pinkie|Pie", "Rainbow|Dash", "Fluttershy"]
    ponies_dfs = create_dfs(arr, ponies_dfs, dialog_by_others)

    # twilight
    total_count = 0
    for i in [1, 2, 3, 4, 5]:
        count = 0
        for j in mentions_by[i][0]['pony'].index:
            if (dialog.iloc[j+1, 0] == pony_i(0) or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        twilight[ponies[i]] = count

    count = 0
    for j in ponies_dfs[0]['pony'].index:
        if (dialog.iloc[j+1, 0] == "Twilight Sparkle" or dialog.iloc[j+1,0]=="Everypony"):
            count += 1

    total_count += count

    for i in [1, 2, 3, 4, 5]:
        twilight[ponies[i]] = to2decimal(twilight[ponies[i]]/total_count)

    twilight['other'] = to2decimal(count/total_count)
    # applejack
    total_count = 0
    for i in [0, 2, 3, 4, 5]:
        count = 0
        if i == 0:
            key = 0
        else:
            key = 1
        for j in mentions_by[i][key]['pony'].index:
            if (dialog.iloc[j+1, 0]=="Applejack" or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        applejack[ponies[i]] = count

    count = 0
    for j in ponies_dfs[1]['pony'].index:
        if (dialog.iloc[j+1, 0]=="Applejack" or dialog.iloc[j+1, 0]=="Everypony"):
            count += 1

    total_count += count
    for i in [0, 2, 3, 4, 5]:
        applejack[ponies[i]] = to2decimal(applejack[ponies[i]]/total_count)

    applejack['other'] = to2decimal(count/total_count)
    # rarity
    total_count = 0
    for i in [0, 1, 3, 4, 5]:
        count = 0
        if i == (0 or 1):
            key = 1
        else:
            key = 2
        for j in mentions_by[i][key]['pony'].index:
            if (dialog.iloc[j+1, 0]=="Rarity" or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        rarity[ponies[i]] = count

    count = 0
    for j in ponies_dfs[2]['pony'].index:
        if (dialog.iloc[j+1, 0]=="Rarity" or dialog.iloc[j+1, 0]=="Everypony"):
            count += 1

    total_count += count
    for i in [0, 1, 3, 4, 5]:
        rarity[ponies[i]] = to2decimal(rarity[ponies[i]]/total_count)

    rarity['other'] = to2decimal(count/total_count)
    # pinkie
    total_count = 0
    for i in [0, 1, 2, 4, 5]:
        count = 0
        if i == (0 or 1 or 2):
            key = 2
        else:
            key = 3
        for j in mentions_by[i][key]['pony'].index:
            if (dialog.iloc[j+1, 0] == "Pinkie Pie" or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        pinkie[ponies[i]] = count

    count = 0
    for j in ponies_dfs[3]['pony'].index:
        if (dialog.iloc[j+1, 0] == "Pinkie Pie" or dialog.iloc[j+1, 0]=="Everypony"):
            count += 1

    total_count += count
    for i in [0, 1, 2, 4, 5]:
        pinkie[ponies[i]] = to2decimal(pinkie[ponies[i]]/total_count)

    pinkie['other'] = to2decimal(count/total_count)
    # rainbow
    total_count = 0
    for i in [0, 1, 2, 3, 5]:
        count = 0
        if i == 5:
            key = 4
        else:
            key = 3
        for j in mentions_by[i][key]['pony'].index:
            if (dialog.iloc[j+1, 0] == "Rainbow Dash" or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        rainbow[ponies[i]] = count

    count = 0
    for j in ponies_dfs[4]['pony'].index:
        if (dialog.iloc[j+1, 0]=="Rainbow Dash" or dialog.iloc[j+1, 0]=="Everypony"):
            count += 1

    total_count += count
    for i in [0, 1, 2, 3, 5]:
        rainbow[ponies[i]] = to2decimal(rainbow[ponies[i]]/total_count)

    rainbow['other'] = to2decimal(count/total_count)
    # fluttershy
    total_count = 0
    for i in [0, 1, 2, 3, 4]:
        count = 0
        for j in mentions_by[i][4]['pony'].index:
            if (dialog.iloc[j+1, 0]=="Fluttershy" or dialog.iloc[j+1, 0]=="Everypony"):
                count += 1

        total_count += count
        fluttershy[ponies[i]] = count

    count = 0
    for j in ponies_dfs[5]['pony'].index:
        if (dialog.iloc[j+1, 0]=="Fluttershy" or dialog.iloc[j+1, 0]=="Everypony"):
            count += 1

    total_count += count
    for i in [0, 1, 2, 3, 4]:
        fluttershy[ponies[i]] = to2decimal(fluttershy[ponies[i]]/total_count)

    fluttershy['other'] = to2decimal(count/total_count)

    ponies_data = [twilight, applejack, rarity, pinkie, rainbow, fluttershy]
    data['follow_on_comments'] = set_data(ponies, ponies_data, follow_on_comments)
    # write non_dic_words
    data['non_dictionary_words'] = non_dictionary_words

    # write json file
    if len(sys.argv) == 2:
        print(data)
    if len(sys.argv) == 4:
        with open(sys.argv[2], 'w') as fl:
            json.dump(data, fl)


if __name__ == '__main__':
    main()
