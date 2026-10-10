# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
- Branching practice complete.
## PW1 - Lab A: Reproducible Foundations

*What I built:*
- Created the CSPC repository structure.
- Set up a reproducible Conda environment with Python, NumPy and pytest.
- Implemented and tested a radioactive decay simulation.
- Compared the performance of the pure-Python loop and NumPy versions.

*Speed comparison (loop vs NumPy):*
- loop : 1.9664 s
- numpy : 0.0002 s
- speed-up: 12349.94 x faster

*Tests:* all passing? yes

*Conclusion:*
- The environment and radioactive decay simulation were set up successfully.
- All three tests passed successfully.
- The NumPy implementation was much faster than the pure-Python loop.
## PW1 - Lab B: Data, Plotting, and Automation

*What I did:*
- Loaded the observed radioactive decay data from decay_observed.csv.
- Compared the observed data with the analytical decay law using lambda = 0.3.
- Created a side-by-side plot of the observed data and the analytical curve.

*Result:*
- The observed data follows the same decreasing exponential trend as the analytical curve.
- The two shapes match well visually.

*Snakemake:*
- The Snakemake pipeline builds figure.png from decay_observed.csv by running plot.py.
- It rebuilds the figure when the input or script changes and does nothing when everything is up to date.
## PW2 --- Lab A: Motion from Tracking Data

*Mean acceleration:*  
The measured mean acceleration was approximately -8.58 m/s², which is reasonably close to the expected gravitational acceleration of -9.81 m/s².

*Noise observation:*  
The acceleration was much noisier than the position because differentiation amplifies noise in the measured data.

*Integration result:*  
After integrating the noisy acceleration back to velocity and then position, the recovered position was close to the original position. The largest difference was approximately 0.785 m, which is within about 1 metre.

*Plot:*  
The motion.png figure shows position, velocity, and acceleration as three stacked panels. A dashed line at -9.81 m/s² is shown on the acceleration panel.

### PW2 — Lab B

#### Part 2A — Easy convex function

Gradient Descent, Newton's method, and SLSQP all found the minimum near x = 3, with f(x) = 1.

#### Part 2B — Harder landscape

The methods can give different results depending on the starting point. Newton's method from x0 = 0 found a stationary point near x = 0.1699, where the second derivative is negative, so it is a local maximum. From x0 = 2, Newton's method found a local minimum near x = 1.1309.

The starting point and optimization method affect the result.
### Part 4 — Chemical Equilibrium

The equilibrium extent was found using Newton's method and SLSQP. Both methods gave approximately the same result: x = 0.66385.

The equilibrium amounts are:
- H2 = 0.33615 mol
- I2 = 0.33615 mol
- HI = 1.32770 mol

The equilibrium composition was calculated using H2 = 1 - x, I2 = 1 - x, and HI = 2x. The plot was saved as equilibrium.png.
#### Part 5 — Titration Analysis 
The equivalence point was estimated by calculating the slope of the pH curve using numpy.gradient(pH, V).

- Equivalence point: *50.0 mL*
- Maximum slope: *4.0*

The pH curve and its slope were plotted, and the figure was saved as titration.png.

### Exercise 3 — Normality tests

I used the Shapiro–Wilk test to check whether the four continuous variables follow a normal distribution. I used a significance level of 0.05.

The p-values for age, cholesterol (chol), resting blood pressure (trestbps), and maximum heart rate (thalach) were all below 0.05. Therefore, I rejected the null hypothesis of normality for all four variables.

The results suggest that none of the four variables is normally distributed according to the Shapiro–Wilk test.

### Exercise 4 — Maximum heart rate comparison

I divided the patients into two groups using the target variable: target = 1 for patients with heart disease and target = 0 for healthy patients.

The mean maximum heart rate was 139.26 for patients with heart disease (SE = 1.92, n = 139) and 158.38 for healthy patients (SE = 1.50, n = 164).

I used the Mann–Whitney U test because the Shapiro–Wilk tests indicated departures from normality. The test gave U = 5806.50 and p < 0.001.

There is a statistically significant difference between the two groups. Patients with heart disease had a lower mean maximum heart rate in this dataset. The error-bar plot is consistent with this result.

The analysis shows an association, not proof that heart disease itself causes the lower maximum heart rate.

### Exercise 6 — Naive chemical analysis

I used Spearman correlation to investigate the association between each chemical and malignancy.

Benzene had a correlation of 0.3765 (p < 0.001), while cadmium had a much stronger correlation of 0.8849 (p < 0.001). Based on the naive analysis alone, cadmium appears more strongly associated with malignancy.

However, correlation does not establish causation, so I investigated the possible influence of pollution index.

### Exercise 7 — Controlling for pollution

I restricted the dataset to patients with pollution index between 40 and 60. This left 199 patients.

Within this subgroup, the Spearman correlation between benzene and malignancy was 0.7093 (p < 0.001). The correlation between cadmium and malignancy was 0.2972 (p < 0.001).

The association with cadmium became much weaker, while the association with benzene became stronger. This suggests that pollution may explain part of the naive association between cadmium and malignancy.

This restricted analysis supports benzene as the stronger candidate within the selected pollution range, but it does not by itself prove causation. Further analysis of the synthetic dataset and its confounding variables is needed before identifying the actual causal chemical.

### Bonus — Target category entropy

I calculated the entropy of the target category using the proportions of healthy patients and patients with heart disease.

The entropy was 0.9951 bits, which is close to the maximum of 1 bit for a binary category. This means the two target categories are relatively balanced, so guessing the category is fairly unpredictable.