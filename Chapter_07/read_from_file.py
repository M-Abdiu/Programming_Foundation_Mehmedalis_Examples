with open("cities.txt", "r") as file:
    cities = [line.strip() for line in file]  # List comprehension

with open("cities.txt", "a") as file:
    if "Portland" not in cities:
        file.write("\nPortland\n")

with open("cities.txt", "r") as file:
    cities = file.readlines()
    print(cities)
