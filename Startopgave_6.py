# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.



def main():




    try:

        bestand = "testalpaca.fasta"
        headers, seqs = lees_inhoud(bestand)
        zoekwoord = input("Geef een zoekwoord op: ")

        while zoekwoord != "":

            zoek_header, zoek_seq = zoek(zoekwoord, headers, seqs)
            if is_dna(zoek_seq):

                enzym_bestand ="enzymen.txt"
                lijst = lees_enzym(enzym_bestand)
                knipt(lijst, zoek_header, zoek_seq)

            else:
                print("Sequence not mRNA.")
            zoekwoord = input("Geef een zoekwoord op: ")

    except UnboundLocalError:
        print("ERROR: Keyword not found. Try again.")
    except FileNotFoundError:
        print("ERROR: File", end=" ")
        print('\"', enzym_bestand, '\"', sep="", end=" ")
        print("not found.")
    except TypeError:
        #print("ERROR: File", end=" ")
        #print('\"', bestand, '\"', sep="", end=" ")
        #print("does not exist.")
        print("Unknown Error")
    except KeyboardInterrupt:
        print('\n', "Program aborted by user.", sep="")



def lees_inhoud(bestands_naam):

    try:
        bestand = open(bestands_naam, "r")
        dna = ""
        headers = []
        seqs = []
        bestand = bestand.readlines()



        for line in bestand:

            if ">" in line:
                clean_line = line.rstrip()
                headers.append(clean_line)
                if len(dna) != 0:
                    dna += " "
            else:
                clean_lines = line.rstrip()
                dna += clean_lines
            seqs = dna.split(" ")

        # print(headers)
        # print(seqs)


        return headers, seqs

    except IOError:
        print("ERROR: File", end=" ")
        print('\"', bestands_naam, '\"', sep="", end=" ")
        print("could not be opened or cannot be found.")
    except:
        print("ERROR: Unknown in \"lees_inhoud\"")



def is_dna(seq):
    try:
        count_A = 0
        count_T = 0
        count_G = 0
        count_C = 0

        for i in seq:
            if i == "A":
                count_A += 1
            elif i == "T":
                count_T += 1
            elif i == "G":
                count_G += 1
            elif i == "C":
                count_C += 1

        total_count = (count_A + count_T + count_G + count_C)

        if total_count == len(seq):
            dna = True
            # print(dna)
        else:
            dna = False
            # print(dna)
        return dna

    except:
        print("ERROR: Unknown in \"is_dna\"")


def lees_enzym(bestands_naam):
    #try:

    bestand = open(bestands_naam, "r")

    lijst = []
    regel = bestand.readline()
    while regel != "":
        raw_data = regel.replace("\n", "").replace("^", "")
        raw_data = raw_data.split(" ")
        regel = bestand.readline()
        lijst.append(raw_data)
    bestand.close()
    # print(lijst)
    return lijst
    '''
    except IOError:
        print("ERROR: Could not open enzyme file. (lees_enzym)")
    except:
        print("ERROR: Unknown in \"lees_enzym\'")
    '''
def knipt(enzyme_list, zoek_head, zoek_seq):

    try:

        enzyme = []
        enzyme_name = []
        for elem in enzyme_list:
            # print(elem)
            enzyme_name.append(elem[0])
            enzyme.append(elem[1])
        print("-" * 50)
        print(zoek_head)
        print(zoek_seq)
        print("-" * 50)
        enzym_counter = 0
        for item in enzyme:  # item @ index 0

            if item in zoek_seq:
                print(enzyme_name[enzym_counter], "is in sequence.")

            enzym_counter += 1  # plus one to be syncronized with the next item
        print("-" * 50, "\n")
    except:
        print("Problem in \"knipt\" function.")

def lijst_doorlopen(seqs):
    for seq in seqs:
        if is_dna(seq):
            dna = True
        else:
            dna = False
    return dna


def zoek(woord, head, seq):
    try:
        for i in range(len(head)):

            if woord in head[i]:
                zoek_header = head[i]
                # print (zoek_header)
                zoek_seq = seq[i]
                # print(zoek_seq)
                # knipt(seq[i])

        return zoek_header, zoek_seq
    except:
        print("ERROR:", end=" ")
        print('\"', woord, '\"', sep="", end=" ")
        print("not found in file.")
main()
