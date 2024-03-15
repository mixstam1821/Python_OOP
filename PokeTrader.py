def main():
    poke_party = ["PIKACHU", "CHARMELEON", "GEODUDE", "GYARADOS", "BUTTERFREE", "MANKEY"]

    while True:
        print("EXCHANGE POKEMON\n")
        print("0. " + poke_party[0])
        for i in range(1, len(poke_party)):
            print("\t" + str(i) + ". " + poke_party[i])

        print("\nChoose a Pokemon to exchange with " + poke_party[0] + ". (Or enter 0 to quit.)")
        x = int(input("> "))

        if x == 0:
            break

        # Swap the Pokemon in slot 0 with the Pokemon in slot x
        swap_poke = poke_party[0]
        poke_party[0] = poke_party[x]
        poke_party[x] = swap_poke

if __name__ == "__main__":
    main()
