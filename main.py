import pandas as pd
filename = "train.csv"

data = pd.read_csv(filename)

df = pd.DataFrame(data)

# # table
# group_click=pd.DataFrame({'Imps':df.groupby('advertiser')['advertiser'].agg('count'),
#                            'Bids':df.groupby('advertiser')['bidprice'].sum(),
#                            'Cost':df.groupby('advertiser')['payprice'].sum()/1000,
#                            'Clicks':df.groupby('advertiser')['click'].sum(),
#                            'CTR':df.groupby('advertiser')['click'].sum()/df.groupby('advertiser')['advertiser'].agg('count'),
#                            'CPM':df.groupby('advertiser')['payprice'].sum()*1000/(df.groupby('advertiser')['advertiser'].agg('count')*1000),
#                            'eCPC':df.groupby('advertiser')['payprice'].sum()/(df.groupby('advertiser')['click'].sum()*1000)
#                          })
# group_click.to_csv('Table.csv')
#
#
# hours = []
# for hour in df['hour']:
#     if hour not in hours:
#         hours.append(hour)
# hours = sorted(hours)
# #
# advertisers = []
# for advertiser in df['advertiser']:
#     if advertiser not in advertisers:
#         advertisers.append(advertiser)
# advertisers = sorted(advertisers)
# # import csv
# # with open(filename, "r", encoding='utf-8') as table:
# #     r = csv.DictReader(table)
# #     for line in r:
# #         if line['advertiser'] == '2997':
# #             print(line)
# data_advertisers = {}
# for i in advertisers:
#     data_advertisers[i] = []
#     for dt in df.groupby('advertiser'):
#         for adv in dt:
#             print(adv)
#             print(i)
#
# df.insert(1,'os',df['useragent'])
# df['os'] = df["useragent"].map(lambda x:x.split('_')[0])
#
#
# df.insert(1,'size')
# width = df['slotwidth'].astype('str')
# height = df['slotheight'].astype('str')
# size = width.str.cat(height, sep='*')
# df['size']=size
# print(df['size'])
#

#
#
# df.insert(1,'floorprice',df['slotprice'])
# for i in df["slotprice"]:
#     if i in range(1,10):
#         df['floorprice'] = 1
#     elif i in range(11,50):
#         df['floorprice'] = 2
#     elif i in range(51,100):
#         df['floorprice'] = 3
#     elif i == 0:
#         df['floorprice'] = 0
#     else:
#         df['floorprice'] = 4
# print(df['floorprice'])



# df.insert(1,'os',df['useragent'])
oss = []
for name in df["useragent"].map(lambda x:x.split('_')[0]):
    if name not in oss:
        oss.append(name)
data_os = []
for os in df["useragent"].map(lambda x:x.split('_')[0]):
    data_os.append(oss.index(os))
df['os'] = data_os
for i,j in zip(df['os'], df["useragent"]):
    print(i,j)