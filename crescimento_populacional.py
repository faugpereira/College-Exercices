pop_a = 9000000
pop_b = 20000000
tax_a = (1 + 0.03)
tax_b = (1 + 0.015)
anos = 0

while (pop_a <= pop_b):
    pop_a = (pop_a * tax_a)
    pop_b = (pop_b * tax_b)
    anos = anos + 1
print('\nA população A será {:.3f} \nA população B será {:.3f} \nSerão necessários {} anos para se chegar a isso.'.format(pop_a, pop_b, anos))
