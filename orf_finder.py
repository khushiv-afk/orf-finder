def find_orfs(dna):
    dna = dna.upper()
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []

    for i in range(len(dna) - 2):
        codon = dna[i:i+3]

        if codon == start_codon:
            for j in range(i, len(dna)-2, 3):
                stop_codon = dna[j:j+3]

                if stop_codon in stop_codons:
                    orf = dna[i:j+3]
                    orfs.append(orf)
                    break

    return orfs


# -------- MAIN -------- #

sequence = input("Enter DNA sequence: ")
results = find_orfs(sequence)

if results:
    print("\nFound ORFs:")
    for idx, orf in enumerate(results, 1):
        print(f"{idx}. {orf} (Length: {len(orf)})")
else:
    print("No ORFs found.")
