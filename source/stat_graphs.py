# Make a graph of P_{hysicalPower}(S_{trength})=\left\{0 \le S_{trength}<100:0+1\left|S_{trength}-0\right|\right\}
#

import matplotlib.pyplot as plt
import numpy as np

# Create a range of values for the strength
strength = np.arange(0, 100, 1)

# Create a range of values for the physical power P_{hysicalPowerBonus}(P_{hysicalPower})=\left\{0 \le P_{hysicalPower}<5:-0.8+0.1\left|P_{hysicalPower}-0\right|,5 \le P_{hysicalPower}<7:-0.3+0.05\left|P_{hysicalPower}-5\right|,7 \le P_{hysicalPower}<11:-0.2+0.03\left|P_{hysicalPower}-7\right|,11 \le P_{hysicalPower}<15:-0.08+0.02\left|P_{hysicalPower}-11\right|,15 \le P_{hysicalPower}<50:0+0.01\left|P_{hysicalPower}-15\right|,50 \le P_{hysicalPower}<100:0.35+0.005\left|P_{hysicalPower}-50\right|\right\}
physical_power = np.piecewise(strength, [strength < 5, (strength >= 5) & (strength < 7), (strength >= 7) & (strength < 11), (strength >= 11) & (strength < 15), (strength >= 15) & (strength < 50), strength >= 50], [-0.8+0.1*abs(strength-0), -0.3+0.05*abs(strength-5), -0.2+0.03*abs(strength-7), -0.08+0.02*abs(strength-11), 0+0.01*abs(strength-15), 0.35+0.005*abs(strength-50)])

# Plot the graph
plt.plot(strength, physical_power)
plt.xlabel('Strength')
plt.ylabel('Physical Power')
plt.title('Physical Power vs Strength')
plt.show()