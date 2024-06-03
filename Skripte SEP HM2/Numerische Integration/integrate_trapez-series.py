import numpy as np

# INPUT
r = np.array([0., 800., 1200., 1400., 2000., 3000., 3400., 3600., 4000., 5000., 5500., 6370.])
rho = np.array([13000., 12900., 12700., 12000., 11650., 10600., 9900., 5500., 5300., 4750., 4500., 3300.])

x = r*1000
y = rho*4.*np.pi*x**2
#---------------------------------------------------------------------

def trapez(x, y):
    n = np.size(x) - 1
    
    T = 0
    for i in range(0, n):
        T = T + (y[i] + y[i+1]) / 2 * (x[i+1] - x[i])
    return T

# b

m_berechnet = trapez(x, y)
print('Berechnete Masse', m_berechnet, 'kg')

m_literatur = 5.972e24
fehler_abs = np.abs(m_berechnet - m_literatur)
fehler_rel = fehler_abs / m_literatur
print('Absoluter Fehler', fehler_abs, 'kg')
print('Relativer Fehler', fehler_rel)
