# Brian 1.4 code 
# Brian is available at http://briansimulator.org/
# Tan AY, Andoni S, Priebe NJ
# A spontaneous state of weakly correlated 
# synaptic excitation and inhibition in visual cortex.
# Neuroscience. 2013 Sep 5;247:364-75. 
# doi: 10.1016/j.neuroscience.2013.05.037.

from brian import *
import time

# Subthreshold parameters for conductance based integrate-and-fire neuron
taum = 20 * msecond
taue = 5 * msecond
taui = 10 * msecond
vrest = -70 * mvolt
Ee = 0 * mvolt - vrest
Ei = -70 * mvolt - vrest

start_time = time.time()
eqs = Equations('''
dv/dt = (-v+ge*(Ee-v)+gi*(Ei-v))*(1./taum) : mvolt
dge/dt = -ge*(1./taue) : 1
dgi/dt = -gi*(1./taui) : 1
''')
# NB 1: conductances are in units of the leak conductance
# NB 2: multiplication is faster than division

# Thalamic  neurons
tneuronnum=10
tpoissonrate=1
TC1 = PoissonGroup(tneuronnum,tpoissonrate)
TC2 = PoissonGroup(tneuronnum,tpoissonrate)
TC3 = PoissonGroup(tneuronnum,tpoissonrate)
TC4 = PoissonGroup(tneuronnum,tpoissonrate)
TC5 = PoissonGroup(tneuronnum,tpoissonrate)
TC6 = PoissonGroup(tneuronnum,tpoissonrate)
TC7 = PoissonGroup(tneuronnum,tpoissonrate)
TC8 = PoissonGroup(tneuronnum,tpoissonrate)
TC9 = PoissonGroup(tneuronnum,tpoissonrate)

# Cortical neurons
vthold = 20 * mvolt
vreset = -20 * mvolt
Ge=NeuronGroup(N=100, model=eqs, threshold=vthold,
              reset=vreset, refractory=3 * msecond,
              order=1, compile=True)
Gi=NeuronGroup(N=25, model=eqs, threshold=vthold,
              reset=vreset, refractory=3 * msecond,
              order=1, compile=True)

# Readout neurons
RON=NeuronGroup(N=10, model=eqs, threshold=vthold,
              reset=vreset, refractory=3 * msecond,
              order=1, compile=True)

# Synaptic weights
#wtc0=25; we=2./100.; wi=we; tcrie=2; cxrie=3.5; #Asynchronous state r~0.3 
wtc0=75; we=2./100.; wi=we; tcrie=2; cxrie=1; #Up and down state r~0.8

wtc1= wtc0/1000. # Thalamocortical weight
wtc2= wtc0/ 800. # Thalamocortical weight
wtc3= wtc0/ 400. # Thalamocortical weight
wtc4= wtc0/ 200. # Thalamocortical weight
wtc5= wtc0/ 100. # Thalamocortical weight
wtc6= wtc0/ 200. # Thalamocortical weight
wtc7= wtc0/ 400. # Thalamocortical weight
wtc8= wtc0/ 800. # Thalamocortical weight
wtc9= wtc0/1000. # Thalamocortical weight
we = we # Intracortical excitatory weight 
wi = wi # Intracortical inhibitory weight
tcrie=tcrie; cxrie=cxrie;

# Thalamocortical connections
CteTC1 = Connection(TC1, Ge, 'ge')
WteTC1=lognormal(0,1,(len(TC1),len(Ge)))*wtc1
CteTC1.connect( TC1, Ge, WteTC1 )
CtiTC1 = Connection(TC1, Gi, 'ge')
WtiTC1=lognormal(0,1,(len(TC1),len(Gi)))*wtc1*tcrie
CtiTC1.connect( TC1, Gi, WtiTC1 )

CteTC2 = Connection(TC2, Ge, 'ge')
WteTC2=lognormal(0,1,(len(TC2),len(Ge)))*wtc2
CteTC2.connect( TC2, Ge, WteTC2 )
CtiTC2 = Connection(TC2, Gi, 'ge')
WtiTC2=lognormal(0,1,(len(TC2),len(Gi)))*wtc2*tcrie
CtiTC2.connect( TC2, Gi, WtiTC2 )

CteTC3 = Connection(TC3, Ge, 'ge')
WteTC3=lognormal(0,1,(len(TC3),len(Ge)))*wtc3
CteTC3.connect( TC3, Ge, WteTC3 )
CtiTC3 = Connection(TC3, Gi, 'ge')
WtiTC3=lognormal(0,1,(len(TC3),len(Gi)))*wtc3*tcrie
CtiTC3.connect( TC3, Gi, WtiTC3 )

CteTC4 = Connection(TC4, Ge, 'ge')
WteTC4=lognormal(0,1,(len(TC4),len(Ge)))*wtc4
CteTC4.connect( TC4, Ge, WteTC4 )
CtiTC4 = Connection(TC4, Gi, 'ge')
WtiTC4=lognormal(0,1,(len(TC4),len(Gi)))*wtc4*tcrie
CtiTC4.connect( TC4, Gi, WtiTC4 )

CteTC5 = Connection(TC5, Ge, 'ge')
WteTC5=lognormal(0,1,(len(TC5),len(Ge)))*wtc5
CteTC5.connect( TC5, Ge, WteTC5 )
CtiTC5 = Connection(TC5, Gi, 'ge')
WtiTC5=lognormal(0,1,(len(TC5),len(Gi)))*wtc5*tcrie
CtiTC5.connect( TC5, Gi, WtiTC5 )

CteTC6 = Connection(TC6, Ge, 'ge')
WteTC6=lognormal(0,1,(len(TC6),len(Ge)))*wtc6
CteTC6.connect( TC6, Ge, WteTC6 )
CtiTC6 = Connection(TC6, Gi, 'ge')
WtiTC6=lognormal(0,1,(len(TC6),len(Gi)))*wtc6*tcrie
CtiTC6.connect( TC6, Gi, WtiTC6 )

CteTC7 = Connection(TC7, Ge, 'ge')
WteTC7=lognormal(0,1,(len(TC7),len(Ge)))*wtc7
CteTC7.connect( TC7, Ge, WteTC7 )
CtiTC7 = Connection(TC7, Gi, 'ge')
WtiTC7=lognormal(0,1,(len(TC7),len(Gi)))*wtc7*tcrie
CtiTC7.connect( TC7, Gi, WtiTC7 )

CteTC8 = Connection(TC8, Ge, 'ge')
WteTC8=lognormal(0,1,(len(TC8),len(Ge)))*wtc8
CteTC8.connect( TC8, Ge, WteTC8 )
CtiTC8 = Connection(TC8, Gi, 'ge')
WtiTC8=lognormal(0,1,(len(TC8),len(Gi)))*wtc8*tcrie
CtiTC8.connect( TC8, Gi, WtiTC8 )

CteTC9 = Connection(TC9, Ge, 'ge')
WteTC9=lognormal(0,1,(len(TC9),len(Ge)))*wtc9
CteTC9.connect( TC9, Ge, WteTC9 )
CtiTC9 = Connection(TC9, Gi, 'ge')
WtiTC9=lognormal(0,1,(len(TC9),len(Gi)))*wtc9*tcrie
CtiTC9.connect( TC9, Gi, WtiTC9 )

# Intracortical connections
Cee = Connection(Ge, Ge, 'ge')
Cee.connect( Ge, Ge, lognormal(0,1,(len(Ge),len(Ge)))*we )
Cei = Connection(Ge, Gi, 'ge')
Cei.connect( Ge, Gi, lognormal(0,1,(len(Ge),len(Gi)))*we )
Cie = Connection(Gi, Ge, 'gi')
Cie.connect( Gi, Ge, lognormal(0,1,(len(Gi),len(Ge)))*wi*cxrie )
Cii = Connection(Gi, Gi, 'gi')
Cii.connect( Gi, Gi, lognormal(0,1,(len(Gi),len(Gi)))*wi*cxrie )

# Connect readout neurons
CtronTC1 = Connection(TC1, RON, 'ge')
WtronTC1=lognormal(0,1,(len(TC1),len(RON)))*wtc1*0.1
CtronTC1.connect( TC1, RON, WtronTC1 )

CtronTC2 = Connection(TC2, RON, 'ge')
WtronTC2=lognormal(0,1,(len(TC2),len(RON)))*wtc2*0.1
CtronTC2.connect( TC2, RON, WtronTC2 )

CtronTC3 = Connection(TC3, RON, 'ge')
WtronTC3=lognormal(0,1,(len(TC3),len(RON)))*wtc3*0.1
CtronTC3.connect( TC3, RON, WtronTC3 )

CtronTC4 = Connection(TC4, RON, 'ge')
WtronTC4=lognormal(0,1,(len(TC4),len(RON)))*wtc4*0.1
CtronTC4.connect( TC4, RON, WtronTC4 )

CtronTC5 = Connection(TC5, RON, 'ge')
WtronTC5=lognormal(0,1,(len(TC5),len(RON)))*wtc5*0.1
CtronTC5.connect( TC5, RON, WtronTC5 )

CtronTC6 = Connection(TC6, RON, 'ge')
WtronTC6=lognormal(0,1,(len(TC6),len(RON)))*wtc6*0.1
CtronTC6.connect( TC6, RON, WtronTC6 )

CtronTC7 = Connection(TC7, RON, 'ge')
WtronTC7=lognormal(0,1,(len(TC7),len(RON)))*wtc7*0.1
CtronTC7.connect( TC7, RON, WtronTC7 )

CtronTC8 = Connection(TC8, RON, 'ge')
WtronTC8=lognormal(0,1,(len(TC8),len(RON)))*wtc8*0.1
CtronTC8.connect( TC8, RON, WtronTC8 )

CtronTC9 = Connection(TC9, RON, 'ge')
WtronTC9=lognormal(0,1,(len(TC9),len(RON)))*wtc9*0.1
CtronTC9.connect( TC9, RON, WtronTC9 )

Ceron = Connection(Ge, RON, 'ge')
Ceron.connect( Ge, RON, lognormal(0,1,(len(Ge),len(RON)))*we*0.1 )
Ciron = Connection(Gi, RON, 'gi')
Ciron.connect( Gi, RON, lognormal(0,1,(len(Gi),len(RON)))*wi*cxrie*0.1 )

# Initialize network neurons
Ge.v = 0*mvolt
Ge.ge = 0
Ge.gi = 0
Gi.v = 0*mvolt
Gi.ge = 0
Gi.gi = 0

# Initialize readout neurons
RON.v = 0*mvolt
RON.ge = 0
RON.gi = 0

# Monitor network neurons
#M = SpikeMonitor(TC5)
#M = SpikeMonitor(S5)
M = SpikeMonitor(Ge)
#M = SpikeMonitor(Gi)
Mv = StateMonitor(Ge, 'v', record=[0,10,20,30,40,50,60,70,80,90])
Mge = StateMonitor(Ge, 'ge', record=[0,10,20,30,40,50,60,70,80,90])
Mgi = StateMonitor(Ge, 'gi', record=[0,10,20,30,40,50,60,70,80,90])

# Monitor readout neurons
Mronv = StateMonitor(RON, 'v', record=[0,1,2,3,4,5,6,7,8,9])
Mronge = StateMonitor(RON, 'ge', record=[0,1,2,3,4,5,6,7,8,9])
Mrongi = StateMonitor(RON, 'gi', record=[0,1,2,3,4,5,6,7,8,9])

run(30000 * ms)

# Plot network neurons 
fig1=plt.figure(1)
subplot(211)
raster_plot(M, title='nnetwork_lognormalw', newfigure=False)
subplot(223)
plot(Mv.times / ms, Mv[0] / mV)
xlabel('Time (ms)')
ylabel('V (mV)')
subplot(224)
plot(Mge.times / ms, Mge[0])
plot(Mgi.times / ms, Mgi[0])
xlabel('Time (ms)')
ylabel('ge and gi')
#legend(('ge', 'gi'), 'upper right')

# Plot readout neurons (and network neurons raster)
fig2=plt.figure(2)
subplot(211)
raster_plot(M, title='nnetwork_lognormalw', newfigure=False)
subplot(223)
plot(Mronv.times / ms, Mronv[0] / mV)
xlabel('Time (ms)')
ylabel('V (mV)')
subplot(224)
plot(Mronge.times / ms, Mronge[0])
plot(Mrongi.times / ms, Mrongi[0])
xlabel('Time (ms)')
ylabel('ge and gi')
#legend(('ge', 'gi'), 'upper right')
show()

# Save network neurons & readout neurons
import scipy.io as sio
#sio.savemat('nnetwork_lognormalw_Data_M',{'M':M.spikes})
#sio.savemat('nnetwork_lognormalw_Data_Mtime',{'Mtime':Mv.times})
#sio.savemat('nnetwork_lognormalw_Data_Mv',{'Mv':Mv.values})
#sio.savemat('nnetwork_lognormalw_Data_Mge',{'Mge':Mge.values})
#sio.savemat('nnetwork_lognormalw_Data_Mgi',{'Mgi':Mgi.values})
#sio.savemat('nnetwork_lognormalw_Data_Mronv',{'Mronv':Mronv.values})
#sio.savemat('nnetwork_lognormalw_Data_Mronge',{'Mronge':Mronge.values})
#sio.savemat('nnetwork_lognormalw_Data_Mrongi',{'Mrongi':Mrongi.values})


