entity1="tree flower sun warm green"
entity2 ="tree flower sun hot green"
entity3 ="tree leaves yellow cold sun"
entity4 ="tree snow white cold cloud"
entity5 ="tree family holiday red travel"
entity6 ="tree open school warm happy"

def dice_coefficient(a, b):
    """dice coefficient 2nt/na + nb."""
    if not len(a) or not len(b): return 0.0
    if len(a) == 1:  a = a + u'.'
    if len(b) == 1:  b = b + u'.'

    a_bigram_list = []
    for i in range(len(a) - 1):
        a_bigram_list.append(a[i:i + 2])
    b_bigram_list = []
    for i in range(len(b) - 1):
        b_bigram_list.append(b[i:i + 2])

    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)
    dice_coeff = overlap * 2.0 / (len(a_bigrams) + len(b_bigrams))
    return round(dice_coeff,2)

print(dice_coefficient(entity1, entity5))
print(dice_coefficient(entity5, entity6))
print(dice_coefficient(entity1, entity6))
