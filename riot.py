from riotfuncs import get_puud
from riotfuncs import get_actid

gameName = ""
tagLine = ""

account = get_puud(gameName, tagLine)
print(account['gameName'] + " #" + account['tagLine'])
print("Your PUUID is: " + account['puuid'])
actid = get_actid()
'''if actid:
    for act in actid:
        act_name = act.get('name')
        act_id = act.get('id')
        is_active = act.get('isActive')

        print(f"Act ID: {act_id}")
    else:
        print("No act info available.")'''
