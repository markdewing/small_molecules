The `he_simple.xml` file contains the simplest wavefunction that includes electron correlation.  It performs a Variational Monte Carlo run on that wavefunction.

There are two parts to the wavefunction:

1. Electron orbital using a Slater Type Orbital (STO)
2. Electron-electron Jastrow factor using a simple Pade form.

The exponent of the STO should be fixed to the nuclear charge (Z=2) to cancel the -Z/r Coulomb term between the electrons and the nucleus.
The Jastrow factor has one adjustable variational parameter (b).

#### Running QMCPACK
Use `qmcpack he_simple.xml` to run QMCPACK.  Afterwards, there should be a number of new files in the directory.


#### Analyzing QMCPACK output
One the output files, `He.s000.scalar.dat` contains scalar values, such as the local energy (first column).  There should be one line of data for each block (the file should have `<blocks>` lines, plus one for the header).

To analyze this data, use the `qmca` script (in the `nexus/executables` directory) on the scalar data file: `qmca He.s000.scalar.dat`.  It should print out average values for each scalar along with an error estimate.

The `qmca` script has other feature (use `qmca -h` to see the help).  For instance, to plot a trace of the local energy (matplotlib must be installed): `qmca --quantities LocalEnergy --trace He.s000.scalar.dat`.
