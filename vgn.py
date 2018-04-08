import datetime

year = datetime.date.today().year

# generating intro
print("'''<u>V</u>or<u>g</u>angs<u>n</u>ummern''' für das Jahr {}.".format(year))

# getting VGNs
print("== Vorgangsnummern ==")
print("{| class='wikitable' width='100%'\n|-\n! style='width: 10%;' | Shortcut\n! style='width: 90%;' | Beschreibung")
for i in range(1, 101):

    vgn = "V{}{}".format(year, i)
    
    print("|-")
    print("| [[{}]]".format(vgn))
    print("| <!-- {} -->".format(vgn))
    

print("|}\n")

# Generating Category
print("[[Kategorie:Vorgang|Shortcuts/{}]]".format(year))
