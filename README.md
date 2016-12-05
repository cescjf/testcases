#Sensitivity Analysis test-cases

This folder contains all test-cases for the Sensitivity Analysis framework of [AERO-F](http://frg.bitbucket.org/aero-f/index.html).


##General

A variety od parameter cobinations has to be tested in order to ensure full fuynctionality of the SA framework.
All calculations evaluate the Sensitivity of the Lift and Drag(LD) with respect to the parameters lsuited below.

We test the follwowing features:

- Equation type
   - Euler equations
   - Laminar Navier-Stokes equations
   - RANS equations
- Time formulations
  - Eulerian
  - Arbitrary Lagrangian Eulerian
- Sensitivity Analysis Method
  - Direct SA
  - Adjoint SA
- Sensitivity Type
  - Shape sensitivity
  - Mach sensitivity
  - AoA sensitivity

##Structure
This folder first splits into 3 subfolders that cover the different Sensitivity types
- [./shapesens](shapesens) covers sensitivity with respect to shape variables [README](./shapesens/README.md)
- [./machsens](machsens) convers LD sensitivity with respect to the free-stream mach number [README](./machsens/README.md)
- [./alphasens](alphasens) covers LD sensitivity with respect to the angle of attack [README](./alphasens/README.md)
