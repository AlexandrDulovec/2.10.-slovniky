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

hledana_kancelar = 'A101'

zamestnanci_ve_stejne_kancelari = [zam for zam in zamestnanci.values() if zam['kancelar'] == hledana_kancelar]

for zam in zamestnanci_ve_stejne_kancelari:
    print(f"Jméno: {zam['jmeno']} {zam['prijmeni']}, Pozice: {zam['pozice']}, Email: {zam['email']}")
