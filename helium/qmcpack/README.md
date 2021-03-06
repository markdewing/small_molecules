The `he_simple.xml` file contains the simplest wavefunction that includes electron correlation.  It performs a Variational Monte Carlo (VMC) run on that wavefunction.

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


### Optimizing parameters

The `he_simple_opt.xml` input file optimizes the variational parameters (only one in this case), and then does a final VMC run with the optimized wavefunction.

The file performs 10 iterations of the optimization loop.  After running with QMCPACK, there should be a number of files in the directory with different series (the part the filename with `s000`, `s001`, etc.).   Series 000-009 are the optimization iterations, and series 010 is the final VMC run.   The file `He.s009.opt.xml` contains the wavefunction with optimized parameters.

The `qmca` script can plot the average energy for each run.  Use `qmca --plot --quantities LocalEnergy He.s0*.scalar.dat`.  Because this is a simple wavefunction with one parameter, only the first iteration really reduced the energy.

### Diffusion Monte Carlo

The `he_simple_dmc.xml` input file performs a Diffusion Monte Carlo (DMC) run.  It starts with VMC to warm up the walkers, and then does DMC.  There will be two series of output files - 000 for the VMC and 001 for the DMC.

A single helium atom has one electron of each spin, thus there are no nodes and DMC should give the exact (non-relativistic) ground state energy.   Also in this case, the quality of the wavefunction should not affect the final answer, but can affect the variance.  This input file uses the unoptimized Jastrow parameter.  As an exercise, use the optimized Jastrow parameter instead, and see how the variance of the energy changes.

### Wavefunction Forms
#### B-Splines
The file `he_bspline_jastrow.xml` uses a B-spline form for the electron-electron Jastrow factor.   The file is set to do a run to optimize the B-spline coefficients.

#### Orbitals from GAMESS
First, run GAMESS and save the output file (redirect the output to a file, `rungms he.inp > he.out`)

Use `convert4qmc` in the QMCPACK binary directory to read that output file and convert the orbitals to a form that QMCPACK can read.  Run `convert4qmc -gamessAscii he.out`.   This will produce two output files, `sample.Gaussian-G2.ptcl.xml`, which sets up the ionic and electronic coordinates.  For now this can be ignored.  The second output file, `sample.Gaussian-G2.xml` contains the wavefunction.  In addition to the orbitals, this wavefunction contains some default Jastrow factors.

The file `he_from_gamess.xml` contains the `<wavefunction>` portion of the orbitals (from `sample.Gaussian-G2.xml`) put into the original He input file.  Also, since the He atom has only 2 electrons, the same spin e-e Jastrow was removed.

Using the wavefunction with no Jastrow factor in QMC should reproduce the Hartree-Fock energy from GAMESS.  (Note that the Jastrow factor pieces need to be commented out.  Because of default cusp conditions, simply setting all the coefficients to zero is not quite the same.)
The HF energy ('TOTAL ENERGY' in he.out) is -2.86162.  From QMCPACK, I get -2.8642 +/- 0.0015.  The error bars given are one-sigma, so this is still probably okay.  Do more runs, and run longer to check (increase `<nblocks>` in the VMC section).

The `he_from_gamess.xml` input file does a VMC run by default.  The optimization input code is commented out.  Uncomment it and run to optimize the parameters.  The number of samples (`<parameter name="samples">`) may need to be increased for better optimization convergence.
