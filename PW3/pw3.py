import pandas as pd

# Load the heart disease dataset
df = pd.read_csv("Heart_disease_cleveland_new.csv")

# Print the size of the dataset
print("Dataset shape:", df.shape)

# Show the first five rows
print(df.head())

# Select the four continuous variables
columns = ["age", "chol", "trestbps", "thalach"]

print("\nSelected columns:")
print(df[columns].head())

import matplotlib.pyplot as plt

# Plot distributions of the four variables
columns = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for column, ax in zip(columns, axes.flatten()):
    ax.hist(df[column], bins=15, edgecolor="black")
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("distributions.png")
plt.show()

from scipy.stats import shapiro

print("\nNormality test:")

for column in ["age", "chol", "trestbps", "thalach"]:
    statistic, p_value = shapiro(df[column])

    print(f"\n{column}")
    print(f"Shapiro-Wilk statistic: {statistic:.4f}")
    print(f"p-value: {p_value:.6f}")

    if p_value > 0.05:
        print("Verdict: approximately normal (no significant evidence against normality)")
    else:
        print("Verdict: not normally distributed (evidence against normality)")

from scipy.stats import mannwhitneyu
import numpy as np

# Split patients into two groups
disease = df[df["target"] == 1]["thalach"].dropna()
healthy = df[df["target"] == 0]["thalach"].dropna()

# Calculate means and standard errors
for name, group in [("Disease", disease), ("Healthy", healthy)]:
    mean = group.mean()
    se = group.std(ddof=1) / np.sqrt(len(group))
    print(f"{name}: mean = {mean:.2f}, SE = {se:.2f}, n = {len(group)}")

# Compare the two groups
statistic, p_value = mannwhitneyu(disease, healthy, alternative="two-sided")

print("\nMann-Whitney U test")
print(f"U statistic: {statistic:.2f}")
print(f"p-value: {p_value:.6f}")

if p_value < 0.05:
    print("Conclusion: there is a statistically significant difference.")
else:
    print("Conclusion: no statistically significant difference was detected.")

# Plot group means with standard error bars
means = [disease.mean(), healthy.mean()]
errors = [
    disease.std(ddof=1) / np.sqrt(len(disease)),
    healthy.std(ddof=1) / np.sqrt(len(healthy))
]

plt.figure(figsize=(7, 5))
plt.bar(["Disease", "Healthy"], means, yerr=errors, capsize=8)
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Mean maximum heart rate by disease status")
plt.tight_layout()
plt.savefig("thalach_comparison.png")
plt.show()

from scipy.stats import spearmanr

# Investigate the relationship between age and thalach
correlation, p_value = spearmanr(df["age"], df["thalach"])

print("\nAge vs maximum heart rate")
print(f"Spearman correlation: {correlation:.4f}")
print(f"p-value: {p_value:.6f}")

if correlation < 0:
    print("The relationship is negative.")
elif correlation > 0:
    print("The relationship is positive.")
else:
    print("No monotonic relationship was detected.")

plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Age vs maximum heart rate")
plt.tight_layout()
plt.savefig("age_thalach.png")
plt.show()

# Exercise 6: Chemical exposure mystery
import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# Load the chemical dataset
chem = pd.read_csv("chemicals_cancer.csv")

print("\nChemical dataset shape:", chem.shape)
print(chem.head())

# Calculate the association of each chemical with malignancy
for chemical in ["benzene", "cadmium"]:
    correlation, p_value = spearmanr(
        chem[chemical], chem["malignancy"]
    )

    print(f"\n{chemical}")
    print(f"Spearman correlation: {correlation:.4f}")
    print(f"p-value: {p_value:.6g}")

# Plot the relationships
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

for chemical, ax in zip(["benzene", "cadmium"], axes):
    ax.scatter(chem[chemical], chem["malignancy"], alpha=0.5)
    ax.set_xlabel(chemical)
    ax.set_ylabel("Malignancy")
    ax.set_title(f"{chemical} vs malignancy")

plt.tight_layout()
plt.savefig("chemical_associations.png")
plt.show()

# Exercise 7: Control for pollution index

# Select patients with similar pollution levels
filtered = chem[
    (chem["pollution_index"] > 40) &
    (chem["pollution_index"] < 60)
]

print("\nExercise 7: Controlling for pollution")
print("Number of selected patients:", len(filtered))

for chemical in ["benzene", "cadmium"]:
    correlation, p_value = spearmanr(
        filtered[chemical],
        filtered["malignancy"]
    )

    print(f"\n{chemical}")
    print(f"Spearman correlation: {correlation:.4f}")
    print(f"p-value: {p_value:.6g}")

# Visualise the filtered data
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

for chemical, ax in zip(["benzene", "cadmium"], axes):
    ax.scatter(
        filtered[chemical],
        filtered["malignancy"],
        alpha=0.6
    )
    ax.set_xlabel(chemical)
    ax.set_ylabel("Malignancy")
    ax.set_title(f"{chemical} (controlled pollution)")

plt.tight_layout()
plt.savefig("controlled_chemicals.png")
plt.show()

# Bonus: How unpredictable is the target category?

proportions = df["target"].value_counts(normalize=True)
entropy = -(proportions * np.log2(proportions)).sum()

print("\nBonus: Target category")
print(proportions)
print(f"Entropy: {entropy:.4f} bits")