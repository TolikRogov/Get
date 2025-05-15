import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = [float(line.strip()) * 3.3 / 255 for line in file if line.strip()]
    return np.array(data)

def load_settings(file_path):
    with open(file_path, 'r') as file:
        settings = [float(line.strip()) for line in file if line.strip()]
    return settings

voltage_data = load_data('data.txt')
dt, max_voltage = load_settings('settings.txt')
time_points = np.arange(0, len(voltage_data) * dt, dt)

plt.figure(figsize=(12, 6))
plt.plot(time_points, voltage_data,
            color='blue',
            linestyle='-',
            linewidth=1.5,
            marker='o',
            markersize=4,
            markevery=10,
            label='V(t)')

plt.axis([time_points.min(), time_points.max(), voltage_data.min(), None])

plt.title('Процесс заряда и разряда конденсатора в RC-цепочке',
          fontsize=14,
          wrap = True)
plt.xlabel('Время, с', fontsize=12)
plt.ylabel('Напряжение, В', fontsize=12)

ax = plt.gca()
ax.grid(
    visible=True,
    which='major',
    linestyle='--',
    alpha=0.6)

ax.grid(
    visible=True,
    which='minor',
    linestyle=':',
    alpha=0.4)

ax.minorticks_on()
plt.legend(loc='upper right', fontsize=10)

charge_end = np.argmax(voltage_data)
discharge_end = len(voltage_data) - 1

t_charge = charge_end * dt
t_discharge = (discharge_end - charge_end) * dt
plt.text(0.8 * max(time_points),
         0.9 * max(voltage_data),
         f'Время заряда = {t_charge} с',
         fontsize=10,
         color='black',
         horizontalalignment='center')

plt.text(0.8 * max(time_points),
         0.8 * max(voltage_data),
         f'Время разряда = {t_discharge} с',
         fontsize=10,
         color='black',
         horizontalalignment='center')

plt.tight_layout()
plt.savefig('voltage_vs_time.svg', dpi=300)
plt.show()
