print("=============TAXI FARE CALCULATION============")
def calc(l):
    price=list(map(lambda x:50+x*10,l))
    return price

trip=[]

n=int(input("Enter the number of trips : "))

for i in range(n):
    trip.append(int(input(f"distance of trip {i+1} : ")))

costs=calc(trip)

for i in range(len(costs)):
    print(f"Trip {i+1} : ${costs[i]}")

print(f"Total fare ${sum(costs)}")