gene=''''''
name_organism=""
aantal_a=gene.count("A")
aantal_t=gene.count("T")
aantal_c=gene.count("C")
aantal_g=gene.count("G")
total_nucleotides=aantal_a + aantal_t + aantal_c + aantal_g
print("Organisme: " + name_organism)
print("Aantal nucleotiden: " + str(total_nucleotides))
print("GC%: " + str((aantal_c + aantal_g) / total_nucleotides * 100))
