import itertools
m = []
X = [2,4,5,6]
Y = [9,2,7,8]
for x_1, y_1 in zip(X,Y):
        for x_2, y_2 in zip(X,Y):
                if x_1 != x_2:
                        m.append((y_2-y_1)/(x_2-x_1))
print m

b = []
m_1 = []
for i in m:
        for x_1, y_1 in zip(X,Y):
                for x_2, y_2 in zip(X,Y):
                        if x_1 != x_2:
                                a = i*x_2
                                f = y_2 - a
                                b.append(f)
                                m_1.append(m)
                                print b
                                print m_1

for i,j in zip(m_1,b):

        for a,b in zip(X, Y):

