import pandas as pd


def get_drone_sensors_data():
    path = input("Write the path to the .csv file\n")

    data = pd.read_csv(path, usecols=[
                       'CUSTOM.date [local]', ' CUSTOM.updateTime [local]', ' OSD.latitude', ' OSD.longitude', ' OSD.height [ft]', ' OSD.altitude [ft]'], header=1)

    dates = data['CUSTOM.date [local]'].head(-1)
    hours = data[' CUSTOM.updateTime [local]'].head(-1)
    lat = data[' OSD.latitude'].head(-1)
    lon = data[' OSD.longitude'].head(-1)
    hei = data[' OSD.height [ft]'].head(-1)
    alt = data[' OSD.altitude [ft]'].head(-1)

    new_data = {'Date': format_date(
        dates, hours), 'Lat': lat, 'Lon': lon, 'Hei[ft]': hei, 'Alt[ft]': alt}

    data_frame = pd.DataFrame(new_data)
    
    return data_frame


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
    
    return f'{to_24_format(time)}:{int(items[1]):02}:{int(items[2].split(".")[0]):02}'

def to_24_format(time):
    is_pm = time.find('PM')
    formated_hour = f'{int(time[0]):02}'

    new_hour = ''
    if is_pm:
        new_hour = int(formated_hour) + 12
        new_hour = 00 if new_hour == 24 else new_hour
    else:
        new_hour = formated_hour
        
    return new_hour