import csv

# Columns:
#   0     1       2     3    4     5     6        7         8          9
# lore | type | name | hp | atk | brk | mag | critStar | spdStar | defStar

# 10 11 12 13 14 15 16 17 18 19 20 21   22   23 24 25 26 27 28
# o1|o2|o3|o4|o5|o6| F| W| A| E| L| D| role |fr|wr|ar|er|lr|dr|
#     orb sets     | element enhance |      | ele resist      |

#  29        30       31        32      33      34     35     36        37
# expWeak | painB | iCrit | abChain | pierce | flash | qb | scourge | sguard

def loadSheet(filename = ""):
    """ Load job data from CSV spreadsheet """
    if filename == "": filename = "jobstats.csv"
    with open(filename, 'r') as f:
        rdr = csv.reader(f)
        jobData = list(rdr)

    # csv loads everything as strings: convert to int
    for ii in range(2,len(jobData)):
        for jj in range(7,10): 
            if (jobData[ii][jj] == ''): jobData[ii][jj]=0  # crit/spd/def stars
        for jj in range(16,22): 
            if (jobData[ii][jj] == ''): jobData[ii][jj]=0  # element enhance
        for jj in range(22,41): 
            if (jobData[ii][jj] == ''): jobData[ii][jj]=0  # resist & abilities

        jobData[ii][3:10] = [int(x) for x in jobData[ii][3:10]]
        jobData[ii][16:22] = [int(x) for x in jobData[ii][16:22]]
        jobData[ii][23:41] = [int(x) for x in jobData[ii][23:41]]

    return jobData
