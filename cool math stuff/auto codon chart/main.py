print("enter a codon")
codon = input(">. ").upper()

match codon[0]:
    case "U":
        match codon[1]:
            case "U":
                match codon[2]:
                    case "U" | "C":
                        print("Phenylalanine")
                    case "A" | "G":
                        print("Leucine")
            case "C":
                print("Serine")
            case "A":
                match codon[2]:
                    case "U" | "C":
                        print("Tyrosine")
                    case "A" | "G":
                        print("STOP")
            case "G":
                match codon[2]:
                    case "U" | "C":
                        print("Cysteine")
                    case "A":
                        print("STOP")
                    case "G":
                        print("Tryptophan")
    case "C":
        match codon[1]:
            case "U":
                print("Leucine")
            case "C":
                print("Proline")
            case "A":
                match codon[2]:
                    case "U" | "C":
                        print("Histidine")
                    case "A" | "G":
                        print("Glutamine")
            case "G":
                print("Arginine")
    case "A":
        match codon[1]:
            case "U":
                match codon[2]:
                    case "U" | "C" | "A":
                        print("Isoleucine")
                    case "G":
                        print("Methlonine")
            case "C":
                print("Threonine")
            case "A":
                match codon[2]:
                    case "U" | "C":
                        print("Asparagine")
                    case "A" | "G":
                        print("Lysine")
            case "G":
                match codon[2]:
                    case "U" | "C":
                        print("Serine")
                    case "A" | "G":
                        print("Arginine")
    case "G":
        match codon[1]:
            case "U":
                print("Valine")
            case "C":
                print("Alanine")
            case "A":
                match codon[2]:
                    case "U" | "C":
                        print("Aspartic Acid")
                    case "A" | "G":
                        print("Glutamic Acid")
            case "G":
                print("Glycine")