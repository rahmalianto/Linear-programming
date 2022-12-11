import numpy as np
from scipy.optimize import linprog

A = np.array([[3, 3, 5], [3, 4, 5], [11, 10, 8], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])
b = np.array([230000, 250000, 600000, 0, 0, 0])
c = np.array([-300, -400, -500])

res = linprog(c, A_ub=A, b_ub=b, method='simplex')
optimal_pakan_1mm = round(res.x[0])
optimal_pakan_05mm = round(res.x[1])
optimal_pakan_halus = round(res.x[2])
optimal_keuntungan = round(res.fun*-1)

print('variable optimal untuk setiap pakan adalah:', optimal_pakan_1mm, optimal_pakan_05mm, optimal_pakan_halus)
print('keuntungan optimal adalah:', optimal_keuntungan)