import xlrd

# Columns:
#   0     1       2     3    4     5     6        7         8          9
# lore | type | name | hp | atk | brk | mag | critStar | spdStar | defStar

# 10 11 12 13 14 15 16 17 18 19 20 21   22   23 24 25 26 27 28
# o1|o2|o3|o4|o5|o6| F| W| A| E| L| D| role |fr|wr|ar|er|lr|dr|
#     orb sets     | element enhance |      | ele resist      |

#  29        30       31        32      33      34     35     36        37
# expWeak | painB | iCrit | abChain | pierce | flash | qb | scourge | sguard

def loadSheet(filename = ""):
    """ Load job data from Excel spreadsheet """
    if filename == "": filename = "jobstats.xlsx"
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    # 2 header rows
    jobData = []
    jobData.append(sheet.row_values(0))
    jobData.append(sheet.row_values(1))

    # set null values to 0 for numerical parameters
    for ii in range(2,sheet.nrows):
        row = sheet.row_values(ii)
        for jj in range(7,10): 
            if (row[jj] == ''): row[jj]=0  # crit/spd/def stars
        for jj in range(16,22): 
            if (row[jj] == ''): row[jj]=0  # element enhance
        for jj in range(22,38): 
            if (row[jj] == ''): row[jj]=0  # resist & abilities

        jobData.append(row)

    return jobData
