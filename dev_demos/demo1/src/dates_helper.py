import datetime

def get_dates_in_interval(start_date, end_date):
    result = []
    if start_date is None or end_date is None:
        return
    if start_date == end_date:
        return [start_date]


    # TODO: Solve normal use case
    return result
#write ectual function
def get_dates_in_interval(start_date, end_date):
    if start_date == None:
        return None#redundante
    start =datetime.datetime.strtime(start_date, %m/%d/%y)
    end =datetime.datetime.strtime(start_date, %m/%d/%y)

    if(end-start).days < 0:
        return None
    else:
        date_generated =[start +datetime.timedelta(days=x) for x in range(0, (end-start).days +1)]
        result = []
        for date in date_generated:
            result.append(data.strftime("%m/%d/%y".lstrip('0')))
        return result

def 

if start_date != None or end_date !=None:
    start_date_format_datetime = datetime.strptime(start_date, %m/%d/%Y)
    end_date_format_datetime = datetime.strptime(end_date, %m/%d/%Y)