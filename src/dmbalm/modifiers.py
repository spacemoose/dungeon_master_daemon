# Provide some functions for returning modifiers.

def lookup(score):
    assert(score>=1)
    assert(score<=30)
    modifier = (score - 10) // 2
    return modifier
