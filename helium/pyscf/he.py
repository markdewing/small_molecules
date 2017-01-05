from __future__ import print_function

# PySCF from https://github.com/sunqm/pyscf
# Documentation at http://sunqm.net/pyscf/
from pyscf import gto, scf

# set up Mole object describing the geometry and basis
# built-in basis sets in pyscf/gto/basis
mol = gto.M(atom='He 0 0 0', basis='cc-pvdz')

# Set for more detail during computation
# 0 - no output
# 1 - ERROR
# 2 - WARN
# 3 - NOTE (default)
# 4 - INFO
#mol.verbose = 4

# choose Restricted Hartree Fock
mf = scf.RHF(mol)

# Run it
mf.scf()

print('HF Energy = ',mf.e_tot)
# also have
#   mf.converged - check if SCF iterations converged
#   mf.mo_energy - molecular orbital energies
#   mf.mo_coeff - molecular orbital coefficients
#print('Mo energy')
#print(mf.mo_energy)
#print('Mo coeff')
#print(mf.mo_coeff)
