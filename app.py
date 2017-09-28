import geocoder

dat = geocoder.geocodefarm('Cuautitlan Izcalli')

print(str(dat.latlng))

dat = geocoder.reverse(dat.latlng)

print(dat.address) #Direccion
print(dat.country) #país
print(dat.state) #estado
print(dat.county) #Municipio
print(dat.street) #Calle