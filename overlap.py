import numpy as np
import math
import matplotlib.pyplot as plt
'''
R = 31E-9

multi_fac = []
y = []
for i in range(1,50):
   
    d = 1E-9 * i
    #c = 8 * R**2 * math.acos(d/(2*R)) + 12 * R**2 * math.acos(( (2* d**2)**(1/2)) / (2*R)  )
    if d <2 *R and d > 1.414 * R:
       N = round(2*R/d)-1
       c = 0
       for j in range(1,N):
           c = c + 2 * R**2 * math.acos(d*j/(2*R)) 

       multi_fac.append(((4*c)/(3.14*R*R))-2)
       b = (d/R) 
       y.append(b)

    if d < 2*R and d < 1.414 *R:
       N = round(2*R/d)-1
       c = 0
       for j in range(1,N):
           c = c + 2 * R**2 * math.acos(d*j/(2*R))
       N_d = round(2*R/1.414*d)-1
       e = 0
       for k in range(1,N_d):
           e = e + 2 * R**2 * math.acos(1.414*d*k/(2*R))
       multi_fac.append(((4*(c+e))/(3.14*R*R)))
       b = (d/R) 
       y.append(b)
       

    
#x =  math.acos( 1/2 * R *(2* d**2)**(1/2) )
    #print (x/(3.14*R*R))

'''  
   
 
def find_overlap(R, d):
    N_HV = round((2*R/d)) #2*
    #print (N_HV)
    Area = 0
    
    for i in range(-N_HV,N_HV+1):
        for j in range(-N_HV,N_HV+1):
            
            di = ((abs(i)*d)**2+(abs(j)*d)**2)**(0.5)
            
            try:
                if di != 0:
                    if di < 1000e-9 :
                #cosin = math.acos(di/(2*R))

                       A1 =  2 * (R**2) * math.acos(di/(2*R))
                       A2 =  0.5 * di*(4*R**2 - di**2 )**(0.5)
                       #print (A1-A2)

                       
                       Area = Area + (A1 - A2)
                           
                #Area = Area + (2 * (R**2) * cosin)
                
            except (ValueError):
                continue
            
             
    return Area
   
 

def cal_all(R,No,LST,D):
   #R = 60 nm
   #d = 1 nm - 65 nm
   overlap_area = []
   ratio = []
   ratio_ob = []
   
   
   for i in range(1,No):
       #d = i * 1e-9;
       d = i * LST
       
       #print (d)
       overlap = find_overlap(R,d)
       #print (overlap)
       if overlap != 0:
           overlap_area.append(D*(overlap/(3.14*R*R))) # removed +1 multiply with dosage
           ratio.append(d/R)
           
       if d == 2*R:
           break
           
           
    
      
   return ratio, overlap_area

def dose_cal(R):
    OD_at_E = 0.5
    Io = 15
    Io_I = Io * (1- math.exp(-OD_at_E))

    A = math.pi * R* R
    d = 100
    
    rho = 2.1 #g/cc

    mass_per_pixel = (rho * A * d * 0.001)/(1e21)

    E = 192 #eV
    eff = 0.3
    dose_rate = Io_I * E * (1.6e-19)/(eff*mass_per_pixel)
        
    t = 100 #ms exposure time
    
    D = (t * dose_rate)/1000
    
    print (D)
    

    #D = (0.59 * E * (t/eff) )/(rho * A *d)

    return D



def dose_cal_2(R):
    return 0 
#d = dose_cal(500e-9)


x, multi_fac = cal_all(30e-9, 120, 0.5e-9,dose_cal(30))

x1, multi_fac1 = cal_all(250e-9, 500, 1e-9,dose_cal(250))

x2, multi_fac2 = cal_all(500e-9, 1000, 1e-9,dose_cal(500))



def runner():
    Radius = [30e-9, 60e-9, 120e-9, 250e-9, 480e-9, 500e-9]
    low_stepsize = [1, 1, 1, 1, 1, 1]
    No_points = []



#x= 1-0.5*(np.array(x))
#x1= 1-0.5*(np.array(x1))
#x2= 1-0.5*(np.array(x2))

x=np.array(x)
#plt.plot(x,multi_fac, "o--", color = 'black', linewidth= 2)

plt.plot(x,multi_fac,x1,multi_fac1,x2,multi_fac2, linewidth= 4)


#plt.plot(Z_real,Z_imaginary,'o')
#plt.xscale("log")
plt.yscale("log")
plt.ylabel('Weight factor (k)',fontsize = 24)
#plt.ylabel('Dose (MGy)',fontsize = 24)
plt.xlabel('d/R',fontsize = 24)
#plt.legend(["62 nm","500 nm","1000 nm"])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.legend(["60 nm","500 nm","1000 nm"], loc='upper right', frameon=False, fontsize=15)
#plt.title("Weight factor vs step size", fontsize = 15)
plt.show()
