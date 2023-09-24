allGuests={'Alice':{'apples':5,'pretzels':12},'Bob':{'ham sandwiches':3,'apples':2},'Carol':{'cups':3,'apple pies':1}}
def totalBrought(guests,item):
    numBrought=0
    for k,v in guests.items():
        numBrought+=v.get(item,0)
    return numBrought
print("- Apples ",totalBrought(allGuests,'apples'))
print("- Cups ",totalBrought(allGuests,'cups'))
print("- Cakes ",totalBrought(allGuests,'cakes'))
print("- Ham Sandwiches ",totalBrought(allGuests,'ham sandwiches'))
print("- Apple Pies ",totalBrought(allGuests,'apple pies'))
