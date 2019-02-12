

def wpntime(hp, atk, brk, magic, nMods):

    stats = [int(hp/10), atk, brk, magic]
    hours = range(1,101)
    totHours = 0

    for ii in range(nMods):
        stats = sorted(stats)

        if stats[0] < 200:
            # Need 6 increases in stat values
            for jj in range(6):
                # hours to go from (stat) to (stat+2) = 1 + (stat/2)
                totHours = totHours + hours[int(stats[0]/2)];
                stats[0] = stats[0] + 2;
                stats = sorted(stats);
                if stats[0] == 200: break
            # 24 hours for the mod itself
            totHours = totHours + 24
            print(stats)
        else:
            totHours = totHours + 24


    print(stats)
    print('Days: %.1f\n' % (totHours/24))
    return(totHours)





