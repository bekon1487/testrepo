import numpy as np
rng = np.random.default_rng()

# task 1 

A = rng.random(100)

print('среднее арифметическое:', '\n', np.average(A), '\n',
      'медиана:', '\n', np.median(A), '\n',
      'стандартное отклонение:', '\n', np.std(A))

# task 2

X = rng.random((3,3), float)
Y = rng.random((3,3), float)

Res = np.dot(X, Y)

x = np.reshape(X, -1)
y = np.reshape(Y, -1)

result = []

for i in range(9):
    result.append(x[i]*y[i])

print('матричное умножение:', '\n', Res, '\n',
      'поэлементное:', '\n', result)