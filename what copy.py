import math


def mdm_udl(beam, L1, L2, w1, w2):
    iteration = 0 #starts at zero
    #assume constant beam
    K1 = L1**-1
    K2 = L2**-1

    #Distribution Factors
    DF_AB = 1.0
    DF_BA = K1/(K1 + K2)
    DF_BC = 1-DF_BA
    DF_CB = 1.0

    #fixed end moments
    FEM_AB = w1 * L1**2 / 12 
    FEM_BA = -FEM_AB
    FEM_BC = w2 * L2**2 / 12
    FEM_CB = -FEM_BC

    #Unbalanced Moment
    M_AB = FEM_AB
    M_BA = FEM_BA
    M_BC = FEM_BC
    M_CB = FEM_CB

    C_AB = FEM_AB
    C_BA = FEM_BA
    C_BC = FEM_BC
    C_CB = FEM_CB

    while True:
        iteration += 1
        JOINT_Bsum = C_BA + C_BC
        FEM_AB = -C_AB * DF_AB
        FEM_BA = -(JOINT_Bsum) * DF_BA
        FEM_BC = -(JOINT_Bsum) * DF_BC
        FEM_CB = -C_CB * DF_CB

        C_AB = FEM_BA/2
        C_BA = FEM_AB/2  
        C_BC = FEM_CB/2
        C_CB = FEM_BC/2  

        M_AB += FEM_AB + C_AB
        M_BA += FEM_BA + C_BA
        M_BC += FEM_BC + C_BC
        M_CB += FEM_CB + C_CB

        tol_AB = FEM_AB - math.floor(FEM_AB)
        tol_BA = FEM_BA - math.floor(FEM_BA)
        tol_BC = FEM_BC - math.floor(FEM_BC)
        tol_CB = FEM_CB - math.floor(FEM_CB)


        if tol_AB <0.00001 or tol_BA <0.00001 or tol_BC <0.00001 or tol_CB <0.00001 and iteration == 25:
            M_AB -= C_AB
            M_BA -= C_BA
            M_BC -= C_BC
            M_CB -= C_CB

            return round(M_AB,4), round(M_BA, 4), round(M_BC,4), round(M_CB,4)
            break


x, y, z, w = mdm_udl(1, 5 , 6, 20, 30)
print(x, y, z, w)
x, y, z, w = mdm_udl(2, 5 , 10, 31.42, 34.5)
print(x, y, z, w)
x, y, z, w = mdm_udl(3, 10 , 3, 61, 52)
print(x, y, z, w)