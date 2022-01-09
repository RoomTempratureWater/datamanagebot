import random
from texttable import Texttable
def welcome(name):
    list = [
        'Hi!, What do you need today',
        'YOOOOOOOOOOOOOOO',
        'Hi {} '.format(name),
        '{} is a cool name ngl,btw hewooo'.format(name),
        'I was waiting for your hello, now i can die peacefully',
        'Hewoo!',
        'Who hath summoned me, the greatest of all bots'
    ]

    return random.choice(list)

#for notes
notes = Texttable(max_width=40)

notes.set_deco(Texttable.HEADER)
notes.set_cols_dtype(['t','t'])
notes.set_cols_align(['l','r'])
notes.add_rows([['Command ','What it does'],
               ['/hello -','hellos you\n'],
               ['/notes -','list of commands\n'],
               ['/food -','shows you food places nearby\n'],
               ['/spacey -','shows you some cool space stuff\n'],
               ['/developer -','tells you the developer information\n']
               ])
note = notes.draw()

