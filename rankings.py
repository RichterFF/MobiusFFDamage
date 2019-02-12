from dmgcalc import *
from cards import *


def Rankings(joblist, card, weakness=True, broken=False, chain=True):
    ''' Calculate job rankings for a given card '''
    blank = Weapon()  # assume a blank weapon with no abilities or stats
    buffs = Buffs()  # no active buffs
    status = CurrentStatus(health=100, ultGauge=100, orbs=16)
    if weakness:
        monsterElement = WeaknessElement(card.element) 
    else:
        monsterElement = Neutral

    monster = Monster(defense=35, element=monsterElement)
    monster.broken=broken
    status.ability = chain
    status.attuned = chain
    rankings = [];
    for job in joblist:
        # [non-crit, weighted avg, crit]
        [ncr,av,cr] = cardDamage(job, card, monster, buffs, status, wpn=blank)
        rankings.append([ncr, av, cr, job.name])

    rankings = sorted(rankings, key=lambda x: -x[2]) # sort on crit damage
    #rankings = sorted(rankings, key=lambda x: -x[1]) # sort on avg damage
    return rankings
