#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

joke_words = [
    'piada',
    'conta uma piada ai!',
    'conta uma piada ai',
    'conta uma piada aí!',
    'conta uma piada aí',
    'conta uma piada',
    'conta uma piada?',
    'pia',
    'conta outra piada!',
    'conta outra piada',
    'mais uma piada!',
    'mais uma piada',
    'conta mais uma piada!',
    'conta mais uma piada',
    'conta uma piada melhor!',
    'conta uma piada melhor',
    'outra piada'
]


morning_words = [
    'morning!',
    'morning',
    'good morning!',
    'good morning',
    'bom dia',
    'bom dia!',
]

night_words = [
    'night!',
    'night',
    'good night!',
    'good night',
    'boa noite!',
    'boa noite',
]

fuck_words = [
    'fuck!',
    'fuck',
    'fuck you!',
    'fuck you',
    'fuck yourself!',
    'fuck yourself',
    'fuck u!',
    'fuck u',
    'vai se fuder',
    'vai se fuder!',
    'foda-se',
    'foda-se!',
    'vsf',
]

love_words = [
    'eu te amo!',
    'eu te amo',
    'te amo!',
    'te amo',
    'i love you',
    'i love you!',
    'i lov you',
    'i lov you!',
    'lov u',
    'lov u!',
    'i lov u',
    'i lov u!'
]

months = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
}

welcome_count = 0

bot_names = [
    ', dog',
    'dog, ',
    ' dog,',
    'dog,',
    ' dogão',
    'dogão ',
    'doguinha',
    ' doguinha',
    'doguinha ',
    ' dog',
    'dog ',
    ' rei',
    'rei ',
    ' mestre',
    'mestre ',
    '@doguinha_bot ',
    ' @doguinha_bot',
]