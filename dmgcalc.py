import copy
import pdb
import math

# elements
Neutral = 0; Fire = 1; Water = 2; Wind = 3; Earth = 4; Light = 5; Dark = 6;
Air = 3  # synonym for Wind
ElementNames = ["Neutral", "Fire", "Water", "Wind", "Earth", "Light", "Dark"]

# job types
Warrior=0; Mage=1; Ranger=2; Monk=3; Meia=4; Sarah=5; Sophie=6; Graff=7
TypeNames = ["Warrior", "Ranger", "Monk", "Meia", "Sarah", "Sophie", "Graff"]

def OppositeElement(element):
    if element == Fire: return Water
    if element == Water: return Fire
    if element == Wind: return Earth
    if element == Earth: return Wind
    if element == Light: return Dark
    if element == Dark: return Light
    return Neutral


class Abilities:  # including fractals
    def __init__(self):
        self.elementEnhance = [0, 0, 0, 0, 0, 0, 0] 
        self.attackUp = 0
        self.magicUp = 0
        self.breakUp = 0
        self.abilityChain = 0
        self.attunedChain = 0
        self.improvedCrit = 0
        self.exploitWeakness = 0
        self.painfulBreak = 0
        self.scourge = 0
        self.ravage = 0  # increases damage of aoe/cone attacks

    def EnhanceFire(self, value): self.elementEnhance[Fire] = value
    def EnhanceWater(self, value): self.elementEnhance[Water] = value
    def EnhanceWind(self, value): self.elementEnhance[Wind] = value
    def EnhanceEarth(self, value): self.elementEnhance[Earth] = value
    def EnhanceLight(self, value): self.elementEnhance[Light] = value
    def EnhanceDark(self, value): self.elementEnhance[Dark] = value
    def AttackUp(self, value): self.attackUp = value
    def MagicUp(self, value): self.magicUp = value
    def BreakUp(self, value): self.breakUp = value
    def AbilityChain(self, value): self.abilityChain = value
    def AttunedChain(self, value): self.attunedChain = value
    def ImprovedCrit(self, value): self.improvedCrit = value
    def ImprovedCriticals(self, value): self.improvedCrit = value
    def ExploitWeakness(self, value): self.exploitWeakness = value
    def PainfulBreak(self, value): self.painfulBreak = value
    def Scourge(self, value): self.scourge = value
    def Ravage(self, value): self.ravage = value

    def addAbilities(self, abilities):
        for ii in range(3): 
            self.elementEnhance[ii] = self.elementEnhance[ii] \
                                    + abilities.elementEnhance[ii]
        self.attackUp = self.attackUp + abilities.attackUp
        self.magicUp = self.magicUp + abilities.magicUp
        self.breakUp = self.breakUp + abilities.breakUp
        self.abilityChain =self.abilityChain + abilities.abilityChain
        self.attunedChain = self.attunedChain + abilities.attunedChain
        self.improvedCrit = self.improvedCrit + abilities.improvedCrit
        self.exploitWeakness = self.exploitWeakness + abilities.exploitWeakness
        self.painfulBreak = self.painfulBreak + abilities.painfulBreak
        self.scourge = self.scourge + abilities.scourge
        self.ravage = self.ravage + abilities.ravage

    def AbilString(self):
        abstr = " Enhance: [F:%d, W:%d, A:%d, E:%d, L:%d, D:%d]" % \
                (tuple(self.elementEnhance[1:]))
        if self.attackUp > 0: abstr = abstr + "\n Attack up %d" % (self.attackUp)
        if self.magicUp > 0: abstr = abstr + "\n Magic up %d" % (self.magicUp)
        if self.breakUp > 0: abstr = abstr + "\n Break up %d" % (self.breakUp)
        if self.abilityChain > 0: abstr = abstr + "\n Ability Chain %d" % (self.abilityChain)
        if self.attunedChain > 0: abstr = abstr + "\n Attuned Chain %d" % (self.attunedChain)
        if self.improvedCrit > 0: abstr = abstr + "\n Improved Crit %d" % (self.improvedCrit)
        if self.exploitWeakness > 0: abstr = abstr + "\n Exploit Weakness %d" % (self.exploitWeakness)
        if self.painfulBreak > 0: abstr = abstr + "\n Painful Break %d" % (self.painfulBreak)
        if self.scourge > 0: abstr = abstr + "\n Scourge %d" % (self.scourge)
        if self.ravage > 0: abstr = abstr + "\n Ravage %d" % (self.ravage)
        return abstr

    def display(self):
        print(self.AbilString())

class Weapon:  
    def __init__(self, name="", attack=0, magic=0, breakPower=0, critStars=0):
        self.name = name
        self.attack = attack
        self.breakPower = breakPower
        self.magic = magic
        self.critStars = critStars

        self.appliedBonus = Abilities()

    def WpnString(self):
        wpnstr = " Name: %s; attack %d; break %d; magic %d; crit* %d" % \
            (self.name, self.attack, self.breakPower, self.magic, self.critStars)
        bonusStr = self.appliedBonus.AbilString()
        if bonusStr:
            wpnstr = wpnstr + "\n" + bonusStr
        return wpnstr

    def display(self):
        print(self.WpnString())



class Buffs:
    def __init__(self, brave=False, faith=False, trance=False, boost=False, \
                       snipe=False, berserk=False, enhancedElement=0, \
                       attackIgnition=False, abilityIgnition=False):
        self.brave = brave   # 100% increase to attack stat (only applies
                             #  to ultimates and yellow break damage)
        self.faith = faith   # 50% increase to magic stat
        self.trance = trance # 30% attack, break, magic
        self.boost = boost   # 100% increase to break stat
        self.snipe = snipe   # 30% increase in crit chance
        self.berserk = berserk  # 50% element enhance, 50% increase to ult attack, 
                                # 50% increase to tap attack dmg, unless imbued 
                                # weapon, in which case enhance element get applied

        self.enhancedElement = enhancedElement  # num stacks of Enhance Element (25% increase per stack)
        self.attackIgnition = attackIgnition    # 50% increase to next tap or ult attack. 
                                                # (25% if brave is active)
        self.abilityIgnition = abilityIgnition  # 25% increase to next ability (16.7% if 
                                                # faith is active)

    def Brave(self, value=True): self.brave = value
    def Faith(self, value=True): self.faith = value
    def Trance(self, value=True): self.trance = value
    def Boost(self, value=True): self.boost = value
    def Snipe(self, value=True): self.snipe = value
    def Berserk(self, value=True): self.berserk = value
    def EnhancedElement(self, value=True): self.enhancedElement = value
    def AttackIgnition(self, value=True): self.attackIgnition = value
    def AbilityIgnition(self, value=True): self.abilityIgnition = value

    def addBuffs(self, buffs):
        if buffs.brave: self.brave = True
        if buffs.faith: self.faith = True
        if buffs.trance: self.trance = True
        if buffs.boost: self.boost = True
        if buffs.snipe: self.snipe = True
        if buffs.berserk: self.berserk = True
        if buffs.enhancedElement > self.enhancedElement: 
            self.enhancedElement = buffs.enhancedElement
        if buffs.attackIgnition: self.attackIgnition = True
        if buffs.abilityIgnition: self.abilityIgnition = True

    def BuffString(self):
        bufstr = ""
        if self.brave: bufstr = bufstr + ", Brave"
        if self.faith: bufstr = bufstr + ", Faith"
        if self.trance: bufstr = bufstr + ", Trance"
        if self.boost: bufstr = bufstr + ", Boost"
        if self.snipe: bufstr = bufstr + ", Snipe"
        if self.berserk: bufstr = bufstr + ", Berserk"
        if self.enhancedElement > self.enhancedElement: 
            bufstr = bufstr + ", Enhanced Element"
        if self.attackIgnition: bufstr = bufstr + ", Attack Ignition"
        if self.abilityIgnition: bufstr = bufstr + ", Ability Ignition"
        if bufstr: bufstr = bufstr[2:]
        return(bufstr)

    def display():
        bufstr = self.BuffString()
        print(bufstr) if skstr else print("No buffs")

class Debuffs:
    def __init__(self, unguard=False, debarrier=False, bio=False, bdd=False, \
                       crd=False, weaken=False):
        self.unguard = unguard      # reduce monster defense to 0
        self.debarrier = debarrier  # 50% increase in damage taken
        self.bio = bio              # 5% max HP poison damage
        self.bdd = bdd              # break defense down: 50% increase in break damage
        self.crd = crd              # critical resist down: 60% increase in crit chance
        self.weaken = weaken        # 50% exploit weakness (elemental dmg)

    def Unguard(self, value=True): self.unguard = value
    def Debarrier(self, value=True): self.debarrier = value
    def Bio(self, value=True): self.bio = value
    def Bdd(self, value=True): self.bdd = value
    def Crd(self, value=True): self.crd = value
    def Weaken(self, value=True): self.Weaken = value

    def addDebuffs(self, debuffs):
        if debuffs.unguard: self.unguard = True
        if debuffs.debarrier: self.debarrier = True
        if debuffs.bio: self.bio = True
        if debuffs.bdd: self.bdd = True
        if debuffs.crd: self.crd = True
        if debuffs.weaken: self.weaken = True

    def DebuffString(self):
        dbstr = ""
        if self.unguard: dbstr = dbstr + ", Unguard"
        if self.debarrier: dbstr = dbstr + ", Debarrier"
        if self.bio: dbstr = dbstr + ", Bio"
        if self.bdd: dbstr = dbstr + ", BDD"
        if self.crd: dbstr = dbstr + ", CRD"
        if self.weaken: dbstr = dbstr + ", Weaken"
        if dbstr: dbstr = dbstr[2:]
        return(dbstr)

    def display():
        dbstr = self.DebuffString()
        print(dbstr) if skstr else print("No debuffs")




class ExtraSkills:
    def __init__(self, imbueElement=False, sicariusHunter=False, \
                sicariusKiller=False, bloodthirst=False, \
                vitalityTap=False, breakExploiter=False, \
                critWeakness=False, elementTap=False, breakerKiller=False, \
                critSundering=False, bloodTap=False, martialArts=False, \
                martialFlow=False, martialCombat=False, critRupture=False, \
                meiaSynchro = False):
        self.imbueElement = imbueElement     # imbues tap attacks with an element
        self.sicariusHunter = sicariusHunter # 10% damage to named sicarius type
        self.sicariusKiller = sicariusKiller # 40% damage to named sicarius type
        self.bloodthirst = bloodthirst       # 15% damage to broken target
        self.vitalityTap = vitalityTap       # enhance element up by 0.3*(health %)^3
        self.breakExploiter = breakExploiter # 25% damage to broken target if weakness
        #self.weaknessBreaker = False # 20% increased break dmg to weakness
        self.critWeakness = critWeakness     # 15% increased crit chance if weakness
        self.elementTap = elementTap         # enhance element up by 0.3(*orbs/16)^3
        self.breakerKiller = breakerKiller   # 15% increased crit chance if broken
        self.critSundering = critSundering   # 30% increase break on critical hit
        self.bloodTap = bloodTap             # enhance element up by 0.3*(1-health%)^3
        self.martialArts = martialArts       # tap attack dmg up by 70% * sqrt(ult gauge%)
        self.martialFlow = martialFlow       # tap attack break stat up by 30%*(ult gauge)^2
        self.martialCombat = martialCombat   # enhance element up by 0.5*(ult gauge)^2
        self.critRupture = critRupture       # reduces defense by 20%, and adds 30%
                                             # to crit damage
        self.meiaSynchro=meiaSynchro         # adds 10% magic if meia job
        self.armiger = False                 # supreme UB ability: adds 0.9 × (health)^0.8 dmg

    def ImbueElement(self, value=True): self.imbueElement = value
    def SicariusHunter(self, value=True): self.sicariusHunter = value
    def SicariusKiller(self, value=True): self.sicariusKiller = value
    def Bloodthirst(self, value=True): self.bloodthirst = value
    def VitalityTap(self, value=True):   self.vitalityTap = value
    def BreakExploiter(self, value=True): self.breakExploiter = value
    def CritWeakness(self, value=True): self.critWeakness = value
    def CriticalWeakness(self, value=True): self.critWeakness = value
    def ElementTap(self, value=True): self.elementTap = value
    def BreakerKiller(self, value=True): self.breakerKiller = value
    def CritSundering(self, value=True): self.critSundering = value
    def BloodTap(self, value=True): self.bloodTap = value
    def MartialArts(self, value=True): self.martialArts = value
    def MartialFlow(self, value=True): self.martialFlow = value
    def MartialCombat(self, value=True): self.martialCombat = value
    def CritRupture(self, value=True): self.critRupture = value
    def CriticalRupture(self, value=True): self.critRupture = value
    def MeiaSynchro(self, value=True): self.meiaSynchro = value

    def SkillStr(self):
        skstr = ""
        if (self.imbueElement): skstr = skstr + ", Imbue"
        if (self.sicariusHunter): skstr = skstr + ", Sic Hunter"
        if (self.sicariusKiller): skstr = skstr + ", Sic Killer"
        if (self.bloodthirst): skstr = skstr + ", Bloodthirst"
        if (self.vitalityTap): skstr = skstr + ", Vitality Tap"
        if (self.breakExploiter): skstr = skstr + ", Break Exploiter"
        if (self.critWeakness): skstr = skstr + ", Crit Weakness"
        if (self.elementTap): skstr = skstr + ", Element Tap"
        if (self.breakerKiller): skstr = skstr + ", Breaker Killer"
        if (self.critSundering): skstr = skstr + ", Crit Sundering"
        if (self.bloodTap): skstr = skstr + ", Blood Tap"
        if (self.martialArts): skstr = skstr + ", Martial Arts"
        if (self.martialFlow): skstr = skstr + ", Martial Flow"
        if (self.martialCombat): skstr = skstr + ", Martial Combat"
        if (self.critRupture): skstr = skstr + ", Crit Rupture"
        if (self.meiaSynchro): skstr = skstr + ", Meia Synchro"
        if skstr: skstr = skstr[2:]
        return(skstr)

    def display(self):
        skstr = self.SkillStr()
        print(skstr) if skstr else print("No skills")

class Job:
    def __init__(self, name="", attack=0, magic=0, breakPower=0, critStars=0, limitBreak=False):
        self.name = name
        self.attack = attack
        self.magic = magic
        self.breakPower = breakPower
        self.critStars = critStars
        self.elements = [0, 0, 0, 0, 0, 0, 0]
        self.lore = []

        self.isMeia = False
        self.abilities = Abilities()
        self.attackLimitBreak = limitBreak # tap attacks can break 9999 damage

    def JobString(self):
        jobstr = "%s: attack %d; break %d; magic %d; critStars %d" % \
            (self.name, self.attack, self.breakPower, self.magic, self.critStars)
        jobstr = jobstr + "\n Elements: "
        if self.elements[Fire]: jobstr = jobstr + "F"
        if self.elements[Water]: jobstr = jobstr + "W"
        if self.elements[Wind]: jobstr = jobstr + "A"
        if self.elements[Earth]: jobstr = jobstr + "E"
        if self.elements[Light]: jobstr = jobstr + "L"
        if self.elements[Dark]: jobstr = jobstr + "D"

        abstr = self.abilities.AbilString()
        if abstr: jobstr = jobstr + "\n" + abstr
        if self.attackLimitBreak: jobstr = jobstr + " Attack Limit Broken"
        return jobstr

    def display(self):
        print(self.JobString())




# weapon stats folded into job
#class Weapon:  
#    def __init__(self):
#        self.attack = 0
#        self.breakPower = 0
#        self.magic = 0
#        self.critStars = 3
#
#        self.abilities = Abilities()


class AbilityCard:
    def __init__(self, attack=0, breakPower=0, critStars=0, element=Neutral, area=False, \
                    jobType=''):
        self.attack = attack
        self.breakPower = breakPower
        self.critStars = critStars
        self.element = element
        self.area = area  # True if area or cone attack
        self.jobtype = jobType

        self.skills = ExtraSkills()
        self.appliedBonus = Abilities()
        self.appliedBuffs = Buffs()
        self.appliedDebuffs = Debuffs()

    def display(self):
        print('atk: %d; brk %d; critStar %d; area? %s; element %s; type %s' %
               (self.attack, self.breakPower, self.critStars,  \
                "Y" if self.area else "N", \
                ElementNames[self.element], TypeNames[self.jobtype]))
        skString = self.skills.SkillStr()
        abilString = self.appliedBonus.AbilString()
        bufString = self.appliedBuffs.BuffString()
        debuffString = self.appliedDebuffs.DebuffString()
        if skString: print(" " + skString)
        if abilString: print(abilString)
        if bufString: print(" " + bufString)
        if debuffString: print(" " + debuffString)

class CurrentStatus:
    def __init__(self, health=100, ultGauge=100, orbs=16, ability=True, attuned=True):
        self.health = health        # health percentage from 0 to 100
        self.ultGauge = ultGauge    # ultmate gauge percentage from 0 to 100
        self.orbs = orbs            # number of orbs from 0 to 16
        self.ability = ability      # ability chain active?
        self.attuned = attuned      # attuned chain active?

    def display(self):
        print('Status: health %d; ult %d; orbs %d, abilty %d; attuned %d' %
          (self.health, self.ultGauge, self.orbs,  self.ability, self.attuned))

class Monster:
    def __init__(self, defense=0, element=Neutral, broken=False, isSicarius=False):
        self.defense = defense  # from 0 to 100
        self.element = element
        self.debuffs = Debuffs()
        self.broken = broken
        self.isSicarius = isSicarius  # is a sicarius of the type that is vulnerable to the 
                                      # Hunter/Killer extra skills on sicarius cards
    def display(self):
        print('\nelement: %s, defense: %d, broken %s, sicarius? %s' % \
                (ElementNames[self.element], self.defense, \
                 'Y' if self.broken else 'N', \
                 'Y' if self.isSicarius else 'N'))

##########################################
# Damage Calculation
##########################################
# red break damage calculation (for later)
# BD(red) = [ base break power x Boost x (Enelement + Exploit Weakness) x BDD ] x Piercing Break  
# boost = 100%; enelment = 30%; BDD = 50%


def weaknessElement(element):
  if element==Fire: return Water
  if element==Water: return Fire
  if element==Wind: return Earth
  if element==Earth: return Wind
  if element==Light: return Dark
  if element==Dark: return Light
  return -1  # neutral: no weakness


def cardDamage(job, card, monster, startingBuffs, status, wpn=[], debug=0):
# assume auto abilities on cards are already counted in job abilities

    debuffs = copy.deepcopy(monster.debuffs)
    skills = copy.deepcopy(card.skills)
    abilities = copy.deepcopy(job.abilities)
    critStars = job.critStars + card.critStars
    if wpn: critStars = critStars + wpn.critStars

    # add effects of ability card
    buffs = copy.deepcopy(startingBuffs)
    buffs.addBuffs(card.appliedBuffs)
    debuffs.addDebuffs(card.appliedDebuffs)
    abilities.addAbilities(card.appliedBonus)
    if wpn: abilities.addAbilities(wpn.appliedBonus)

    # magic modifier
    magic = 1.0
    if card.jobtype in job.lore:
        magic = 1 + job.magic/100
    if not job.elements[card.element]: magic = 0
 

    if job.isMeia and skills.meiaSynchro: 
        magic = magic * 1.1 
    if buffs.faith: magic = magic * 1.5
    if buffs.trance: magic = magic * 1.3
    if wpn: magic = magic + wpn.magic

    # element Damage
    elementFactor = 1 + abilities.elementEnhance[card.element]/100
    elementFactor = elementFactor + 0.25*buffs.enhancedElement
    if status.ability:
        elementFactor = elementFactor + abilities.abilityChain/100
    if status.attuned:
        elementFactor = elementFactor + abilities.attunedChain/100
    if buffs.berserk:       elementFactor = elementFactor + 0.5
    if skills.vitalityTap:   elementFactor = elementFactor + 0.3*pow(status.health/100, 3)
    if skills.bloodTap:      elementFactor = elementFactor + 0.3*pow(1 - status.health/100, 3)
    if skills.elementTap:    elementFactor = elementFactor + 0.3*pow(status.orbs/16, 3)
    if skills.martialCombat: elementFactor = elementFactor + 0.5*pow(status.ultGauge/100, 2)

    # criticals
    critFactor = 1.5  # base factor
    critFactor = critFactor + abilities.improvedCrit/100
    if skills.critRupture: critFactor = critFactor + 0.3

    critChance = 0.05 * critStars
    if monster.broken and skills.breakerKiller:
        critChance = critChance + 0.15
    if buffs.snipe: critChance = critChance + 0.3
    if debuffs.crd: critChance = critChance + 0.6
    if critChance > 1: critChance = 1

    # weakness
    weakness = (card.element == weaknessElement(monster.element))
    if weakness:
        weaknessFactor = 2 + abilities.exploitWeakness/100;
        if debuffs.weaken: 
            weaknessFactor = weaknessFactor + 0.5
    else:
        weaknessFactor = 1

    # broken 
    if monster.broken:
        brokenFactor = 2 + abilities.painfulBreak/100;
    else:
        brokenFactor = 1

    # extra factors
    extraFactor = 1
    if monster.broken and weakness and skills.breakExploiter: 
        extraFactor = extraFactor * 1.25
    if monster.isSicarius and skills.sicariusHunter:
        extraFactor = extraFactor * 1.1
    if monster.isSicarius and skills.sicariusKiller:
        extraFactor = extraFactor * 1.4
    if monster.broken and skills.bloodthirst:
        extraFactor = extraFactor * 1.15
    if buffs.abilityIgnition:
        if buffs.faith: 
            extraFactor = extraFactor * 1.167
        else:
            extraFactor = extraFactor * 1.25
    if debuffs.debarrier:
        extraFactor = extraFactor * 1.5
    if abilities.ravage > 0 and abilities.area:
        extraFactor = extraFactor * (1 + abilities.ravage)
    if skills.armiger:
        healthFrac = status.health/100
        extraFactor = extraFactor * (1 + 0.9*math.pow(healthFrac, 0.8))

    # monster defense
    defense = monster.defense/100
    if debuffs.unguard or monster.broken:
        defense = 0
    elif skills.critRupture:
        defense = max(0, defense - 0.2)
    defenseFactor = 1 - defense

    baseDamage = card.attack * magic * elementFactor * weaknessFactor \
                             * brokenFactor * extraFactor * defenseFactor
    critDamage = baseDamage * critFactor
    avgDamage = (1-critChance)*baseDamage + critChance*critDamage


    factList = [magic, elementFactor, weaknessFactor, brokenFactor, \
                extraFactor, critFactor] 
    #print(list(map(lambda x: round(x,2), factList)))
    if debug>0:
        for factor in factList: print("%.2f" % (factor), end=' ')
        print("")
    #if debug>1: pdb.set_trace()
    return [baseDamage, avgDamage, critDamage]
