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

for zamestnanec_id, zamestnanec_info in zamestnanci.items():
    print(f'ID zaměstnance: {zamestnanec_id}')
    print(f'Jméno: {zamestnanec_info["jmeno"]}')
    print(f'Příjmení: {zamestnanec_info["prijmeni"]}')
    print(f'Pozice: {zamestnanec_info["pozice"]}')
    print(f'Email: {zamestnanec_info["email"]}')
    print(f'Označení kanceláře: {zamestnanec_info["kancelar"]}')
    print('-' * 30)
