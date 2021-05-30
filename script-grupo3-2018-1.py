#Modelagem Computacional 2018 - Projeto
#Grupo 3: ALEXANDRE AZIS DA SILVA, LEONARDO SIMÕES, PEDRO HENRIQUE QUARESMA COELHO, RAFAEL MAGALHÃES STORCK

import math
import matplotlib.pyplot as plt

def plotaGrafico(H, m1, m2, m3):
    plt.xlabel('H')
    plt.ylabel('M')
    plt.title('H X M')
    plt.plot(H, m1, label='menor densidade mássica')
    plt.plot(H, m2, label='densidade mássica intermediária')
    plt.plot(H, m3, label='maior densidade mássica')
    plt.legend()
    plt.grid()
    plt.show()

def AS(a, b, h):
    return (a*(h-b)/b)*(b**2-(h-b)**2)**(1/2) + a*b*math.asin((h-b)/b)+(math.pi*a*b)/2

def M(p, L, As):
    return p*L*As

def main():
    H, m1, m2, m3 = [], [], [], []
    #Leitura dos valores das variaveis a,b,L,NN via teclado
    a = float(input('Digite o valor de a:  '))
    b = float(input('Digite o valor de b:  '))
    L = float(input('Digite o valor de L:  '))
    NN = int(input('Digite o valor de NN:  '))

    #Impressão dos valores das variaveis a,b,L,NN via tela
    print('\na = %.2f \nb = %.2f \nL = %.2f \nNN = %i\n' %(a, b, L, NN))

    p = []
    #Leitura de p[3] via teclado
    p.append(int(input('Digite o valor de p[1]:  ')))
    p.append(int(input('Digite o valor de p[2]:  ')))
    p.append(int(input('Digite o valor de p[3]:  ')))

    #Impressão de p[3] via tela
    print('\np[1] = %i \np[2] = %i \np[3] = %i' %(p[0],p[1],p[2]))

    #Cálculo de DeltaH
    deltaH = (2*b)/(NN-1)

    h = 0.0
    m = [0.0, 0.0, 0.0]

    for i in range(0, NN):
        h = i * deltaH
        # Cálculo de As
        As = AS(a, b, h)
        for j in range(0,3):
            #Cálculo de m[j]
            m[j] = M(p[j], L, As)
        #Impressão de h e m[3] via tela
        print('%.2f %.1f %.1f %.1f' % (h, m[0], m[1], m[2]))

        m1.append(m[0])
        m2.append(m[1])
        m3.append(m[2])
        H.append(h)
    plotaGratico(H, m1, m2, m3)

if __name__ == "__main__":
    main()
