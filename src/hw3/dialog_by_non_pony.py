
def dialog_by_non_pony(dialog):
    ponies = ["Twilight Sparkle","Applejack","Rarity","Everypony","Pinkie Pie","Rainbow Dash", "Fluttershy"]
    for i in range(len(ponies)):
        dialog = dialog[dialog['pony']!=ponies[i]]
    return dialog


