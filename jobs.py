import xlrd
#import csv
from dmgcalc import *
import pdb
import re


# Columns:
#   0     1       2     3    4     5     6        7         8          9
# lore | type | name | hp | atk | brk | mag | critStar | spdStar | defStar

# 10 11 12 13 14 15 16 17 18 19 20 21   22   23 24 25 26 27 28
# o1|o2|o3|o4|o5|o6| F| W| A| E| L| D| role |fr|wr|ar|er|lr|dr|
#     orb sets     | element enhance |      | ele resist      |

#  29        30       31        32      33      34     35     36        37
# expWeak | painB | iCrit | abChain | pierce | flash | qb | scourge | sguard

def loadJobs(filename = ""):
    """ Load job list from spreadsheet """
    if filename == "": filename = "jobstats.xlsx"
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    jobList = []
    for ii in range(2,sheet.nrows):
        row = sheet.row_values(ii) 
        name = row[2]; 
        [atk,brk,mag, critStar] = row[4:8]
        if critStar == '': critStar = 0
        lbreak = (row[40] == 1)
        job = Job(name, atk, mag, brk, critStar, lbreak)

        joblore = []
        jobtype = row[1]
        job.isMeia = ("Meia" in jobtype)
        if "Warrior" in jobtype or "Graff" in jobtype: joblore = [Warrior]
        if "Mage" in jobtype or "Meia" in jobtype: joblore = [Mage]
        if "Ranger" in jobtype or "Sarah" in jobtype: joblore = [Ranger]
        if "Monk" in jobtype or "Sophie" in jobtype: lore = [Monk]

        lore = row[0]
        if "Mage" in lore: joblore.append(Mage)
        if "Ranger" in lore: joblore.append(Ranger)
        if "Monk" in lore: joblore.append(Monk)
        job.lore = joblore

        job.type = jobtype
        orbs = "".join(row[10:16])
        job.elements[Fire]  = 'F' in orbs
        job.elements[Water] = 'W' in orbs
        job.elements[Wind]  = 'A' in orbs
        job.elements[Earth] = 'E' in orbs
        job.elements[Dark]  = 'D' in orbs
        job.elements[Light] = 'L' in orbs
        
        for jj in range(16,22): 
            if (row[jj] == ''): row[jj]=0
        for jj in range(29,38): 
            if (row[jj] == ''): row[jj]=0
        job.abilities.EnhanceFire(row[16])
        job.abilities.EnhanceWater(row[17])
        job.abilities.EnhanceWind(row[18])
        job.abilities.EnhanceEarth(row[19])
        job.abilities.EnhanceLight(row[20])
        job.abilities.EnhanceDark(row[21])

        job.abilities.ExploitWeakness(row[29])
        job.abilities.PainfulBreak(row[30])
        job.abilities.ImprovedCrit(row[31])
        job.abilities.AbilityChain(row[32])

        jobList.append(job)
        #pdb.set_trace()

    return jobList

def findJob(joblist, nameExpr):
    """ Find the first job that matches name. """
    # nameExpr can be a regular expression 
    job = []
    for ijob in joblist:
        if re.search(nameExpr, ijob.name):
            job = ijob
            break

    if job == []:
        # try again, but this time ignore case
        for ijob in joblist:
            if re.search(nameExpr, ijob.name, re.IGNORECASE):
                job = ijob
                break

    return job

#joblist = loadJobs()
