print('One a Day One Liners with Python - 2023.02.02')
print('Scale and rotation invariant triangle similarity test 📐')

a = 6, 8, 4
b = 5, 7.5, 10
c = 10, 7.5, 10

a_theta = (a[1]**2 + a[2]**2 - a[0]**2) / (2 * a[1] * a[2])
b_theta = (b[1]**2 + b[2]**2 - b[0]**2) / (2 * b[1] * b[2])

sim = [sorted([(t[y]**2+t[z]**2-t[x]**2)/(2*t[y]*t[z]) for x,y,z in [[0,1,2],[1,2,0],[2,0,1]]]) for t in [a, b]]

print(sim)
assert sim[0] == sim[1]
print('Triangles a and b are similar!')

sim = [sorted([(t[y]**2+t[z]**2-t[x]**2)/(2*t[y]*t[z]) for x,y,z in [[0,1,2],[1,2,0],[2,0,1]]]) for t in [a, c]]
print(sim)
assert sim[0] != sim[1]
print('Triangles a and c are not equal')
