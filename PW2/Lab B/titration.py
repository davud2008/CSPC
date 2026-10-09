"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]
print("Volume:", V)
print("pH:", pH)

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

# Calculate the slope of the pH curve
slope = np.gradient(pH, V)

# Find the index where the slope is largest
index = np.argmax(slope)

# Find the equivalence volume
V_eq = V[index]

print("Equivalence point:", V_eq, "mL")
print("Maximum slope:", slope[index])

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
# Create two plots side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: pH versus volume
ax[0].plot(V, pH, marker="o", label="pH curve")
ax[0].axvline(V_eq, color="red", linestyle="--",
              label="Equivalence point")
ax[0].set_xlabel("Volume of base (mL)")
ax[0].set_ylabel("pH")
ax[0].set_title("Titration Curve")
ax[0].legend()
ax[0].grid(True)

# Right plot: slope versus volume
ax[1].plot(V, slope, marker="o", label="Slope")
ax[1].axvline(V_eq, color="red", linestyle="--",
              label="Equivalence point")
ax[1].set_xlabel("Volume of base (mL)")
ax[1].set_ylabel("dpH/dV")
ax[1].set_title("Slope of Titration Curve")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.savefig("titration.png")
plt.show()