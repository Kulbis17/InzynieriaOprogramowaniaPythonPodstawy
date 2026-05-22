def verify_pesel(pesel: str) -> int:
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0

    for i in range(10):
        suma = suma + (int(pesel[i]) * wagi[i])

    cyfra_kontrolna = 10 - (suma % 10)

    if cyfra_kontrolna == 10:
        cyfra_kontrolna = 0

    if cyfra_kontrolna == int(pesel[10]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    pesel_input = "97082123152"
    print(verify_pesel(pesel_input))