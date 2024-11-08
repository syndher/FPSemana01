monstroa = input("Qual o nome da primeira criatura?")
vidaa = input("Quanta vida tem o " + monstroa)
xpa = input("Qual o nivel do " + monstroa)
monstrob = input("Qual o nome da segunda criatura?")
vidab = input("Quanta vida tem o " + monstrob)
xpb = input("Qual o nivel do " + monstrob)
monstroc = input("Qual o nome da terceira criatura?")
vidac = input("Quanda vida tem o " + monstroc)
xpc = input("Qual o nivel do " + monstroc)

array1 = [[monstroa, (vidaa , xpa)],
        [ monstrob, (vidab , xpb)],
        [ monstroc, (vidac , xpc)]
]

array2 = [[(xpa), (xpb), (xpc)]]
print(array1)

if xpa > xpb and xpa > xpc and xpb > xpc:
    print(monstroa)
    print(monstrob)
    print(monstroc)
elif xpa > xpb and xpa > xpc and xpb < xpc:
    print(monstroa)
    print(monstroc)
    print(monstrob)
elif xpa < xpb and xpa > xpc and xpb > xpc:
    print(monstrob)
    print(monstroa)
    print(monstroc)
elif xpa < xpb and xpa < xpc and xpb > xpc:
    print(monstrob)
    print(monstroc)
    print(monstroa)
elif xpa < xpb and xpa < xpc and xpb < xpc:
    print(monstroc)
    print(monstrob)
    print(monstroa)
elif xpa > xpb and xpa < xpc and xpb < xpc:
    print(monstroc)
    print(monstroa)
    print(monstrob)

