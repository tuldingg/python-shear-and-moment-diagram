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

    print('-' *111) 
    print('|        Joint        |          A          |                     B                     |           C         |')
    print('-' *111)   
    print('|        Member       |          AB         |         BA          |          BC         |           CB        |')
    print('-' *111) 
    print(f'| Distribution Factor |{DF_AB:>14.4f}       |{DF_BA:>14.4f}       |{DF_BC:>14.4f}       |{DF_CB:>14.4f}       |')            
    print('-' *111) 
    print(f'|  Unbalanced Moment  |{FEM_AB:>15.7f} kN-m |{FEM_BA:>15.7f} kN-m |{FEM_BC:>15.7f} kN-m |{FEM_CB:>15.7f} kN-m |')
    print('-' *111)

    with open('mdm_results.txt', 'a') as file:
        file.write('-' *111 + '\n') 
        file.write('|        Joint        |          A          |                     B                     |           C         |' '\n')
        file.write('-' *111 + '\n')   
        file.write('|        Member       |          AB         |         BA          |          BC         |           CB        |' '\n')
        file.write('-' *111 + '\n') 
        file.write(f'| Distribution Factor |{DF_AB:>14.4f}       |{DF_BA:>14.4f}       |{DF_BC:>14.4f}       |{DF_CB:>14.4f}       |' '\n')            
        file.write('-' *111 + '\n') 
        file.write(f'|  Unbalanced Moment  |{FEM_AB:>15.7f} kN-m |{FEM_BA:>15.7f} kN-m |{FEM_BC:>15.7f} kN-m |{FEM_CB:>15.7f} kN-m |' '\n')
        file.write('-' *111 + '\n')

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

        print('-' *111)   
        print(f'|  Distribution: {iteration:3}  |{FEM_AB:>15.7f} kN-m |{FEM_BA:>15.7f} kN-m |{FEM_BC:>15.7f} kN-m |{FEM_CB:>15.7f} kN-m |')
        print('-' *111)
        print(f'|   Carry Over (CO)   |{C_AB:>15.7f} kN-m |{C_BA:>15.7f} kN-m |{C_BC:>15.7f} kN-m |{C_CB:>15.7f} kN-m |')

        with open('mdm_results.txt', 'a') as file:
            file.write('-' *111 + '\n')   
            file.write(f'|  Distribution: {iteration:3}  |{FEM_AB:>15.7f} kN-m |{FEM_BA:>15.7f} kN-m |{FEM_BC:>15.7f} kN-m |{FEM_CB:>15.7f} kN-m |' '\n')
            file.write('-' *111 + '\n')
            file.write(f'|   Carry Over (CO)   |{C_AB:>15.7f} kN-m |{C_BA:>15.7f} kN-m |{C_BC:>15.7f} kN-m |{C_CB:>15.7f} kN-m |' '\n')    

        if tol_AB <0.00001 or tol_BA <0.00001 or tol_BC <0.00001 or tol_CB <0.00001 and iteration == 25:
            M_AB -= C_AB
            M_BA -= C_BA
            M_BC -= C_BC
            M_CB -= C_CB
            print('-' *111)
            print('-' *111)
            print('|  No. of Iterations  |      Length 1       |      Length 2       |        UDL 1        |        UDL 2        |')
            print('-' *111)
            print(f'|         {iteration:>}          |   {L1:>15.2f} m |   {L2:>15.2f} m |{w1:>15.3f} Kn/m |{w2:>15.3f} kN/m |')
            print('-' *111)
            print('|        Beam         |      Moment AB      |      Moment BA      |      Moment BC      |      Moment CB      |')
            print('-' *111)
            print(f'|         {beam:>}           |{M_AB:>15.7f} kN-m |{M_BA:>15.7f} kN-m |{M_BC:>15.7f} kN-m |{M_CB:>15.7f} kN-m |')
            print('-' *111)
            print('\n' '\n' '\n')

            with open('mdm_results.txt', 'a') as file:
                file.write('-' *111 + '\n')
                file.write('-' *111 + '\n')
                file.write('|  No. of Iterations  |      Length 1       |      Length 2       |        UDL 1        |        UDL 2        |' '\n')
                file.write('-' *111 + '\n')
                file.write(f'|         {iteration:>}          |   {L1:>15.2f} m |   {L2:>15.2f} m |{w1:>15.3f} Kn/m |{w2:>15.3f} kN/m |' '\n')
                file.write('-' *111 + '\n')
                file.write('|        Beam         |      Moment AB      |      Moment BA      |      Moment BC      |      Moment CB      |' '\n')
                file.write('-' *111 + '\n')
                file.write(f'|         {beam:>}           |{M_AB:>15.7f} kN-m |{M_BA:>15.7f} kN-m |{M_BC:>15.7f} kN-m |{M_CB:>15.7f} kN-m |' '\n')
                file.write('-' *111 + '\n')
                file.write('\n' '\n' '\n')           
            
            break


mdm_udl(1, 5 , 6, 20, 30)
mdm_udl(2, 5 , 10, 31.42, 34.5)
mdm_udl(3, 10 , 3, 61, 52)