import random

toad = ('████████████████████████████████████████\n'
'██████████████████████████▀▀▀███████████\n'
'█████████████████████████░░████░░▀▀█████\n'
'█████████████████████▀▀░▀▄░▀▀█▀░░░░░▀███\n'
'██████████▀▀▀▀▀▀▀▀▀░░░░░░░▀▀▀░░░░░░▄▄███\n'
'██████▀▀░░░░░░░░░░░░░░░░░░░░░░░░▄▄██████\n'
'████▀░░░░░░░░░░░░░░░░░░░░░░░░░██████████\n'
'███▀░░░░░▄▄▄░░░░░░░░░░░░░░░░░░██████████\n'
'███░░░░░░░░░▀▀▄░░░░░░░░░░░░░░░██████████\n'
'███░░░░░░░░░░░░▀▄░░░░░█░░░▄░▄███████████\n'
'███▄░░░░░░░░░░░░█░░░░░█░░░██▀███████████\n'
'████▄░░░░░░░░░░█▀░░░░░█░░░█░░███████████\n'
'████▀░░░░░░▄▄▀▀░░░░░▄▄██░░▀▄░▀██████████\n'
'███░░░░░░▀▀▀▀▀▀▀▀████████▄░▀▄░▀█████████\n'
'████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄███████\n'
'████████████████████████████████████████\n')

guardian = ('░░░░░░░░██░░░░░░░░\n'
'░░░░░░░█▀▀█░░░░░░░\n'
'░░░░░░▄▀░░▀▄░░░░░░\n'
'░░░░░▄█░░░░█▄░░░░░\n'
'░░░░░█░░░░░░█░░░░░\n'
'░░░░▄█░░░░░░█▄░░░░\n'
'░░░░█░▄▄▄▄▄▄░█░░░░\n'
'░░░▄████░░████▄░░░\n'
'░░▄▀█░░████░░█▀▄░░\n'
'░░█░▀▀▀████▀▀▀░█░░\n'
'░░█▄░░░░▀▀░░░░▄█░░\n'
'▄█▀█▄░░░░░░░░▄█▀█▄\n'
'█░█░▀█▄░░░░▄█▀░█░█\n'
'███░░░░▀██▀░░░░███\n'
'▀█▀▀█▄▄▄▄▄▄▄▄█▀▀█▀\n'
'▄█▀▄▄▄▄█░░█▄▄▄▄▀█▄\n'
'▀█▄▄▄▀▀▀▀▀▀▀▀▄▄▄█▀\n'
'░░▀█▀▀▀▀██▀▀▀▀█▀░░\n'
'░░▄█▄▄▄█▀▀█▄▄▄█▄░░\n')

actions_start = ('взять', 'отказать')                           #списки действий игрока
actions_play = ('держать', 'уронить', 'выбросить', 'отдать')
inventory = []

creeps = ('Упырь', 'Лесавки', 'Леший', 'Бесы', 'Бабай', 'Лихо', 'Шишига', 'Мавка' ) #убить лесавок - вы разозлили лешего
actions_with_creeps = {
    creeps[0]: ['убить', 'проигнорировать', 'пообщаться'],
    creeps[1]: ['убить', 'напугать', 'проигнорировать', 'поиграть'],
    creeps[2]: ['убить', 'проигнорировать', 'пообщаться'], #одобрение лешего или злость
    creeps[3]: ['убить', 'напугать', 'проигнорировать', 'поиграть'],
    creeps[4]: ['убить', 'напугать','проигнорировать'],
    creeps[5]: ['изгнать', 'напугать', 'проигнорировать'],
    creeps[6]: ['убить', 'прогнать', 'бегать вокруг дерева', 'проигнорировать'],#из шишиги выпадает камыш
    creeps[7]: ['убить', 'проигнорировать', 'пообщаться','пойти с ней'],
}              

guardians_phrases = {                                           #список фраз хранителя при действиях игрока
    'взять': ['Береги её. Прийду, проверю.', 'Скоро вернусь', 'Не смей уронить !', 'Не отдавай её никому !', 'Смотри у меня !'],
    'отказать': ['У тебя никто не спрашивал.', 'Забирай уже !', 'Что ты мнешься ?..', 
                 'Твои желания не имеют значения.', 'Твое мнение не важно.'],
    'держать': [' ', 'Держишь ?\n Держи.', 'А ты молодец !', 'Хорошо справляешься !'],
    'уронить': ['Во раздолбай !', 'Разве такому тебя матушка учила ?', 'Ничего тебе доверить нельзя...', 'Моя жаба ! (；□；)'],
    'выбросить': ['Во раздолбай !', 'Разве такому тебя матушка учила ?', 'Ничего тебе доверить нельзя...', 'Моя жаба ! (；□；)'],
    'отдать': ['Хорошая работа, путник )', 'спасибо за помощь', 'Зачем ты мне её отдаёшь ? Ну, ладно...', 
               'А, ну, лано...', 'Спасибо !', 'Благодарю !', 'Прими мою благодарность.'],
}

print('нажмите "enter", чтобы начать и далее чтобы продолжить.') #начало игры
input()
print('твоё местоположение: густой лес близ болота')
input()
print(guardian)                                                
print("Привет ! Я хранитель жаб.\n Для тебя есть работа не из легких...\nТы должен подержать жабу, пока я не вернусь.")
input()
print("Держи жабу !\n")
input()
print(toad)
input()
inventory.append('меч')
print('хранитель дал тебе', inventory[0])

for i in range(4):
    print('уровень', i+1)
    print('\nваши действия с жабой:')
    for i in range(len(actions_start)):
        print( i+1, ':', actions_start[i])
        i += 1

    your_actions = input('выберите действие: ')  #print(actions[your_actions])
    if your_actions == 'взять':
        print('\n', random.choice(guardians_phrases['взять']))
    elif your_actions == 'отказать':
        print('\n', random.choice(guardians_phrases['отказать']))
    input()
    print(toad)
    input()

    rand_num = random.randint(1, 10)
    for i in range(rand_num):
        creep_came = random.choice(creeps)

        if creep_came == creeps[0]:
            print('рядом с вами', creeps[0])
            for i in range(len(actions_with_creeps(creeps[0]))):
                print(i, ':', actions_with_creeps(creeps[0]))
                your_actions = input('выберите действие, чтоб защитить жабу:')
            if your_actions == 'убить':
                print('ты защитил себя и жабу. молодец !')
            elif your_actions == 'проигнорировать':
                print('Упырь высосал из тебя всю кровь и раздавил жабу, остолбень !')
                break
            elif your_actions == 'пообщаться':
                print('Упырь не стал тебя слушать, высосал всю твою кровь и раздавил жабу, тугодум ты проклятый!')
                print(random.choice(guardians_phrases('уронить')))
                break

        if creep_came == creeps[1]:
            print('рядом с вами', creeps[1])
            for i in range(len(actions_with_creeps(creeps[1]))):
                print(i, ':', actions_with_creeps(creeps[1]))
            your_actions = input('выберите действие, чтоб защитить жабу:')
            if your_actions == 'убить':
                inventory.append('ненависть Лешего')
                print('ты разозлил Лешего...')
                print('в инвентарь добавлено', inventory[inventory.index('ненависть Лешего')])
            elif your_actions == 'напугать':
                inventory.append('ненависть Лешего')
                print('ты разозлил Лешего...')
                print('в инвентарь добавлено', inventory[inventory.index('ненависть Лешего')])
            elif your_actions == 'проигнорировать':
                print('Лесавки - безобидные дети. они тебе ничего не сделают.')
            elif your_actions == 'поиграть':
                print('ты чудно побаловался с Лесавками, но чуть не уронил жабу.\nбудь осторожнее.')
                inventory.append('уважение Лешего')
                print('в инвентавь добавлено', inventory[inventory.index('уважение Лешего')])

        if creep_came == creeps[2]:
            print('рядом с вами', creeps[2])
            if inventory.count('ненависть Лешего') > 0:
                print('Леший отомстил за своих детей Лесавок и накормил вас ядовитыми грибами...')
                print('к счастью, с жабой ничего не произошло.')
                inventory.remove('ненависть Лешего')
                break
            elif inventory.count('уважение Лешего') > 0:
                print('Леший дал вам травы, что отгоняют лесную нечисть.\nты ему нравишься.')
                inventory.append('лесные травы')
                inventory.remove('уважение Лешего')
            else:
                for i in range(len(actions_with_creeps(creeps[2]))):
                    print(i, ':', actions_with_creeps(creeps[2]))
                your_actions = input('выберите действие, чтоб защитить жабу:')
                #  'пообщаться'
                if your_actions == 'убить':
                    print('Леший безобидный ! ты за что его убил, окаянный ?!')
                    print('ну, хотя бы жаба цела...')
                elif your_actions == 'проигнорировать':
                    print('Леший безобидный. он просто прошел мимо по своим делам.\nникто не пострадал.')
                else:
                    print('Леший безобидный. вы мило побеседовали, и он ушел дальше следить за лесом.')
        
        if creep_came == creeps[3]:
            print('рядом с вами', creeps[3])
            for i in range(len(actions_with_creeps(creeps[3]))):
                print(i, ':', actions_with_creeps(creeps[3]))
            your_actions = input('выберите действие, чтоб защитить жабу:')
            #  'напугать' 'проигнорировать' 'поиграть'
            if your_actions == 'убить':
                print('это было тяжело, но вы зашитились')
            elif your_actions == 'напугать':
                print()

        # for i in range(len(actions_play)):
        #     print(i, ':', actions_play[i])
        # your_actions = input('выберете действие: ')
        # if your_actions == 'держать':
        #     print(random.choice(guardians_phrases['держать']))
        # elif your_actions == 'урониить':
        #     print(random.choice(guardians_phrases['уронить']))
        #     print('жаба умерла...')
        #     break
        # elif your_actions == 'отдать':
        #     print(random.choice(guardians_phrases['отдать']))
        #     print('вы сохранили жабу')
        #     break 
    input()