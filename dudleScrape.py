import pandas as pd
from requests_html import HTMLSession

names = []
Ticks = []
Positions = []
#create the session
session = HTMLSession()

#define our URL
url = 'https://dud-poll.inf.tu-dresden.de/jmd'

#use the session to get the data
r = session.get(url)

#get number of participants to feed into loop
nParticipant = len(r.html.find('.participantrow'))


for j in range(nParticipant):
    #Get names and meeting durations:
    participantRow = r.html.find('.participantrow')
    trInfo = participantRow[j].find('td')
    names.append(trInfo[1].text) #list of names with durations

    #get tick marks:
    ticks = []
    P = participantRow[j].find('td') 
    for i in range(2,17):
        a = (P[i].find('.vote'))
        ticks.append(a[0].text) #list of tick marks
    Ticks.append(ticks)
    

for i in range(len(Ticks)):
    Positions.append(Ticks[i].index('✔')) #get position of tick marks

#compile all to dataframe:
Results = pd.DataFrame({'positions': Positions, 'names':names}).sort_values(by=['positions'])
print(Results)
