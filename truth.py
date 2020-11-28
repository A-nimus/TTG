import ttg

prop = [p for p in input('[+]ENTER THE PROPOSITIONS SEPERATED WITH SPACE: \n |\n |\n |\n |------[+] ').strip().split()]

con = [c for c in input('\n[+]ENTER THE CONDITION(s) SEPERATED WITH HYPHEN(-): \n |\n |\n |\n |------[+] ').strip().split('-')]


try:
    print('\n'+'-'*21+'TRUTH TABLE'+'-'*21)
    print(ttg.Truths(prop , con))
    
except:
    print('\n'+'-'*17+'DEFAULT TRUTH TABLE'+'-'*17)
    print(ttg.Truths(['p', 'q'] , ['p or q', 'p and q', 'p = q', 'p=>q']))
