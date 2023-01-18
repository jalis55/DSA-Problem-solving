prices = [1,2,4,2,5,7,2,4,9,0,9]

profit=0

l=0
r=1
def profitable(profit,cur_profit):
    if cur_profit>profit:
        return cur_profit
    return profit
while r<len(prices):
    if prices[l]<prices[r]:
        cur_porfit=prices[r]-prices[l]
        profit=cur_porfit if cur_porfit>profit else profit
        # profit=profitable(profit,cur_porfit)
        
        
            
    else:
        l =r
    r +=1
   
print(profit)