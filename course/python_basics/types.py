a = 1
b = 12345677456789876543
c = 1.23456789

s1 = 'Hello'
s2 = "Hello"
assert s1 == s2

set1 = set([1,2]).union({3})
assert set1 == {1,2,3}

l1 = [1, 2, 3, "4", "5"]
l2 = [1] + [2] + [3] + ["4"] + ["5"]
assert l1 == l2

t1 = (1, 2, 3, "4", "5")
t2 = (1,) + (2,) + (3,) + ("4",) + ("5",)
assert t1 == t2

d1 = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5"}
d2 = {}
d3 = dict()
d2[1] = "1"
d2[2] = "2"
d2.update({3: "3", 4: "4", 5: "5"})
assert d1 == d2
d3 = dict(zip([1,2,3,4,5], ["1","2","3","4","5"]))
assert d1 == d3



s = 'Hello' + ' ' +  'World'
assert s == 'Hello World'
s = s.replace('World', 'father')
assert s == 'Hello father'
assert '  Yoy '.strip() == 'Yoy'
assert '  Yoy '.lstrip() == 'Yoy '
assert '"""  Yoy "'.strip('"') == '  Yoy '
assert 'Hello'.index('e') == 1
assert 'Hello World World'.replace('World', 'father') == 'Hello father father'
assert 'Hello World World'.replace('World', 'father', 1) == 'Hello father World'
assert 'Hello'.startswith('H') == True
assert 'hello'.capitalize() == 'Hello'