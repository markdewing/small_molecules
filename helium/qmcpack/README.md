The `he_simple.xml` file contains the simplest wavefunction that includes electron correlation.  It performs a Variational Monte Carlo run on that wavefunction.

There are two parts to the wavefunction:

1. Electron orbital using a Slater Type Orbital (STO)
2. Electron-electron Jastrow factor using a simple Pade form.

The exponent of the STO should be fixed to the nuclear charge (Z=2) to cancel the -Z/r Coulomb term between the electrons and the nucleus.
The Jastrow factor has one adjustable variational parameter (b).
