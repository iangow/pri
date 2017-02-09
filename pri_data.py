political_bigrams_data = [
    ("and", "political", 21.42),
    ("the", "political", 10.59),
    ("to", "political", 3.45),
    ("actions", "in", 1.97),
    ("within", "our", 1.23),
    ("foundations", "of", 0.98),
    ("for", "regional", 0.92),
    ("appropriate", "balance", 0.74),
    ("our", "most", 0.74),
    ("practices", "and", 0.49),
    ("with", "regard", 0.49),
    ("the", "foundations", 0.49),
    ("loss", "ratio", 0.34),
    ("negotiate", "on", 0.25),
    ("cancellation", "of", 0.25),
    ("unchanged", "from", 0.25),
    ("size", "the", 0.25),
    ("nevertheless", "be", 0.25),
    ("was", "unique", 0.25),
    ("balance", "came", 0.25),
    ("the", "professional", 0.25),
    ("diligently", "to", 0.25), 
    ("resolution", "to", 0.25), 
    ("significantly", "reduced", 0.25), 
    ("global", "financial", 0.25), 
    ("demonstrated", "the", 0.25), 
    ("and", "professionalism", 0.21),
    ("year", "includes", 0.21), 
    ("management", "practices", 0.21), 
    ("with", "ample", 0.21)
]

political_bigrams = [(b[0], b[1]) for b in political_bigrams_data]
bigram_weights = {(b[0], b[1]): b[2] for b in political_bigrams_data}

risk_synonyms_text = """
risk 155645
risks 45650
uncertainty 33278
variable 30566
chance 25354
pending 23947
possibility 22695
uncertainties 21623
uncertain 16883
doubt 13983
bet 10708
likelihood 8403
variability 8152
exposed 6931
threat 6797
probability 6760
varying 3995
unpredictable 3872
unclear 3766
speculative 3707
fear 3516
gamble 3137
hesitant 2849
reservation 2393
hazard 1937
risky 1883
tentative 1881
doubtful 1867
dangerous 1692
instability 1381
sticky 1371
tricky 1368
hazardous 1318
queries 1020
danger 1002
vague 987
fluctuating 971
unstable 841
query 791
erratic 782
unsettled 754
dilemma 729
jeopardize 722
unpredictability 685
hesitancy 663
jeopardy 565
unsure 509
unresolved 462
suspicion 452
riskier 443
irregular 374
risking 305
chancy 279
peril 266
unreliable 265
halting 224
hesitating 216
risked 205
unsafe 193
wager 171
debatable 170
dicey 169
undecided 161
undetermined 160
precarious 153
apprehension 137
indecision 136
wavering 128
faltering 114
iffy 111
quandary 87
hazy 84
treacherous 76
changeable 74
hairy 68
insecurity 61
perilous 55
riskiest 55
dubious 51
wariness 43
oscillating 41
unreliability 39
riskiness 38
insecure 37
tentativeness 36
qualm 30
vagueness 26
equivocation 26
menace 20
scepticism 19
indecisive 17
vacillating 13
imperil 13
dodgy 12
gnarly 12
disquiet 9
vacillation 9
equivocating 9
incalculable 8
unconfident 7
ambivalence 6
parlous 6
diffident 5
untrustworthy 5
changeability 4
misgiving 4
undependable 3
fickleness 3
fitful 2
doubtfulness 1
fluctuant 1
"""

def get_synonyms(synonym_text):
    lines = [line for line in risk_synonyms_text.split("\n") if line != '']
    synonyms = [line.split()[0] for line in lines]
    return synonyms

risk_synonyms = get_synonyms(risk_synonyms_text)