users = {
    "Alice": ["Coding", "Music", "Hiking", "Pizza"],
    "Bob":   ["Movies", "Hiking", "Tacos"],
    "Charlie": ["Coding", "Pizza", "Gaming", "Music"],
    "David": ["Cooking", "Travel"]
}
def common_interest(users, target):

    common = {}
    for names, interests in users.items():
        if names == target:
            continue
        count = 0
        for interest in interests:
            if interest in users[target]:
                count += 1

        common[names] = count

    for name, count in common.items():
        maxium = 0
    
        if count > maxium:
            maxium = count
            maxium_name = name
            maxium_count = maxium
        print(f"Comparing {target} with {name}... {count} shared interests")
    
    print('-' * 40)
    print(f"Best match for {target} is {maxium_name} with {maxium_count} shared interests")
    print(common)
    
common_interest(users, "Bob")
    