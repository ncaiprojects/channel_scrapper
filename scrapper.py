# Channel Schedule Scrapper
# ==========================

# %%
# Importing Libraries
from http import client
import requests
from bs4 import BeautifulSoup
import datetime as dt
import pymongo

# %%
# Available Channel List
mongo_ip = '172.17.0.2'
mongo_port = 27017

channels = {
    'GEO': 'https://www.geo.tv/schedule',
    'ARY': 'https://www.ontvtonight.com/guide/listings/channel/295630272/ary-news.html',
    'DUNYA': 'https://www.ontvtonight.com/guide/listings/channel/3739649474/dunya-tv-usa.html',
    'EXPRESS': 'https://www.ontvtonight.com/guide/listings/channel/69044276/express-news.html',
    'AAJ': 'https://www.ontvtonight.com/guide/listings/channel/3641874346/aaj-entertainment.html',
    'CHANNEL24': 'https://www.ontvtonight.com/guide/listings/channel/1174443204/channel-24.html'

}

schedule_store = {l: {'time': list(), 'label': list()} for l in list(channels.keys())}
upstream_schedule = {l: list() for l in list(channels.keys())}
date_today = dt.datetime.now()

# %%
# Scrap GEO News Schedule
print('>>>>>>>>>> Scrapping GEO News')
resp = requests.get(channels['GEO'])

soup_month = BeautifulSoup(resp.text, features='lxml')
res = soup_month.find('div', class_='month')

soup_times = BeautifulSoup(resp.text, features='lxml')
res = soup_times.find_all('span', class_='timeslot')

for time in res:
    schedule_store['GEO']['time'].append(time.get_text())

soup_names = BeautifulSoup(resp.text, features='lxml')
res = soup_names.find_all('span', class_='schudule_status')

for name in res:
    schedule_store['GEO']['label'].append(name.get_text())


# %%
# Scrap ARY News Schedule
print('>>>>>>>>>> Scrapping ARY News')
resp2 = requests.get(channels['ARY'])

soup_times = BeautifulSoup(resp2.content, features='lxml')
res2 = soup_times.find_all('h5', class_='thin')

i = 0
for content in res2:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
        i += 1
        continue
    if i%2 == 0:
        get_st = content_text.split(' ')[1]
        get_h = int(content_text.split(' ')[0].split(':')[0])
        get_m = content_text.split(' ')[0].split(':')[1]
        if get_st == 'pm':
            new_time = str(get_h + 12).zfill(2) + ':' + get_m
        else:
            if get_h >= 12:
                new_time = str(get_h - 12).zfill(2) + ':' + get_m
            else:
                new_time = str(get_h).zfill(2) + ':' + get_m
        schedule_store['ARY']['time'].append(new_time)
    else:
        schedule_store['ARY']['label'].append(content_text)
    i += 1

# %%
# Scrap DUNYA News Schedule
print('>>>>>>>>>> Scrapping DUNYA News')
resp3 = requests.get(channels['DUNYA'])

soup_times = BeautifulSoup(resp3.content, features='lxml')
res3 = soup_times.find_all('h5', class_='thin')

i = 0
for content in res3:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
        i += 1
        continue
    if i%2 == 0:
        get_st = content_text.split(' ')[1]
        get_h = int(content_text.split(' ')[0].split(':')[0])
        get_m = content_text.split(' ')[0].split(':')[1]
        if get_st == 'pm':
            new_time = str(get_h + 12).zfill(2) + ':' + get_m
        else:
            if get_h >= 12:
                new_time = str(get_h - 12).zfill(2) + ':' + get_m
            else:
                new_time = str(get_h).zfill(2) + ':' + get_m
        schedule_store['DUNYA']['time'].append(new_time)
    else:
        schedule_store['DUNYA']['label'].append(content_text)
    i += 1

# %%
# Scrap EXPRESS News Schedule
print('>>>>>>>>>> Scrapping EXPRESS News')
resp4 = requests.get(channels['EXPRESS'])

soup_times = BeautifulSoup(resp4.content, features='lxml')
res4 = soup_times.find_all('h5', class_='thin')

i = 0
for content in res4:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
        i += 1
        continue
    if i%2 == 0:
        get_st = content_text.split(' ')[1]
        get_h = int(content_text.split(' ')[0].split(':')[0])
        get_m = content_text.split(' ')[0].split(':')[1]
        if get_st == 'pm':
            new_time = str(get_h + 12).zfill(2) + ':' + get_m
        else:
            if get_h >= 12:
                new_time = str(get_h - 12).zfill(2) + ':' + get_m
            else:
                new_time = str(get_h).zfill(2) + ':' + get_m
        schedule_store['EXPRESS']['time'].append(new_time)
    else:
        schedule_store['EXPRESS']['label'].append(content_text)
    i += 1

# %%
# Scrap AAJ News Schedule
print('>>>>>>>>>> Scrapping AAJ News')
resp5 = requests.get(channels['AAJ'])

soup_times = BeautifulSoup(resp5.content, features='lxml')
res5 = soup_times.find_all('h5', class_='thin')

i = 0
for content in res4:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
        i += 1
        continue
    if i%2 == 0:
        get_st = content_text.split(' ')[1]
        get_h = int(content_text.split(' ')[0].split(':')[0])
        get_m = content_text.split(' ')[0].split(':')[1]
        if get_st == 'pm':
            new_time = str(get_h + 12).zfill(2) + ':' + get_m
        else:
            if get_h >= 12:
                new_time = str(get_h - 12).zfill(2) + ':' + get_m
            else:
                new_time = str(get_h).zfill(2) + ':' + get_m
        schedule_store['AAJ']['time'].append(new_time)
    else:
        schedule_store['AAJ']['label'].append(content_text)
    i += 1

# %%
# Scrap CHANNEL24 News Schedule
print('>>>>>>>>>> Scrapping CHANNEL24 News')
resp6 = requests.get(channels['CHANNEL24'])

soup_times = BeautifulSoup(resp6.content, features='lxml')
res6 = soup_times.find_all('h5', class_='thin')

i = 0
for content in res6:
    content_text = content.get_text().strip()
    if "More channels at the American TV Listings Guide.." in content_text or i == 0 or i == 1:
        i += 1
        continue
    if i%2 == 0:
        get_st = content_text.split(' ')[1]
        get_h = int(content_text.split(' ')[0].split(':')[0])
        get_m = content_text.split(' ')[0].split(':')[1]
        if get_st == 'pm':
            new_time = str(get_h + 12).zfill(2) + ':' + get_m
        else:
            if get_h >= 12:
                new_time = str(get_h - 12).zfill(2) + ':' + get_m
            else:
                new_time = str(get_h).zfill(2) + ':' + get_m
        schedule_store['CHANNEL24']['time'].append(new_time)
    else:
        schedule_store['CHANNEL24']['label'].append(content_text)
    i += 1

# %%
# Create Upstream Data
for i in list(upstream_schedule.keys()):
    for t, s in zip(schedule_store[i]['time'], schedule_store[i]['label']):
        upstream_schedule[i].append({
            'year': date_today.year,
            'month': date_today.month,
            'day': date_today.day,
            'time': t,
            'show': s
        })

# %%
# Mongo Connection
client = pymongo.MongoClient(mongo_ip, mongo_port)
db = client['schedule_scrap']

for j in list(upstream_schedule.keys()):
    if len(upstream_schedule[j])!=0:
        col = db[j]
        col.insert_many(upstream_schedule[j])
