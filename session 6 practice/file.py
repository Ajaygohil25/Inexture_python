import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
c = collections.defaultdict(None,s)
print(type(d))
for k, v in s:
    d[k].append(v)


d["Asdf"]
print(d)
sorted(d.items())