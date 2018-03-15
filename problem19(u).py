temp = (365*100 + 25)

mydict = {'Montag':0, 'Dienstag':0, 'Mittwoch':0, 'Donnerstag':0, 'Freitag':0,
          'Samstag':0, 'Sonntag':0}

mydict




day_state = 7
for i in range(temp):
    if day_state==7:
        mydict['Montag'] += 1
        day_state=1
    elif day_state ==1:
        mydict['Dienstag'] += 1
        day_state += 1
    elif day_state ==2:
        mydict['Mittwoch'] += 1
        day_state += 1
    elif day_state ==3:
        mydict['Donnerstag'] += 1
        day_state += 1
    elif day_state ==4:
        mydict['Freitag'] += 1
        day_state += 1
    elif day_state ==5:
        mydict['Samstag'] += 1
        day_state += 1
    elif day_state ==6:
        mydict['Sonntag'] += 1
        day_state += 1

print(mydict['Sonntag'])