import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 给定的时间点和对应的位置
t = np.array([0, 3])
y = np.array([0, 225])

# 创建三次样条曲线，指定起点和终点的一阶导数为0
cs = CubicSpline(t, y, bc_type='clamped')

# 用于绘图的细分时间点
t_fine = np.linspace(0, 3, 300)
y_fine = cs(t_fine)

# 计算速度和加速度
v_fine = cs(t_fine, 1)  # 1表示求一阶导数
a_fine = cs(t_fine, 2)  # 2表示求二阶导数

# 绘制位置，速度，加速度图
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, y, 'o', label='Data Points')
plt.plot(t_fine, y_fine, label='Position (Cubic Spline)')
plt.legend()
plt.title('Position vs Time')

plt.subplot(3, 1, 2)
plt.plot(t_fine, v_fine, label='Velocity')
plt.legend()
plt.title('Velocity vs Time')

plt.subplot(3, 1, 3)
plt.plot(t_fine, a_fine, label='Acceleration')
plt.legend()
plt.title('Acceleration vs Time')

plt.tight_layout()
plt.show()
