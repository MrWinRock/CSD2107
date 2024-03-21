"Variable"
c1 = {}
c2 = {}
c3 = {}
c4 = {}
c5 = {}

a = 'a'
b = 'b'
c = 'c'

"Domain"
c1 = {c}
c2 = {b, c}
c3 = {a, b, c}
c4 = {a, b, c}
c5 = {b, c}

"Constraint"
a = {c3}
b = {}
c = {c1}

"arc con"
c1 = {c}
c2 = {b, 0}
c3 = {a, 0, c}
c4 = {0, b, 0}
c5 = {0, c}
