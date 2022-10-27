import pandas as pd


def get_drone_sensors_data(csv_path):
    data = pd.read_csv(csv_path, usecols=[
                       'CUSTOM.date [local]', ' CUSTOM.updateTime [local]', ' OSD.latitude', ' OSD.longitude', ' OSD.height [ft]', ' OSD.altitude [ft]'], header=1)
    
    pd.set_option('display.max_rows', None)

    dates = data['CUSTOM.date [local]']
    hours = data[' CUSTOM.updateTime [local]']
    lat = data[' OSD.latitude']
    lon = data[' OSD.longitude']
    hei = data[' OSD.height [ft]']
    alt = data[' OSD.altitude [ft]']

    new_data = {'Date': format_date(
        dates, hours), 'Lat': lat, 'Lon': lon, 'Hei[ft]': hei, 'Alt[ft]': alt}
    
    return pd.DataFrame(new_data)


def format_date(dates, hours):
    new_dates = map(replace_slash_by_middle_dash, dates)
    new_hours = map(format_time, hours)
    return list(map(lambda date, time: f'{date} {time}', new_dates, new_hours))


def replace_slash_by_middle_dash(date):
    items = date.split('/')
    new_dates = '-'.join(list(map(lambda item: f'{int(item):02}', items)))

    return new_dates


def format_time(time):
    items = time.split(':')
    return f'{to_24_format(items):02}:{int(items[1]):02}:{int(items[2].split(".")[0]):02}'

def to_24_format(time_items):
    is_pm = time_items[2].find('PM') != -1
    hour = int(time_items[0])
    new_hour = ''
    
    if is_pm :
        new_hour = hour + 12
        new_hour = 00 if new_hour == 24 else new_hour
    else:
        new_hour = hour
        
    return new_hour
