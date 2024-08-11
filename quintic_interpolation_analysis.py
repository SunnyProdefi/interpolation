import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 时间点和对应的位置
t = np.array([0, 3])
y = np.array([0, 225])

# 创建五次样条曲线，设置一阶和二阶导数为0
k = 5
# bc_type需要包括四个条件，这里假设两个端点的一阶和二阶导数都为0
bc_type = ((1, 0.0), (2, 0.0)), ((1, 0.0), (2, 0.0))

# 使用make_interp_spline创建五次样条
tck = make_interp_spline(t, y, k=k, bc_type=bc_type)

# 用于绘图的细分时间点
t_fine = np.linspace(t.min(), t.max(), 300)
y_fine = tck(t_fine)
v_fine = tck(t_fine, 1)  # 速度（一阶导数）
a_fine = tck(t_fine, 2)  # 加速度（二阶导数）

# 绘制位置，速度，加速度图
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, y, 'o', label='Data Points')
plt.plot(t_fine, y_fine, label='Position (Quintic Spline)')
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
