s = "a34ryanAa34"
to_replace = s[0]+s[1]+s[2]
for i in to_replace:
    s = s.replace(i,'')
print(s)
