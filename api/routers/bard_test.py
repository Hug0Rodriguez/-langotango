from bardapi import Bard

token = 'aAjFqAoOWzI8j174bxxnzksuffs3RLRtno3okXKX-c3jr-dV50MftEgT1k2jS0p6ZgEQmQ.'
bard = Bard(token=token)
bard.get_answer("hola me llamo beau")['content']
