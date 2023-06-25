from zeep import Client

wsdl_url = 'http://test.mymxp.com/cgi-bin/MarineXchangeEComWebService2.exe/wsdl/IMarineXchangeECommerce'
client = Client(wsdl=wsdl_url)

iWS = client

po_login_code = 'CDCA743BC3314EFBA11C128F9992C66A'
user_full_name = 'Bekele'
po_header = iWS.service.GetPOHeader(po_login_code, user_full_name)

print("PO Header:")
print(po_header)

po_details = iWS.service.GetPODetails(po_login_code)

print("\nPO Details:")
for detail in po_details:
    print(detail)

contact_guid = 'your_contact_guid'
mxp_client_id = 24 
external_shipment_id = 4  

shipment = iWS.service.GetShipment(contact_guid, mxp_client_id, external_shipment_id)

print("\nShipment:")
print(shipment)
