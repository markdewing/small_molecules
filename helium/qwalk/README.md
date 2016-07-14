
#### Orbitals from GAMESS
Run GAMESS on `../gamess/he_ext.inp`.  (QWalk seems to require that the basis set be explicitly specified)
In addition to the output file (from saving standard out to `he.out`), copy the `he_ext.dat` file from the scratch location.

Run the converter (in `src/converter/gamess2qmc-Linux`), giving it the base name (`he_ext`) as a command line argument.  There should be a number of output files produced.

The file `he.hf` is the top level QWalk input file. It contains no reference a Jastrow factor.
Running it should reproduce the HF energy from GAMESS.


#### Running QWalk
Use `qwalk-Linux he.hf` to run QWalk.  The output is stored in `he.hf.o`  Look for the average energy there.

