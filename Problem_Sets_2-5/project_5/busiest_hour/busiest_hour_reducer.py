import sys

def reducer():
    '''
    For every single unit, write a reducer that will return the busiest datetime (e.g.,
    the entry that had the most entries).  Ties should go to datetimes that are later on in the 
    Month of May.  You can assume that the contents of the reducer will be sorted by UNIT, such that
    all entries corresponding to a given UNIT will be sorted together. The output should be the UNIT
    name, the datetime (which is a concatenation of date and time), and ridership separated by tabs.

    For example, the output of the reducer may look like this:
    R001    2011-05-11 17:00:00    31213.0
    R002    2011-05-12 21:00:00    4295.0
    R003    2011-05-05 12:00:00    995.0
    R004    2011-05-12 12:00:00    2318.0
    R005    2011-05-10 12:00:00    2705.0
    R006    2011-05-25 12:00:00    2784.0
    R007    2011-05-10 12:00:00    1763.0
    R008    2011-05-12 12:00:00    1724.0
    R009    2011-05-05 12:00:00    1230.0
    R010    2011-05-09 18:00:00    30916.0
    
    unit, the ENTRIESn_hourly, the DATEn, and TIMEn
    
    ...
    ...
    
    '''

    max_entries = 0
    old_unit = None
    datetime = ''

    # your code here
    for line in sys.stdin:
        # your code here
        data = line.strip().split("\t")
        
        if len(data) != 4:
            continue
        else:
            this_unit, entries, daten, timen = data
            
#        if old_unit and old_unit != this key:
        if old_unit and old_unit != this_unit: # new unit            
            print "{0}\t{1}\t{2}".format(old_unit, datetime , max_entries) #print old unit details
            max_entries = 0
            datetime = ''            
            
        old_unit = this_unit
        
        if max_entries <= float(entries):
            max_entries = float(entries)
            datetime = daten+' '+timen
        else:
            continue
      
    if old_unit != None:
        print "{0}\t{1}\t{2}".format(old_unit, datetime, max_entries)
        
reducer()
