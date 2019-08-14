times = ('Flamento', 'Atlético', 'Sao paulo', 'Internacional', 'Gremio',
         'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo', 'Corinthians',
         'Vasco da Gama', 'Fluminense', 'America-MG', 'Chapecoense', 'Santos',
         'EC Vitorias', 'Bahia', 'Parana', 'Ateltico-PR', 'Ceara SC')
print(f'''{"-" * 30}
A classificacao atual é: {times}')
{"-" * 30}
Os 5 primeiros times sao:{times[:5]}
{"-" * 30}
Os 4 ultimos times sao: {times[-4:]}
{"-" * 30}
Os times sao: {sorted(times)}
{"-" * 30}
Chapecoense esta em {times.index("Chapecoense") + 1}º
{"-" * 30}''')
