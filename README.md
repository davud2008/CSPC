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