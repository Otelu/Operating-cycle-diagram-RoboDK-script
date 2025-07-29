import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diagram_6axe.csv', encoding='latin1')

plt.figure(figsize=(12, 6))

for joint in ['J1 [°]', 'J2 [°]', 'J3 [°]', 'J4 [°]']:
    plt.plot(df['Iteration'], df[joint], label=joint)

plt.title('Operating cycle diagram')
plt.xlabel('Iteration')
plt.ylabel('Unghi [°]')
plt.legend()
plt.grid(True)
plt.show()
