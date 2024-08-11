import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 时间点和对应的位置
t = np.array([0, 1, 2, 3, 4, 5])  # 假设这些是时间点
y = np.array([0, 0.5, 2, 1, 2.5, 0])  # 对应时间点的位置

# 创建三次样条插值，假设边界条件为自然边界（二阶导数在边界为0）
cs = CubicSpline(t, y, bc_type='clamped')

# 生成用于绘图的细致时间点
t_fine = np.linspace(0, 5, 500)
y_fine = cs(t_fine)
v_fine = cs(t_fine, 1)  # 速度（一阶导数）
a_fine = cs(t_fine, 2)  # 加速度（二阶导数）

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
