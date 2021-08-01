def house_allocation(prices,budget):
    arr = sorted(prices)
    number_of_houses = 0
    #
    # \\\   `L   ≥MK.sum = 0
    for price in arr:
        if price <= budget:
            budget = budget - price
            #sum += price
            number_of_houses += 1
    
    return number_of_houses
#Algorithm
#1. Sort the array by lowest
#2. Add the prices as you iterate through the sorted arry
#3. 











#Driver function
Prices = 20,90,40,90 #2
budget = 100
print(house_allocation(Prices,budget))