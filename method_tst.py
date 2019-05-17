weight=85
high=1.90
b_mass_index=weight/(high**2)

if b_mass_index<20:
    print("skinny")

if 20<b_mass_index<25:
    print("busty")

if b_mass_index>25:
    print("over")
