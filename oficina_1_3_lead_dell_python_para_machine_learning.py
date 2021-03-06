# -*- coding: utf-8 -*-
"""Oficina 1.3 Lead Dell - Python para Machine Learning

Durante a aula, você aprendeu a utilizar o módulo datetime e seus tipos para trabalhar com informação de data e hora. Agora é a vez de praticar os seus conhecimentos. Para esta atividade, considere a situação e os dados a seguir.

Seus amigos sabem que você está trabalhando com Python e estão entusiasmados com as possibilidades de aplicações. Um deles é muito esquecido e sugeriu que você fizesse um programa que o alerte quando for o aniversário de alguém do seu grupo de amigos.

Você pediu aos seus amigos que anotassem as datas de seus aniversários em uma lista, conforme está descrito a seguir, mas cada pessoa escreveu de uma forma diferente, então, cabe a você interpretá-la adequadamente:

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990'].

Para isso, o recomendado é criar uma lista de formatos correspondentes e aplicá-la à lista de datas de aniversários. O seu objetivo é criar um programa que converta a lista de datas de tipo string em uma lista de objetos do tipo data e organizá-los por ordem de aniversário no ano. Isso significa que primeiro vem o mês e, em seguida, o dia como critério de ordenação.

Depois, você deve verificar se o dia de hoje é aniversário de alguém. Caso seja, você deve escrever a string “Hoje, (DIA DA SEMANA) (DIA) de (MÊS) de (ANO ATUAL), tem aniversário!”, em que as palavras DIA DA SEMANA, DIA, MÊS e ANO ATUAL devem ser substituídas pelos seus respectivos valores. As informações devem estar escritas em português.
"""

from datetime import datetime, date, time

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

data1 = datetime.strptime('1/2/1990', '%m/%d/%Y').date()
data2 = datetime.strptime('22 de Maio de 1991', '%d de %B de %Y').date()
data3 = datetime.strptime('04/Abr/1995', '%d/%b/%Y').date()
data4 = datetime.strptime('1995-Outubro-10', '%Y-%B-%d').date()
data5 = datetime.strptime('12 Julho 1989', '%d %B %Y').date()
data6 = datetime.strptime('16 de Junho de 1987', '%d de %B de %Y').date()
data7 = datetime.strptime('04/07/1990', '%m/%d/%Y').date()

aniversarios = [(data1.strftime('%b/%d/%Y')), 
                 (data2.strftime('%b/%d/%Y')),
                 (data3.strftime('%b/%d/%Y')),
                 (data4.strftime('%b/%d/%Y')),
                 (data5.strftime('%b/%d/%Y')),
                 (data6.strftime('%b/%d/%Y')),
                 (data7.strftime('%b/%d/%Y'))
                ]

# print(sorted(aniversarios))

hoje = date.today()

hojeFormat = hoje.strftime('%b/%d/%Y')

# print(hoje)
# print(hojeFormat)


if hojeFormat in aniversarios:
    print(datateste.strftime("Hoje, %A, %d de %B de %Y, tem aniversário!"))
    
else:
    print("Hoje não tem bolo :(")
