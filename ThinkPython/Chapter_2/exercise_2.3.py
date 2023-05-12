# 1) The volume of a sphere with radius r is 4/3(πr**3). 
# What is the volume of a sphere with radius 5?
r = 5

from math import pi
V = 4/3*(pi*r**3)   # find the volume
print("1. Volume = ", V)

# 2) Suppose the cover price of a book is $24.95, 
# but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?

coverPrice = 24.95
bookstoreCoverPrice = coverPrice*0.6
firstShippingCost = 3
additionalShippingCost = 0.75
copies = 60

totalWholesale = copies*bookstoreCoverPrice+(copies-1)*additionalShippingCost + firstShippingCost
print("2. Total wholesale cost: ", totalWholesale)


# 3) If I leave my house at 6:52 am and run 1 mile at an 
# easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) 
# and 1 mile at easy pace again, 
# what time do I get home for breakfast?

easyPaceTime = 2*(8 + 15/60)
tempoTime = 3*(7 + 12/60)

endTime = 6 + (52+ easyPaceTime + tempoTime)/60
print("3. Breakfast time: ", endTime)