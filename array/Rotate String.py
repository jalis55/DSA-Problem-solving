from xmlrpc.client import boolean


s = "abcde"
goal = "cdeab"

temp=s
status=False

while True:
    t=temp[0]
    temp=temp[1:]+temp[0]
    print(temp)
    if temp==goal:
        status=True
    if temp==s:
        break

print(status)
