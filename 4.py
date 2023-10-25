import json
with open("firms.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
firms_profit = []
total_profit = 0
num_profit_firms = 0
for line in lines:
    parts = line.split()
    name = parts[0]
    revenue = float(parts[2])
    costs = float(parts[3])
    profit = revenue - costs
    if profit >= 0:
        num_profit_firms += 1
        total_profit += profit
    firm_dict = {name: profit}
    firms_profit.append(firm_dict)
    average_profit = total_profit / num_profit_firms
    average_dict = {"average_profit": average_profit}
    firms_profit.append(average_dict)
    with open("firms.json", "w", encoding="utf-8") as json_file:
        json.dump(firms_profit, json_file)