accounts = [
    [1,2,3],
    [3,2,1],
    [7,5,6],
    [2,8,7]
    ]
def suma(accounts):
    wealthness=[]
    for lists in accounts:
        riqueza=sum(lists)
        wealthness.append(riqueza)
    return wealthness
def max(wealthness):
    max = 0
    for x in wealthness:
        x=int(x)
        if x>max:
            max=x
    return max
def main():
    print(accounts)
    print(f"The most rich client has: {max(suma(accounts))}")
main()
