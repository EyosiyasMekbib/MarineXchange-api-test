from zeep import Client

# Step 1: Import web service interface using the WSDL import wizard
wsdl_url = 'http://test.mymxp.com/cgi-bin/MarineXchangeEComWebService2.exe/wsdl/IMarineXchangeECommerce'
client = Client(wsdl=wsdl_url)

# Step 2: Declare iWS variable of type IMarineXchangeECommerce
iWS = client

# Step 3: Call the iWS.ServiceCheck method to check the service availability
result = iWS.service.ServiceCheck()

# Check the availability status
if result == 'OK':
    print("Service is available.")
else:
    print("Service is not available.")

# Step 4: Code snippet to retrieve units of measure
units_of_measure = iWS.service.GetUnitsOfMeasure()

# Print the retrieved units of measure
for unit in units_of_measure:
    print(unit)

# Now you can continue with the rest of your script using the iWS variable

