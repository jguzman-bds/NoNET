import adodbapi

# Connection string
conn = adodbapi.connect("Provider=MSOLAP.8; \
    Data Source='powerbi://api.powerbi.com/v1.0/myorg/ModelosMayores1GB'; \
    Initial Catalog='SatisfactionReport'")

# Example query
print('The tables in your database are:')
for name in conn.get_table_names():
    print(name)
