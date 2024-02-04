# declaram si initializam un dict

note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

#adaugam elemente
note_elevi['Sebi'] = 7

print(note_elevi)

# afalam elemente
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizare valori
note_elevi['Costel'] = 10

print(note_elevi)

# dimensiunea
print(len(note_elevi))

# stergere valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi)

# printam doar cheile
print(note_elevi.keys())

