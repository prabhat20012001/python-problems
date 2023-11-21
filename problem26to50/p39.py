arr = []

for i in range(5):
    arr.append(int(input(f"Enter year {i + 1}: ")))

for year in arr:
    if year % 4 == 0:
        print(year)
