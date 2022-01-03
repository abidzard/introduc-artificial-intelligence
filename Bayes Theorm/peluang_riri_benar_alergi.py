# Abidzard Lintang Adhiasta
# 1910631170149 - 5G

def teori_bayes(p_a, p_b_ke_a, p_b_ke_not_a):
    # rumus P(notA)
    p_not_a = 1 - p_a
    # rumus P(A|B)
    p_a_ke_b = (p_b_ke_a * p_a) / (p_b_ke_a * p_a + p_b_ke_not_a * p_not_a)
    return p_a_ke_b

# nilai P(A)
p_a = 1/50

# nilai P(B|A)
p_b_ke_a = 17/20

# nilai P(B|notA)
p_b_ke_not_a = 1/10

# menghitung P(A|B)
hasil = teori_bayes(p_a, p_b_ke_a, p_b_ke_not_a)

print("P(A) = %.0f%%" % (p_a * 100))
print("P(B|A) = %.0f%%" % (p_b_ke_a * 100))
print("P(B|notA) = %.0f%%" % (p_b_ke_not_a * 100))
print("---------------------------------------------------")
print("Peluang Riri benar memiliki alergi adalah %.4f%%" % (hasil * 100))
print("P(A|B) = %.4f%%" % (hasil * 100))