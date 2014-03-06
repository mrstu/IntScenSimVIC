#!/usr/bin/env python

import glob, os
import argparse

def parse_vss(line):
    '''Parser for calendar/variable/stat/stat-of-stat table (table_cal_var_stat_stats.txt)'''
    parts = line.split()     
    return tblvar, parts[1], 

def parseargs():
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(description='Compute statistics for monthly files containing daily records')

    parser.add_argument("-t", "--table",
                      dest="table", default="table_cal_var_stat_stats.txt", help='Flat file containing rows like: <var> <stat> <<stats-of-stat>>')
    parser.add_argument("-c", "--command",
                      dest="cmd", default="ncra -O -y", nargs="+", help='Command that takes xinput files and produces 1 output file')
    parser.add_argument("-var", "--variable",
                      dest="vname", default="tasmax", help='Name of variable to process')
    parser.add_argument("-d", "--input_directory",
                      dest="indir", default="splitmon.stats/tasmax/rcp45/CanESM2", help='Input directory')
    parser.add_argument("-o", "--output_directory",
                  dest="outdir", default="splitmon.stats/tasmax/rcp45/CanESM2", help='Output directory')
    parser.add_argument("-v", "--verbose",
                      action="store_true", default=None)

    args = parser.parse_args()
    
    return args
    

def main():
   
#     rcp="rcp45"
#     gcm="CanESM2"
#     var='tasmax'
#     
#     basedir='splitmon.stats/%s/%s'%(rcp,gcm)
#     mondir='%s/%s'%(basedir,var)
#     outdir=mondir.replace('splitmon.stats','calmon.stats')
#     cmd='ncra -O -y'
#     filename= 'table_cal_var_stat_stats.txt'
    args = parseargs()
    
    filename=args.table
    mondir=args.indir
    outdir=args.outdir
    cmd=args.cmd
    var=args.vname
    
    with open(filename) as f_in:
        lines = filter(None, (line.rstrip() for line in f_in))
    
    try:
        os.makedirs(outdir)
    except OSError:
        pass
    
    # cdo/nco conventions are slightly different
    # stddev in nco is more involved
    mapcmds = {'mean':'avg', 'std1':None}

    statdb={}
    for line in lines:
        parts = line.split()
        tblvar = parts[0]
        tblstat= parts[1]
        tblsstats= parts[2:]        
    #     statdb[tblvar]=
    #     print 'stat1:', parts[1]    
    #     print 'stats:', ' '.join(parts[2:])
        if tblvar == var:
    #         print 'var:', tblvar
    #         print 'stat1:', parts[1]    
    #         print 'stats:', ' '.join(parts[2:])
            files=glob.glob(mondir+"/*_"+tblstat)
            files.sort()
            # poor man's WY accounting (exclude Jan-Sept first year, OND of last year)
            files=files[9:-3] 
            for mon in range(1,13):
                monpad=str(mon).zfill(2)
                flist=[]
                for ff in files:
                    ffs = ff.split('/')
                    # from filename get month string
                    if ffs[-1][5:7]==monpad:
                        flist.append(ff)
    #                 else:
    #                     print ff[5:7], monpad, ff[:5]
                for ss in tblsstats:
                    if mapcmds.has_key(ss):
                        ss = mapcmds[ss]
                    if ss:
                        ofile=os.path.join(outdir, "_".join([monpad, tblstat, ss]))
                        print ' '.join(cmd), ss, ' '.join(flist), ofile+'.nc'
                        
if __name__=='__main__':
    main()