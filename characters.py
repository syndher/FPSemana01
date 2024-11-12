monstroa = input()
vidaa = input()
xpa = int(input())
monstrob = input()
vidab = input()
xpb = int(input())
monstroc = input()
vidac = input()
xpc = int(input())

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
else:
    pass