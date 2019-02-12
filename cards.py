from dmgcalc import *

# Ariadne
Ariadne = AbilityCard(attack=1200, breakPower=30, critStars=3, element=Earth)
Ariadne.area = True
Ariadne.skills.BreakExploiter()
Ariadne.skills.CriticalRupture()
Ariadne.skills.CriticalWeakness()
Ariadne.skills.ElementTap()
Ariadne.jobtype = Mage

# Tidus & 
Tidus = AbilityCard(attack=1080, breakPower=60, critStars=3, element=Water)
Tidus.area = False
Tidus.skills.Bloodthirst()
Tidus.skills.SicariusKiller()
Tidus.jobtype = Warrior

#Cluckatrice
Cluckatrice = AbilityCard(attack=2400, breakPower=1500, critStars=1, \
                          element=Light)
Cluckatrice.area=False
Cluckatrice.appliedBonus.ExploitWeakness(200)
Cluckatrice.skills.ImbueElement()
Cluckatrice.skills.MartialFlow()
Cluckatrice.skills.MartialArts()
Cluckatrice.skills.MartialCombat()
Cluckatrice.jobtype = Monk

# Fusoya
Fusoya = AbilityCard(attack=2550, breakPower=1200, critStars=3, element=Fire)
Fusoya.area = True
Fusoya.skills.BreakExploiter()
Fusoya.skills.CritWeakness()
Fusoya.appliedBonus.EnhanceFire(400)
Fusoya.jobtype = Mage

# Gaelicat
Gaelicat = AbilityCard(attack=2700, breakPower=450, critStars=3, element=Wind)
Gaelicat.appliedBonus.ImprovedCrit(200)
Gaelicat.skills.ImbueElement()
Gaelicat.skills.MartialFlow()
Gaelicat.skills.MartialArts()
Gaelicat.skills.MartialCombat()
Gaelicat.skills.CritRupture()
Gaelicat.jobtype = Monk

# Gighee & Christopher: FFVII
Gighee = AbilityCard(attack=1200, breakPower=30, critStars=3, element=Fire)
Gighee.area = True
Gighee.skills.BreakExploiter()
Gighee.skills.CritRupture()
Gighee.skills.CritWeakness()
Gighee.skills.ElementTap()
Gighee.appliedDebuffs.Crd()
Gighee.appliedBonus.ImprovedCrit(200)
Gighee.jobtype = Monk

# Gilgamesh: fake Duncan
GregCan = AbilityCard(attack=1862, breakPower=413, critStars=1, element=Light)
GregCan.area = False
GregCan.skills.ImbueElement()
GregCan.jobtype = Monk

# Gilgamesh: fake Minwu
GregWu = AbilityCard(attack=1380, breakPower=2, critStars=3, element=Light)
GregWu.area = True
GregWu.skills.BreakExploiter()
GregWu.skills.CritRupture()
GregWu.appliedDebuffs.Unguard()
GregWu.jobtype = Mage

# GreatTortoise
GreatTortoise = AbilityCard(attack=825, breakPower=2100, critStars=1, element=Earth)
GreatTortoise.skills.ImbueElement()
GreatTortoise.skills.CriticalWeakness()
GreatTortoise.skills.ElementTap()
GreatTortoise.appliedBonus.PainfulBreak(200)
GreatTortoise.jobtype = Mage

# Hope: FFXIII
Hope = AbilityCard(attack=900, breakPower=30, critStars=3, element=Light)
Hope.area = False
Hope.skills.BreakExploiter()
Hope.skills.SicariusHunter()
Hope.skills.SicariusKiller()
Hope.skills.ElementTap()
Hope.appliedBonus.PainfulBreak(200)
Hope.jobtype = Mage

# Ignis: FFXV
Ignis = AbilityCard(attack=1800, breakPower=3, critStars=1, element=Fire)
Ignis.area = True
Ignis.skills.BreakExploiter()
Ignis.skills.CritRupture()
Ignis.skills.CritWeakness()
Ignis.skills.ElementTap()
Ignis.jobtype = Mage


# Imp:FFX
Imp = AbilityCard(attack=750, breakPower=750, critStars=3, element=Earth)
Imp.area = True
Imp.skills.BreakerKiller()
Imp.skills.CriticalRupture()
Imp.skills.BloodTap()
Imp.appliedBonus.ExploitWeakness(150)
Imp.appliedBonus.ImprovedCrit(150)
Imp.jobtype = Ranger

# Maelspike: FFX
Maelspike = AbilityCard(attack=750, breakPower=750, critStars=3, element=Water)
Maelspike.area = True
Maelspike.skills.BreakExploiter()
Maelspike.skills.CritRupture()
Maelspike.skills.CritWeakness()
Maelspike.skills.ElementTap()
Maelspike.appliedBonus.ImprovedCrit(150)
Maelspike.appliedBonus.ExploitWeakness(150)
Maelspike.jobtype = Mage

# Nausicaa
Nausicaa = AbilityCard(attack=1650, breakPower=1140, critStars=1, element=Wind)
Nausicaa.area = True
Nausicaa.skills.BreakerKiller()
Nausicaa.skills.CriticalRupture()
Nausicaa.skills.BloodTap()
Nausicaa.jobtype = Ranger

# Myrddin
Myrddin = AbilityCard(attack=1200, breakPower=30, critStars=3, element=Dark)
Myrddin.area = True
Myrddin.skills.BreakExploiter()
Myrddin.skills.CriticalRupture()
Myrddin.skills.CriticalWeakness()
Myrddin.skills.ElementTap()
Myrddin.jobtype = Mage


# Nyx
Nyx = AbilityCard(attack=1650, breakPower=1140, critStars=1, element=Water)
Nyx.area = True
Nyx.skills.MeiaSynchro()
Nyx.skills.BreakExploiter()
Nyx.skills.CriticalWeakness()
Nyx.skills.ElementTap()
Nyx.jobtype = Mage


# Ramuh
Ramuh = AbilityCard(attack=540, breakPower=900, critStars=1, element=Wind)
Ramuh.area = True
Ramuh.skills.BreakExploiter()
Ramuh.skills.Bloodthirst()
Ramuh.skills.BreakerKiller()
Ramuh.appliedDebuffs.Crd()
Ramuh.jobtype = Mage

# Sephiroth: DISSIDIA FF
Sephiroth = AbilityCard(attack=900, breakPower=30, critStars = 3, element=Dark)
Sephiroth.area = True
Sephiroth.skills.Bloodthirst()
Sephiroth.skills.CritRupture()
Sephiroth.skills.VitalityTap()
Sephiroth.jobtype = Warrior

# Soldieress
Soldieress = AbilityCard(attack=1200, breakPower=30, critStars=3, element=Water)
Soldieress.area = True
Soldieress.skills.Bloodthirst()
Soldieress.skills.CritRupture()
Soldieress.skills.VitalityTap()
Soldieress.jobtype = Warrior

# Unbreakable Bonds
UB = AbilityCard(attack=2700, breakPower=3, critStars=1, element=Dark)
UB.skills.Bloodthirst()
UB.skills.CritRupture()
UB.skills.VitalityTap()
UB.skills.BloodTap()
UB.skills.armiger = True
UB.jobtype = Warrior


# Water Gun
WaterGun = AbilityCard(attack=1950, breakPower=6300, critStars=1, element=Wind)
WaterGun.appliedBonus.PainfulBreak(500)
WaterGun.skills.ImbueElement()
WaterGun.skills.MartialCombat()
WaterGun.jobtype = Monk

# Yin & Yang
YinYang = AbilityCard(attack=2400, breakPower=300, critStars=3, element=Earth)
YinYang.area= False
YinYang.skills.ImbueElement()
YinYang.skills.MartialFlow()
YinYang.skills.MartialArts()
YinYang.skills.MartialCombat()
YinYang.jobtype = Monk

