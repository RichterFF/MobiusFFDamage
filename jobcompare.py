from dmgcalc import *
from cards import *
from jobs import *



#diamanterrapin = Monster(defense=75, element=Earth)

lightMonster = Monster(defense=35, element=Light)
darkMonster = Monster(defense=35, element=Dark)
waterMonster = Monster(defense=35, element=Water)
fireMonster = Monster(defense=35, element=Fire)
earthMonster = Monster(defense=35, element=Earth)
windMonster = Monster(defense=35, element=Wind)


########################
# Buffs and Status
########################
buffs = Buffs()

status = CurrentStatus(health=100, ultGauge=100, orbs=16)
status.orbs = 16

########################
# Monster
########################
monster = waterMonster
monster.isSicarius = True
monster.display()

joblist = loadJobs()

########################
# Rankings
########################
def Rankings(joblist, card, weakness=True, broken=False, chain=True):
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

print("\nFusoya: Unbroken Weakness, Chain")
rankings = Rankings(joblist, Fusoya, weakness=True, broken=False, chain=True) 
for ii in range(6): print('%d\t%d\t%d\t%s' % tuple(rankings[ii]))

print("\nFusoya: Unbroken Weakness, No Chain")
rankings = Rankings(joblist, Fusoya, weakness=True, broken=False, chain=False) 
for ii in range(6): print('%d\t%d\t%d\t%s' % tuple(rankings[ii]))

print("\nFusoya: Unbroken Neutral, No Chain")
rankings = Rankings(joblist, Fusoya, weakness=False, broken=False, chain=False) 
for ii in range(6): print('%d\t%d\t%d\t%s' % tuple(rankings[ii]))

print("\nFusoya: Broken Weakness, Chain")
rankings = Rankings(joblist, Fusoya, weakness=True, broken=True, chain=True) 
for ii in range(6): print('%d\t%d\t%d\t%s' % tuple(rankings[ii]))

print("\nFusoya: Broken Weakness, No Chain")
rankings = Rankings(joblist, Fusoya, weakness=True, broken=True, chain=False) 
for ii in range(6): print('%d\t%d\t%d\t%s' % tuple(rankings[ii]))

########################
# Specific Comparisons
########################
sven = Weapon(attack=119, breakPower=114, magic=163, critStars=3)
sven.appliedBonus.ImprovedCrit(56)
sven.appliedBonus.PainfulBreak(40)
zeus = Weapon(attack=148, breakPower=148, magic=172, critStars=4)
zeus.appliedBonus.ImprovedCrit(62)
zeus.appliedBonus.ExploitWeakness(65)
blank = Weapon()
card = Fusoya


fv = findJob(joblist, 'fauviste.*hof')
pw = findJob(joblist, 'Witch.*Dmg')
ss = findJob(joblist, 'Skyseer')
mm = findJob(joblist, 'mermaid')
mj = findJob(joblist, 'Magitek Jester')


'''
monster.display()
#[ncr,av,cr] = cardDamage(fv, card,  monster, buffs, status, blank, debug=0)
#print('Fauviste HoF:   non-crit %.0f, crit %.0f avg %.0f' % (ncr, cr, av))
print("magic, ele, weakness, broken, extra, crit")
[ncr,av,cr] = cardDamage(pw, card,  monster, buffs, status, blank, debug=1)
print('Primeval Witch: non-crit %.0f, crit %.0f avg %.0f' % (ncr, cr, av))
[ncr,av,cr] = cardDamage(ss, card,  monster, buffs, status, blank, debug=1)
print('Skyseer:        non-crit %.0f, crit %.0f avg %.0f' % (ncr, cr, av))
[ncr,av,cr] = cardDamage(mm, card,  monster, buffs, status, blank, debug=1)
print('Mermaid:        non-crit %.0f, crit %.0f avg %.0f' % (ncr, cr, av))
[ncr,av,cr] = cardDamage(mj, card,  monster, buffs, status, blank, debug=1)
print('Jester:         non-crit %.0f, crit %.0f avg %.0f' % (ncr, cr, av))
print('%s ' % (pw.name))
[ncr,av,cr] = cardDamage(pw, card,  monster, buffs, status, blank, debug=1)
print('%s ' % (ss.name))
[ncr,av,cr] = cardDamage(ss, card,  monster, buffs, status, blank, debug=1)
print('%s ' % (mm.name))
[ncr,av,cr] = cardDamage(mm, card,  monster, buffs, status, blank, debug=1)
print('%s ' % (mj.name))
[ncr,av,cr] = cardDamage(mj, card,  monster, buffs, status, blank, debug=1)
'''
