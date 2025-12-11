loot_log = [
    "Weapon:Iron Sword:150",
    "Potion:Health Potion:10",
    "Armor:Leather Vest:80",
    "Weapon:Steel Dagger:120",
    "Potion:Mana Potion:15",
    "Armor:Iron Helm:50"
]


def sort_loot(loot_log):
    dictionary = {}
    for line in loot_log:
    
        item_type, item_name, gold = line.split(':')
        gold = int(gold)
    
        if item_type not in dictionary:
            dictionary[item_type] = []

        dictionary[item_type].append((item_name, gold))
    return dictionary
result = sort_loot(loot_log)


def appraise_inventory(loot_dict):


    for line in loot_dict:
        count = 0
        for item in loot_dict[line]:
            count += item[1]
        print(f"{line}: {count} Gold")
appraise_inventory(result)







    
