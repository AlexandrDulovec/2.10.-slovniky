zamestnanci = {
    1: {
        'jmeno': 'Alexandr',
        'prijmeni': 'Dulovec',
        'pozice': 'borec',
        'email': 'alexandr.dulovec@student.ossp.cz',
        'kancelar': 'A101'
    },
    2: {
        'jmeno': 'Filip',
        'prijmeni': 'Zatáčka',
        'pozice': 'Řidič',
        'email': 'filip.zatacka@gmail.com',
        'kancelar': 'A101'
    },
    3: {
        'jmeno': 'Milan',
        'prijmeni': 'Švanda',
        'pozice': 'Bezdomovec',
        'email': 'milan.svanda@gmail.com',
        'kancelar': 'B202'
    }
 }

zamestnanec_id = 1  
vybrany_zamestnanec = zamestnanci.get(zamestnanec_id)

if vybrany_zamestnanec:
    print(f'Jméno: {vybrany_zamestnanec["jmeno"]}')
    print(f'Příjmení: {vybrany_zamestnanec["prijmeni"]}')
    print(f'Pozice: {vybrany_zamestnanec["pozice"]}')
else:
    print(f'Zaměstnanec s ID {zamestnanec_id} nebyl nalezen.')
