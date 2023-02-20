import pandas as pd
import kabbes_nanoid

#100 customers - 
#150 addresses - effective
#1000 orders -customer id
import datetime
import numpy as np

start_datetime = datetime.datetime( 2000, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc) 
end_datetime = datetime.datetime( 2020, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc) 
max_datetime = datetime.datetime.max
max_datetime = max_datetime.replace(tzinfo=datetime.timezone.utc)
delta_datetime = end_datetime - start_datetime
dt_format = '%Y-%m-%d'

# customers
customers = list(range(1,101))
df_customers = pd.DataFrame( {"customerID": customers } )
df_customers['nanoid'] = [ kabbes_nanoid.generate() for i in range(len(df_customers)) ]

# orders
orders = list(range(1,1001))
order_times_prop = np.random.rand(1000)
order_times = delta_datetime*order_times_prop + start_datetime
order_times = [ order_time.strftime(dt_format) for order_time in order_times ]

df_orders = pd.DataFrame( {"orderID": orders} )
df_orders['datetime'] = order_times
df_orders['customerID'] = [ np.random.choice( df_customers['customerID'] ) for i in range(len(df_orders))]

# addresses
min_addresses = 1
max_addresses = 4

addressIDS = []
customerIDS = []
dt_effs = []
dt_ends = []

counter = 1
for customerID in df_customers['customerID']:
    n_addresses = np.random.choice( list(range(min_addresses, max_addresses+1)) )

    dts = [ start_datetime, max_datetime ] 

    eff_times_prop = np.random.rand( n_addresses-1 )
    eff_times_prop.sort()
    eff_times = delta_datetime*eff_times_prop + start_datetime

    for eff_time in eff_times:
        dts.insert( -1, eff_time )

    for i in range(len(dts)-1):
        customerIDS.append( customerID )
        addressIDS.append( counter )
        dt_effs.append( dts[i].strftime( dt_format ) )
        dt_ends.append( dts[i+1].strftime( dt_format) )
        counter += 1

df_addresses = pd.DataFrame({
    "addressID": addressIDS,
    "customerID": customerIDS,
    "dt_eff": dt_effs,
    "dt_ends": dt_ends
})

df_addresses['zip_code'] = [ np.random.choice( list(range(10000,100000)) ) for i in range(len(df_addresses)) ]

print (df_customers)
print (df_addresses)
print (df_orders)

df_customers.to_csv( '../prompts/4/customers.csv', index=False )
df_addresses.to_csv( '../prompts/4/addresses.csv', index=False )
df_orders.to_csv( '../prompts/4/orders.csv', index=False )
