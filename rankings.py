from dmgcalc import *
from cards import *
import copy


def Rankings(joblist, card, weakness=True, broken=False, chain=True, dona=False):
    ''' Calculate job rankings for a given card '''
    # make sure each job has a "blank" (0 stats, no buffs) weapon
    # this means we have to use a separate copy of joblist
    joblist = copy.deepcopy(joblist) 
    blank = Weapon()
    for job in joblist: job.weapon = blank

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
    status.dona = dona
    rankings = RankJobs(joblist, card, buffs, status, monster)
    return rankings

def RankJobs(joblist, card, buffs, status, monster):
    '''Calculate job (& wpn) rankings given: card, buffs, monster, & status'''
    rankings = [];
    for job in joblist:
        # [non-crit, weighted avg, crit]
        [ncr,av,cr] = cardDamage(job, card, monster, buffs, status)
        rankings.append([ncr, av, cr, job.name])

    rankings = sorted(rankings, key=lambda x: -x[2]) # sort on crit damage
    #rankings = sorted(rankings, key=lambda x: -x[1]) # sort on avg damage
    return rankings
