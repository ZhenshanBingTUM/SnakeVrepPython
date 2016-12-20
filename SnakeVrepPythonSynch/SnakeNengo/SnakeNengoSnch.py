# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:56:17 2016

@author: zhenshan
"""


#import nengo
import vrep                  #V-rep library
import sys
import time                #used to keep track of time
import numpy as np         #array library
import math
from math import sqrt
import matplotlib.pyplot as plt   #used for image plotting

PI=math.pi  #pi=3.14..., constant
AMPLITUDE = 60
AI = 10
STEPSIZE = 0.01
THETA = 0
OMEGA_v = 4
OMEGA_h = 2
DELTA=-0.5*np.pi
u=5

# Function Declare

# CPG differential equation    
def AmpFun1(t, amplitude1, amplitude2):
    dydt= AI * (AI/4 * (AMPLITUDE - amplitude2) - amplitude1)
    return dydt
    
def AmpFun2(t, amplitude1, amplitude2):
    dydt = 2 * amplitude1;
    return dydt

def RK_AMP(t, amplitude):
    k1=[0]*2
    k2=[0]*2
    k3=[0]*2
    k4=[0]*2    
    k1[0] = AmpFun1(t, amplitude[0], amplitude[1])
    k2[0] = AmpFun1(t + STEPSIZE/2, amplitude[0] + k1[0]*STEPSIZE/2, amplitude[1] + k1[0]*STEPSIZE/2)    
    k3[0] = AmpFun1(t + STEPSIZE/2, amplitude[0] + k2[0]*STEPSIZE/2, amplitude[1] + k2[0]*STEPSIZE/2)
    k4[0] = AmpFun1(t + STEPSIZE,   amplitude[0] + k3[0]*STEPSIZE,   amplitude[1] + k3[0]*STEPSIZE)
    k1[1] = AmpFun2(t, amplitude[0], amplitude[1])
    k2[1] = AmpFun2(t + STEPSIZE/2, amplitude[0] + k1[1]*STEPSIZE/2, amplitude[1] + k1[1]*STEPSIZE/2)
    k3[1] = AmpFun2(t + STEPSIZE/2, amplitude[0] + k2[1]*STEPSIZE/2, amplitude[1] + k2[1]*STEPSIZE/2)
    k4[1] = AmpFun2(t + STEPSIZE,   amplitude[0] + k3[1]*STEPSIZE,   amplitude[1] + k3[1]*STEPSIZE)
    for i in range(0,2):
        amplitude[i] = amplitude[i] + STEPSIZE * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
    return amplitude

# Horizonal Wave Functions    
def myFun1(t, y1, y2, y3):
    dydt = OMEGA_h + (-1 * y1 + y2) * u + THETA
    return dydt
    
def myFun2(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun3(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt

def myFun4(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun5(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun6(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun7(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun8(t, y1, y2, y3):
    dydt = OMEGA_h + (1 * y2 - 1 * y3) * u - THETA
    return dydt
# Vertical Wave Functions    
def myFun9(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt

def myFun10(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun11(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun12(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun13(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt    
    
def myFun14(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun15(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y1 - 2 * y2 + y3) * u
    return dydt
    
def myFun16(t, y1, y2, y3):
    dydt = OMEGA_v + (1 * y2 - 1 * y3) * u - THETA
    return dydt
    
def RK_fun_h(t, y):
    k1=[0]*8
    k2=[0]*8
    k3=[0]*8
    k4=[0]*8  
    k1[0] = myFun1(t, y[0], y[1], y[2])
    k2[0] = myFun1(t + STEPSIZE/2, y[0] + k1[0]*STEPSIZE/2, y[1] + k1[0]*STEPSIZE/2, y[2] + k1[0]*STEPSIZE/2)
    k3[0] = myFun1(t + STEPSIZE/2, y[0] + k2[0]*STEPSIZE/2, y[1] + k2[0]*STEPSIZE/2, y[2] + k2[0]*STEPSIZE/2)
    k4[0] = myFun1(t + STEPSIZE,   y[0] + k3[0]*STEPSIZE,   y[1] + k3[0]*STEPSIZE,   y[2] + k3[0]*STEPSIZE)
    k1[1] = myFun2(t, y[0], y[1], y[2])
    k2[1] = myFun2(t + STEPSIZE/2, y[0] + k1[1]*STEPSIZE/2, y[1] + k1[1]*STEPSIZE/2, y[2] + k1[1]*STEPSIZE/2)
    k3[1] = myFun2(t + STEPSIZE/2, y[0] + k2[1]*STEPSIZE/2, y[1] + k2[1]*STEPSIZE/2, y[2] + k2[1]*STEPSIZE/2)
    k4[1] = myFun2(t + STEPSIZE,   y[0] + k3[1]*STEPSIZE,   y[1] + k3[1]*STEPSIZE,   y[2] + k3[1]*STEPSIZE)
    k1[2] = myFun3(t, y[1], y[2], y[3])
    k2[2] = myFun3(t + STEPSIZE/2, y[1] + k1[2]*STEPSIZE/2, y[2] + k1[2]*STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2)
    k3[2] = myFun3(t + STEPSIZE/2, y[1] + k2[2]*STEPSIZE/2, y[2] + k2[2]*STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2)
    k4[2] = myFun3(t + STEPSIZE,   y[1] + k3[2]*STEPSIZE,   y[2] + k3[2]*STEPSIZE,   y[3] + k3[2]*STEPSIZE)
    k1[3] = myFun4(t, y[2], y[3], y[4])
    k2[3] = myFun4(t + STEPSIZE/2, y[2] + k1[2]*STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2)
    k3[3] = myFun4(t + STEPSIZE/2, y[2] + k2[2]*STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2)
    k4[3] = myFun4(t + STEPSIZE,   y[2] + k3[2]*STEPSIZE,   y[3] + k3[2]*STEPSIZE,   y[4] + k3[2]*STEPSIZE)
    k1[4] = myFun5(t, y[3], y[4], y[5])
    k2[4] = myFun5(t + STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2)
    k3[4] = myFun5(t + STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2)
    k4[4] = myFun5(t + STEPSIZE,   y[3] + k3[2]*STEPSIZE,   y[4] + k3[2]*STEPSIZE,   y[5] + k3[2]*STEPSIZE)
    k1[5] = myFun6(t, y[4], y[5], y[6])
    k2[5] = myFun6(t + STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2)
    k3[5] = myFun6(t + STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2)
    k4[5] = myFun6(t + STEPSIZE,   y[4] + k3[2]*STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE)
    k1[6] = myFun7(t, y[5], y[6], y[7])
    k2[6] = myFun7(t + STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2, y[7] + k1[2]*STEPSIZE/2)
    k3[6] = myFun7(t + STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2, y[7] + k2[2]*STEPSIZE/2)
    k4[6] = myFun7(t + STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE,   y[7] + k3[2]*STEPSIZE)
    k1[7] = myFun8(t, y[5], y[6], y[7])
    k2[7] = myFun8(t + STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2, y[7] + k1[2]*STEPSIZE/2)
    k3[7] = myFun8(t + STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2, y[7] + k2[2]*STEPSIZE/2)
    k4[7] = myFun8(t + STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE,   y[7] + k3[2]*STEPSIZE)

    
    for i in range(0,8):
        y[i] = y[i] + STEPSIZE * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
    return y
    
def RK_fun_v(t, y):
    k1=[0]*8
    k2=[0]*8
    k3=[0]*8
    k4=[0]*8  
    k1[0] = myFun9(t, y[0], y[1], y[2])
    k2[0] = myFun9(t + STEPSIZE/2, y[0] + k1[0]*STEPSIZE/2, y[1] + k1[0]*STEPSIZE/2, y[2] + k1[0]*STEPSIZE/2)
    k3[0] = myFun9(t + STEPSIZE/2, y[0] + k2[0]*STEPSIZE/2, y[1] + k2[0]*STEPSIZE/2, y[2] + k2[0]*STEPSIZE/2)
    k4[0] = myFun9(t + STEPSIZE,   y[0] + k3[0]*STEPSIZE,   y[1] + k3[0]*STEPSIZE,   y[2] + k3[0]*STEPSIZE)
    k1[1] = myFun10(t, y[0], y[1], y[2])
    k2[1] = myFun10(t + STEPSIZE/2, y[0] + k1[1]*STEPSIZE/2, y[1] + k1[1]*STEPSIZE/2, y[2] + k1[1]*STEPSIZE/2)
    k3[1] = myFun10(t + STEPSIZE/2, y[0] + k2[1]*STEPSIZE/2, y[1] + k2[1]*STEPSIZE/2, y[2] + k2[1]*STEPSIZE/2)
    k4[1] = myFun10(t + STEPSIZE,   y[0] + k3[1]*STEPSIZE,   y[1] + k3[1]*STEPSIZE,   y[2] + k3[1]*STEPSIZE)
    k1[2] = myFun11(t, y[1], y[2], y[3])
    k2[2] = myFun11(t + STEPSIZE/2, y[1] + k1[2]*STEPSIZE/2, y[2] + k1[2]*STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2)
    k3[2] = myFun11(t + STEPSIZE/2, y[1] + k2[2]*STEPSIZE/2, y[2] + k2[2]*STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2)
    k4[2] = myFun11(t + STEPSIZE,   y[1] + k3[2]*STEPSIZE,   y[2] + k3[2]*STEPSIZE,   y[3] + k3[2]*STEPSIZE)
    k1[3] = myFun12(t, y[2], y[3], y[4])
    k2[3] = myFun12(t + STEPSIZE/2, y[2] + k1[2]*STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2)
    k3[3] = myFun12(t + STEPSIZE/2, y[2] + k2[2]*STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2)
    k4[3] = myFun12(t + STEPSIZE,   y[2] + k3[2]*STEPSIZE,   y[3] + k3[2]*STEPSIZE,   y[4] + k3[2]*STEPSIZE)
    k1[4] = myFun13(t, y[3], y[4], y[5])
    k2[4] = myFun13(t + STEPSIZE/2, y[3] + k1[2]*STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2)
    k3[4] = myFun13(t + STEPSIZE/2, y[3] + k2[2]*STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2)
    k4[4] = myFun13(t + STEPSIZE,   y[3] + k3[2]*STEPSIZE,   y[4] + k3[2]*STEPSIZE,   y[5] + k3[2]*STEPSIZE)
    k1[5] = myFun14(t, y[4], y[5], y[6])
    k2[5] = myFun14(t + STEPSIZE/2, y[4] + k1[2]*STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2)
    k3[5] = myFun14(t + STEPSIZE/2, y[4] + k2[2]*STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2)
    k4[5] = myFun14(t + STEPSIZE,   y[4] + k3[2]*STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE)
    k1[6] = myFun15(t, y[5], y[6], y[7])
    k2[6] = myFun15(t + STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2, y[7] + k1[2]*STEPSIZE/2)
    k3[6] = myFun15(t + STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2, y[7] + k2[2]*STEPSIZE/2)
    k4[6] = myFun15(t + STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE,   y[7] + k3[2]*STEPSIZE)
    k1[7] = myFun16(t, y[5], y[6], y[7])
    k2[7] = myFun16(t + STEPSIZE/2, y[5] + k1[2]*STEPSIZE/2, y[6] + k1[2]*STEPSIZE/2, y[7] + k1[2]*STEPSIZE/2)
    k3[7] = myFun16(t + STEPSIZE/2, y[5] + k2[2]*STEPSIZE/2, y[6] + k2[2]*STEPSIZE/2, y[7] + k2[2]*STEPSIZE/2)
    k4[7] = myFun16(t + STEPSIZE,   y[5] + k3[2]*STEPSIZE,   y[6] + k3[2]*STEPSIZE,   y[7] + k3[2]*STEPSIZE)

    
    for i in range(0,8):
        y[i] = y[i] + STEPSIZE * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
    return y




# VREP Initialization    
vrep.simxFinish(-1) # just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)

if clientID!=-1:  #check if client connection successful
    print 'Connected to remote API server'
    
else:
    print 'Connection not successful'
    sys.exit('Could not connect')

# Synchronous mode    
returnCode = vrep.simxSynchronous(clientID,1)
returnCode = vrep.simxStartSimulation(clientID, vrep.simx_opmode_blocking)
returnCode, iteration1 = vrep.simxGetIntegerSignal(clientID, 'iteration', vrep.simx_opmode_streaming)

#retrieve joints handles
joints_v = [0]*8
joints_h = [0]*8

for i in range(0, 8):
    errorCode, joints_v[i] = vrep.simxGetObjectHandle(clientID, 'snake_joint_v'+str(i+1), vrep.simx_opmode_oneshot_wait)
    errorCode, joints_h[i] = vrep.simxGetObjectHandle(clientID, 'snake_joint_h'+str(i+1), vrep.simx_opmode_oneshot_wait)

start_time = time.time()
print 'start time', start_time

amplitude=[0.25, 1]
y_h = [0, 0, 0, 0, 0, 0, 0, 0];
y_v = [0, 0, 0, 0, 0, 0, 0, 0];
index = 0
param_1=0.1
TEMP1 = 1.75
TEMP2 = 3.5
ALPHA = [0*TEMP1/8*np.pi, 1*TEMP1/8*np.pi, 2*TEMP1/8*np.pi, 3*TEMP1/8*np.pi, 4*TEMP1/8*np.pi, 5*TEMP1/8*np.pi, 6*TEMP1/8*np.pi, 7*TEMP1/8*np.pi]
BETA = [0*TEMP2/8*np.pi, 1*TEMP2/8*np.pi, 2*TEMP2/8*np.pi, 3*TEMP2/8*np.pi, 4*TEMP2/8*np.pi, 5*TEMP2/8*np.pi, 6*TEMP2/8*np.pi, 7*TEMP2/8*np.pi]


# Main Loop
while (time.time() - start_time) < 50:
    # Synchronise triger
    returnCode, iteration1 = vrep.simxGetIntegerSignal(clientID, 'iteration', vrep.simx_opmode_buffer)
    if iteration1 != 0:
        iteration1 = -1
    returnCode = vrep.simxSynchronousTrigger(clientID);
    iteration2=iteration1;
    while iteration2==iteration1:
        returnCode, iteration2=vrep.simxGetIntegerSignal(clientID,"iteration",vrep.simx_opmode_buffer);
        #iteration2=res;
        #print 'res', iteration2    
    
    t = time.time()
    tf = t + 0.1
    while (t<tf):
        y_h = RK_fun_h(t, y_h)
        y_v = RK_fun_v(t, y_v)
        amplitude = RK_AMP(t, amplitude)
        t = t + STEPSIZE 
        index = index + 1
    #print amplitude[1]
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[0], (0.7*0/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[0] + ALPHA[0]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[1], (0.7*1/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[1] + ALPHA[1]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[2], (0.7*2/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[2] + ALPHA[2]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[3], (0.7*3/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[3] + ALPHA[3]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[4], (0.7*4/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[4] + ALPHA[4]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[5], (0.7*5/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[5] + ALPHA[5]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[6], (0.7*6/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[6] + ALPHA[6]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_h[7], (0.7*7/8 + param_1)*amplitude[1]/180*np.pi*np.sin(y_h[7] + ALPHA[7]), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[0], (0.7*0/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[0] + BETA[0] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[1], (0.7*1/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[1]  + BETA[1] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[2], (0.7*2/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[2]  + BETA[2] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[3], (0.7*3/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[3]  + BETA[3] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[4], (0.7*4/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[4]  + BETA[4] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[5], (0.7*5/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[5]  + BETA[5] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[6], (0.7*6/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[6]  + BETA[6] + DELTA), vrep.simx_opmode_oneshot)
    errorCode1 = vrep.simxSetJointTargetPosition(clientID, joints_v[7], (0.7*7/8 + param_1)*amplitude[1]/2/180*np.pi*np.cos(y_v[7]  + BETA[7] + DELTA), vrep.simx_opmode_oneshot)
    #plt.plot(t, (0.7*5/8 + param_1),'r.')
    time.sleep(0.05)
    
print 'Script finished'





