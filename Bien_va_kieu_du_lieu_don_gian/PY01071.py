'''print('yes' if input()[-3:].lower() == '.py' else 'no')'''

def check(inp : str):
    if len(inp) < 3: return False
    inp = inp.lower()
    if inp[-3:] != '.py': return False
    for c in inp:
        if not c.isalpha and ord(c) != ord('.') and ord(c) != ord('_'): return False
    return True

print('yes' if check(input()) else 'no')