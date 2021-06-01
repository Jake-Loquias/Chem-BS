#Script to amino acid peptide converter baby

def pepFunc():
    met = int(len(script))-1
    roNome = 0
    pepTide = ""

    pepPar = {
        'A': "Alanine",
        'B': "Aspartic acid",
        'C': "Cysteine",
        'D': "Aspartic acid",
        'E': "Glutamic acid",
        'F': "Phenylalanine",
        'G': "Glycine",
        'H': "Histidine",
        'I': "Isoleucine",
        'J': "Isoleucine",
        'K': "Lysine",
        'L': "Leucine",
        'M': "Methionine",
        'N': "Asparagine",
        'O': "Pyrrolysine",
        'P': "Proline",
        'Q': "Glutamine",
        'R': "Arginine",
        'S': "Serine",
        'T': "Threonine",
        'U': "Selenocysteine",
        'V': "Valine",
        'W': "Tryptophan",
        'X': "Glutamic acid",
        'Y': "Tyrosine",
        'Z': "Glutamic acid",
        'a': "alanine",
        'b': "aspartic acid",
        'c': "cysteine",
        'd': "aspartic acid",
        'e': "glutamic acid",
        'f': "phenylalanine",
        'g': "glycine",
        'h': "histidine",
        'i': "isoleucine",
        'j': "isoleucine",
        'k': "lysine",
        'l': "leucine",
        'm': "methionine",
        'n': "asparagine",
        'o': "pyrrolysine",
        'p': "proline",
        'q': "glutamine",
        'r': "arginine",
        's': "serine",
        't': "threonine",
        'u': "selenocysteine",
        'v': "valine",
        'w': "tryptophan",
        'x': "glutamic acid",
        'y': "tyrosine",
        'z': "glutamic acid"
    }
    pepper = {
        ' ': " ",
        'A': "Alanyl",
        'B': "Asparagyl",
        'C': "Cysteinyl",
        'D': "Aspartyl",
        'E': "Glutamyl",
        'F': "Phenylalanyl",
        'G': "Glycinyl",
        'H': "Histidyl",
        'I': "Isoleucyl",
        'J': "Leucyl",
        'K': "Lysyl",
        'L': "Leucyl",
        'M': "Methionyl",
        'N': "Asparagyl",
        'O': "Pyrrolysyl",
        'P': "Prolinyl",
        'Q': "Glutamyl",
        'R': "Arginyl",
        'S': "Serinyl",
        'T': "Threonyl",
        'U': "Selenocystyl",
        'V': "Valinyl",
        'W': "Tryptophanyl",
        'X': "Glutamyl",
        'Y': "Tyrosyl",
        'Z': "Glutamyl",
        'a': "alanyl",
        'b': "asparagyl",
        'c': "cysteinyl",
        'd': "aspartyl",
        'e': "glutamyl",
        'f': "phenylalanyl",
        'g': "glycinyl",
        'h': "histidyl",
        'i': "isoleucyl",
        'j': "leucyl",
        'k': "lysyl",
        'l': "leucyl",
        'm': "methionyl",
        'n': "asparagyl",
        'o': "pyrrolysyl",
        'p': "prolinyl",
        'q': "glutamyl",
        'r': "arginyl",
        's': "serinyl",
        't': "threonyl",
        'u': "selenocystyl",
        'v': "valinyl",
        'w': "tryptophanyl",
        'x': "glutamyl",
        'y': "tyrosyl",
        'z': "glutamyl"
    }
    while met >= roNome:
        if roNome==met:
            pepTide = pepTide + (pepPar[script[roNome]])
        else:
            if script[roNome+1]==" ":
                pepTide = pepTide + (pepPar[script[roNome]])
            else:
                pepTide = pepTide + (pepper[script[roNome]])
        roNome=roNome+1
    print('Your amino acid peptide is:')
    print(pepTide)



print('Input the script you want to turn into a peptide. Spell out numbers. Do not include punctuations.')
print('Additionally write in Title Case. ie "Each Word Starts Capitalized"')
print('Some letters such as B, J, Z, and X can refer to multiple amino acids.')
print('For the sake of not losing my sanity:')
print('B will be asparagyl or aspartic acid. J will be leucyl or isoleucine.')
print('Z and X will be glutamyl or glutamic acid.')
print(' ')

script = input("Enter your script: ")

pepFunc()
