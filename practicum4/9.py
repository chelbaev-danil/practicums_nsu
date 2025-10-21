print('Собака короткошерстной породы?')
x=input()
if x=='да':
    print('Рост собаки менее 50 см?')
    y=input()
    if y=='да':
        print('У собаки короткий хвост?')
        u=input()
        if u=='да':
            print('Английский бульдог')
        else:
            print('У собаки длинные уши?')
            a = input()
            if a=='да':
                print('гончая')
            else:
                print('у собаки короткое тело?')
                s= input()
                if s=='да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        print('Собака весит более 50 кг?')
        i =input()
        if i=='да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    print('Рост собаки менее 50 см?')
    z=input()
    if z=='да':
        print('У собаки доброжелательный характер?')
        o=input()
        if o =='да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')

    else:
        print('У собаки рост меньше 70 см?')
        p=input()
        if p=='да':
            print('у собаки длинные уши?')
            d = input()
            if d=='да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            print('Окрас ражий с белыми отметинами?')
            f = input()
            if f=='да':
                print('сенбернар')
            else:
                print('Белоснежный окрас?')
                g = input()
                if g=='да':
                    print('ирладский волкодав')
                else:
                    print('ньюфаундлен')