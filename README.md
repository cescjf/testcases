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

##Setup
All calculations are performed on a NACA0012 airfoil mesh as depicted below.
![NACA0012](doc/mesh.png)

##Structure
This folder first splits into 3 subfolders that cover the different Sensitivity types
- [./shapesens](shapesens) covers sensitivity with respect to shape variables [README](./shapesens/README.md)
- [./machsens](machsens) convers LD sensitivity with respect to the free-stream mach number [README](./machsens/README.md)
- [./alphasens](alphasens) covers LD sensitivity with respect to the angle of attack [README](./alphasens/README.md)


##Results

<table class="tg" style="undefined;table-layout: fixed; width: 510px">
<colgroup>
<col style="width: 79px">
<col style="width: 56px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
<col style="width: 45px">
</colgroup>
  <tr>
    <th class="tg-031e" colspan="2" rowspan="2"></th>
    <th class="tg-hgcj" colspan="3">Euler</th>
    <th class="tg-amwm" colspan="3">Laminar</th>
    <th class="tg-amwm" colspan="3">RANS</th>
  </tr>
  <tr>
    <td class="tg-s6z2">s</td>
    <td class="tg-s6z2">α</td>
    <td class="tg-s6z2">Ma</td>
    <td class="tg-baqh">s</td>
    <td class="tg-baqh">α</td>
    <td class="tg-baqh">Ma</td>
    <td class="tg-baqh">s</td>
    <td class="tg-baqh">α</td>
    <td class="tg-baqh">Ma</td>
  </tr>
  <tr>
    <td class="tg-e3zv" rowspan="2">ALE</td>
    <td class="tg-031e">Direct</td>
    <td class="tg-031e">&#10003</td>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
  </tr>
  <tr>
    <td class="tg-031e">Adjoint</td>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
    <td class="tg-031e"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
  </tr>
  <tr>
    <td class="tg-9hbo" rowspan="2">Embedded</td>
    <td class="tg-yw4l">Direct</td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
  </tr>
  <tr>
    <td class="tg-yw4l">Adjoint</td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
    <td class="tg-yw4l"></td>
  </tr>
</table>
