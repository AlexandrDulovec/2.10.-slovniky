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

for zam_id, zam_info in zamestnanci.items():
    print(f'Jméno: {zam_info["jmeno"]}')
    print(f'Příjmení: {zam_info["prijmeni"]}')
    print(f'Email: {zam_info["email"]}')
    print('-' * 30)