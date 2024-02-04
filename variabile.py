# variabila = zona din memorie care tine date
# = este un operator de atribuire

# am declarat si initializat variabila marca
marca = 'Volvo'
model_masina = 'XC 60'

# variabila incepe cu litera mica si nu putem pune spatiu in nume

print(f'Am cumparat o masina marca {marca}')
print (f'Este modelul : {model_masina}')

print('Am cumparat o masina marca ' + marca)
print('Am cumparat o masina marca' + ' ' + marca)

# suprascriere sau overwrite
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina marca {marca}')
print (f'Este modelul : {model_masina}')

# concatenare stringuri
nume = 'Creta'
prenume = 'Sarra'
varsta = 26
print(prenume + ' ' + nume)
print(f'{prenume} {nume} are  varsta de {varsta}')

print(nume + ' ' + prenume + ' ' + str(varsta))

