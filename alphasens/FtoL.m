clear
close all
clc

dF(1)=-0.547
dF(2)=9.11
dF(3)=0.0

F(1)=1.55175
F(2)=53.696
F(3)=0.0


% 
alpha=0.0
beta=6


refval_force = 20852.7
% 
% %Lift values as read from file
% F(1)=6.48241e-05
% F(2)=0.0022431
% F(3)=0


sin_a = sind(alpha);
cos_a = cosd(alpha);
sin_b = sind(beta);
cos_b = cosd(beta);

dL(1) =        dF(1)*cos_a*cos_b  + dF(2)*-cos_a*sin_b + dF(3)*sin_a;
dL(2) =        dF(1)*sin_b        + dF(2)*cos_b        + dF(3)*0.0;
dL(3) =        dF(1)*-sin_a*cos_b + dF(2)*sin_a*sin_b  + dF(3)*cos_a

ddL(1) = F(1)*-cos_a*sin_b +  F(2)*-cos_a*cos_b +  F(3)*0.0;
ddL(2) = F(1)*cos_b        +  F(2)*-sin_b       +  F(3)*0.0;
ddL(3) = F(1)*-sin_a*sin_b +  F(2)*sin_a*cos_b  +  F(3)*0.0
