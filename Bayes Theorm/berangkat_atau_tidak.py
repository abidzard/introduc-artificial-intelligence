# Abidzard Lintang Adhiasta
# 1910631170149 - 5G

def rumus_bayes(p_h, p_m, p_m_ke_h):
    # menghitung kejadian h bersyarat m P(H|M)
    p_h_ke_m = (p_h * p_m_ke_h) / p_m
    return p_h_ke_m

# P(H)
p_h = 12/30

# P(M)
p_m = 30/100

# P(M|H)
p_m_ke_h = 55/100

# Menghitung P(H|M)
hasil = rumus_bayes(p_h, p_m, p_m_ke_h)

if hasil <= 40/100:
    print("Saya akan tetap pergi")
else:
    print("Saya tidak akan pergi")

print("P(H|M) = %.2f%%" % (hasil * 100))