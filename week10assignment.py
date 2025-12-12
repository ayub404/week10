
pledge_list = [
    "Alice,Animals,50",
    "Bob,Environment,100",
    "Charlie,Animals,25",
    "David,Education,200",
    "Eve,Environment,50",
    "Frank,Education,75"
]

def process_donations(pledge_list):
    dictionary = {}
    for i in pledge_list:
        donorname, cause, amount = i.split(',')
        amount = int(amount)
        if cause not in dictionary:
            dictionary[cause] = []

        dictionary[cause].append((donorname, amount)) 
    return dictionary

collected_list = process_donations(pledge_list)
# print(collected_list)
def print_fund_totals(charity_dict):
    for types in charity_dict:
        count = 0
        for i in charity_dict[types]:
            count += i[1]
        print(f"{types}: ${count} total")
print_fund_totals(collected_list)




    
