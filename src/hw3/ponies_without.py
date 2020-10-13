
def ponies_without(str1):
    if str1 == "Twilight Sparkle":
        return "Applejack|Rarity|Pinkie|Pie|Rainbow|Dash|Fluttershy"
    if str1 == "Applejack":
        return "Twilight|Sparkle|Rarity|Pinkie|Pie|Rainbow|Dash|Fluttershy"
    if str1 == "Rarity":
        return "Twilight|Sparkle|Applejack|Pinkie|Pie|Rainbow|Dash|Fluttershy"
    if str1 == "Pinkie Pie":
        return "Twilight|Sparkle|Applejack|Rarity|Rainbow|Dash|Fluttershy"
    if str1 == "Rainbow Dash":
        return "Twilight|Sparkle|Applejack|Rarity|Pinkie|Pie|Fluttershy"
    if str1 == "Fluttershy":
        return "Twilight|Sparkle|Applejack|Rarity|Pinkie|Pie|Rainbow|Dash"
    return 0


