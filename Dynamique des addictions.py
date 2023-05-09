"""
Nom du fichier : Dynamique des addictions.py
Auteur(s) : Astruc Lélio, Del Rosso Luca, Edery Nathan
Date de création : 24/04/2023
Dernière mise à jour : 09/05/2023
Version : 1.1

Description : Voici une implémentation en python du modèle d'éviolution des addictions proposé par Abderrahmane Habbal
"""
    
    ## Imports nécéssaires pour les opérations d'algèbre linéaire et d'affichage graphique
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
d = 0.2
q = 0.8
p = 0.2
S_max = 0.5
h = p*S_max
k = (p/q)*S_max
b = 2*d/q
R_max = 7
m_E = 0.04
m_Epsi = m_E
m_lambda = 0.001


# Initialisation
T = 200
desireIntensity = np.zeros(T)
selfControl = np.zeros(T)
societyInfluence = np.ones(T)
vulnerability = np.zeros(T)
addiction = np.zeros(T)
psi = np.zeros(T)
lamda = np.zeros(T)
desireIntensity[0] = 1
selfControl[0] = S_max
societyInfluence[0] = 0.3
lamda[0] = 0.5

# Fonction d'influence sociétale périodique
def social_influence(t, amp, freq):
    return 0.5 + amp * np.sin(2 * np.pi * freq * t)


# Simulation normale, cas avec exposition sociale linéaire-periodique
for t in range(T-1):
    psi[t] = desireIntensity[t] - selfControl[t] #- societyInfluence[t]
    vulnerability[t] = min(1, max(0, psi[t]))
    addiction[t] = q*vulnerability[t] + (np.random.poisson(lamda[t], 1)/R_max) * q*(1-vulnerability[t])
    desireIntensity[t+1] = (1-d)*desireIntensity[t] + b*min(1, 1-desireIntensity[t])*addiction[t]
    selfControl[t+1] = selfControl[t] + p*max(0, S_max-selfControl[t]) - h*desireIntensity[t] - k*addiction[t]
    societyInfluence[t+1] = societyInfluence[t] - m_E 
    lamda[t+1] = lamda[t] + m_lambda 


# Simulation avec exposition sociale psychiatrique
for t in range(T-1):
    psi[t] = desireIntensity[t] - selfControl[t] - societyInfluence[t]
    print(psi[t])
    vulnerability[t] = min(1, max(0, psi[t]))
    addiction[t] = q*vulnerability[t] + (np.random.poisson(lamda[t], 1)/R_max)*q*(1-vulnerability[t])
    desireIntensity[t+1] = (1-d)*desireIntensity[t] + b*min(1, 1-desireIntensity[t])*addiction[t]
    selfControl[t+1] = selfControl[t] + p*max(0, S_max-selfControl[t]) - h*desireIntensity[t] - k*addiction[t]
    if (t%5 == 0):
        societyInfluence[t+1] =  societyInfluence[t] + 0.08
        m_E = m_E - 0.001
    else:
        societyInfluence[t+1] = societyInfluence[t] - m_E
    lamda[t+1] = lamda[t] + m_lambda

"""
# Simulation avec exposition sociale psychiatrique puis arrêt du suivi psy si le patient est guéri
for t in range(T-1):
    psi[t] = desireIntensity[t] - selfControl[t] - societyInfluence[t]
    print(psi[t])
    vulnerability[t] = min(1, max(0, psi[t]))
    addiction[t] = q*vulnerability[t] + (np.random.poisson(lamda[t], 1)/R_max)*q*(1-vulnerability[t])
    desireIntensity[t+1] = (1-d)*desireIntensity[t] + b*min(1, 1-desireIntensity[t])*addiction[t]
    selfControl[t+1] = selfControl[t] + p*max(0, S_max-selfControl[t]) - h*desireIntensity[t] - k*addiction[t]
    if(desireIntensity[t]>0.5):
        if (t%5 == 0):
            societyInfluence[t+1] =  societyInfluence[t] + 0.08
            m_Epsi = m_Epsi - 0.001
        else:
            societyInfluence[t+1] = societyInfluence[t] - m_Epsi
    else:
        societyInfluence[t+1] = societyInfluence[t] - m_E
    lamda[t+1] = lamda[t] + m_lambda"""

# On tronque les vecteurs pour éviter les valeurs nulles de desireIntensity, selfControl et societyInfluence
desireIntensity = desireIntensity[:-1]
selfControl = selfControl[:-1]
societyInfluence = societyInfluence[:-1]
vulnerability = vulnerability[:-1]
addiction = addiction[:-1]
psi = psi[:-1]
lamda = lamda[:-1]

t = np.arange(T-1)

# Self control et vulnérabilité
""" plt.xlabel('Temps (en semaines)')
plt.plot(t, selfControl, label='Self-control')
plt.plot(t, vulnerability, label='Vulnérabilité')
plt.legend()
plt.title("Self-control et vulnérabilité avec des expositions sociales psychiatriques")
plt.show()

#Désir et passage à l'acte
plt.xlabel('Temps (en semaines)')
plt.plot(t, desireIntensity, label='Intensité du désir')
plt.plot(t, addiction, label='Passage à l\'acte')
plt.legend()
plt.title("Désir et passage à l'acte avec des expositions sociales psychiatriques")
plt.show()

#Désir et passage à l'acte
plt.xlabel('Temps (en semaines)')
plt.plot(t, societyInfluence, label='Influence sociétale')
plt.plot(t, desireIntensity, label='Intensité du désir')
plt.plot(t, selfControl, label='Self-control')
plt.legend()
plt.title("Self-control désir et influence sociétale avec des expositions sociales psychiatriques")
plt.show()

#Désir et passage à l'acte
plt.xlabel('Temps (en semaines)')
plt.plot(t, psi, label='État psychologique')
plt.plot(t, desireIntensity, label='Intensité du désir')
plt.legend()
plt.title("État psychologique et désir avec des expositions sociales psychiatriques")
plt.show()  """

plt.xlabel('Temps (en semaines)')
plt.plot(t, societyInfluence, label='Influence sociétale')
plt.plot(t, desireIntensity, label='Intensité du désir')
plt.plot(t, selfControl, label='Self-control')
plt.plot(t, psi, label='État psychologique')
plt.plot(t, vulnerability, label='Vulnérabilité')
plt.plot(t, addiction, label='Passage à l\'acte')
plt.title('Simulation avec exposition sociale psychiatrique')
plt.legend()
plt.show()





