h = int(input())
w = int(input())

ind = w/((h/100)**2)

if ind < 16:
    print("выраженный дефицит массы тела")
elif 16 <= ind < 18.5:
    print("недостаточная масса тела")
elif 18.5 <= ind < 25:
    print("норма")
elif 25 <= ind < 30:
    print("избыточная масса тела")
elif 30 <= ind < 35:
    print("ожирение первой степени")
elif 35 <= ind < 40:
    print("ожирение второй степени")
elif ind >= 40:
    print("ожирение третьей степени")