def num_input():
    rand_num = input("Enter a random 4 digit number (digits cannot all be the same): ")

    # Prüfen: nur Ziffern, genau 4 Stellen, nicht alle gleich
    if rand_num.isdigit() and len(rand_num) == 4 and len(set(rand_num)) > 1:
        kaprekar(rand_num)
    else:
        print("Number must contain 4 digits and not all be the same. Please try again")

def kaprekar(rand_num):
    step = 0
    current = rand_num

    while current != "6174":
        current = f"{int(current):04d}"

        sort_desc = "".join(sorted(current, reverse=True))   #join um die Liste wieder in einen str zu bringen. 
        sort_asce = "".join(sorted(current))

        high = int(sort_desc)
        low = int(sort_asce)
        total = high - low

        step += 1
        print(f"Step {step}: {sort_desc} - {sort_asce} = {total:04d}")

        current = f"{total:04d}"

        # Sicherheitsabbruch, falls etwas schiefgeht
        if current == "0000":
            print("Reached 0000, no 6174 for this number.")
            break

    if current == "6174":
        print("Reached 6174!")

num_input()
