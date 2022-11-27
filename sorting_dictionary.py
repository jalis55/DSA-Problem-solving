map={'usa':50000,'rsa':30000,'cda':70000}

# print(map)
# print(sorted(map))
print(sorted(map.items())) 

sortet_by_key={k:v for k,v in sorted(map.items())}

print(sortet_by_key)

sortet_by_value={k:v for k,v in sorted(map.items(),key=lambda v:v[1])}

print(sortet_by_value)

print(list(sortet_by_value.keys()))
print(list(sortet_by_value.values()))
