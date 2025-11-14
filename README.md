# the-phiQKD-protocol-codes

This repository contains the simulation codes and numerical analysis associated with our work on Generalized State Discrimination (GSD) and its application to a tunable B92-type quantum key distribution scheme, resulting in the proposed phiQKD protocol.

The project develops:

- A generalized measurement strategy where the probabilities of incorrect and inconclusive outcomes are optimally balanced.

- A flexible QKD protocol (phiQKD) that adapts to channel parameters by tuning the measurement angle ϕ.

Simulations for error rates, sifted key rates, and secure key rates under various noise and channel conditions.

Paper:
The full theoretical framework and results are presented in our arXiv preprint: 
[Generalized State Discrimination for Tunable Quantum Key Distribution: The phiQKD Protocol](https://arxiv.org/abs/2511.06488) 

---

#  Repository Structure
- [CSV_files](./CSV_files/)
- [Colab notebooks](./Colab_notebooks)
    - [Generalized_state_discrimination.ipynb](./Colab_notebooks/Generalized_state_discrimination.ipynb)
    - [GSD_to_phiQKD_protocol.ipynb](./Colab_notebooks/GSD_to_phiQKD_protocol.ipynb)
- [Figures](./Figures/)
    - [Improvement_vs_theta.png](./Figures/Improvement_vs_theta.png)
    - [difference_vs_theta.png](./Figures/difference_vs_theta.png)
    - [phiQKD_plot.png](./Figures/phiQKD_plot.png)
    - [phi_optimal_vs_theta.png](./Figures/phi_optimal_vs_theta.png)
    - [quantum_circuit.png](./Figures/quantum_circuit.png)
    - [skr_vs_theta.png](./Figures/skr_vs_theta.png)
- [Python_files](./Python_files/)
    - [main.py](./Python_files/main.py)
    - [plot_drawer.py](./Python_files/plot_drawer.py)
    - [csv_generator_plots.py](./Python_files/csv_generator_plots.py)
- [.gitignore](./gitignore)
- [.python-version](./python-version)
- [LICENSE](./LICENSE)
- [README.md](./README.md)
- [pyproject.toml](./pyproject.toml)
- [uv.lock](./uv.lock)

---

