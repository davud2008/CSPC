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