principal = 1000

rate = 7 / 100



for year in range(1, 31):
    amount = principal * (1 + rate) ** year

    print(f'{year:>2}{amount:>30.2f}')
