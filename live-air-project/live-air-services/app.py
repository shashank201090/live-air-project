import json
import boto3

from chalice import Chalice
from chalicelib.db import * 

app = Chalice(app_name='live-air')
app.debug = True

# Create Tenant
@app.route('/tenants', methods=['POST'],cors=True)
def create_tenant():    
    return create('Tenant',app.current_request.json_body)

# Get All Tenants
@app.route('/tenants', methods=['GET'],cors=True)
def read_tenants():
    return read_all('Tenant',None,None)

# Create Order
@app.route('/tenants/{tenant_id}/orders', methods=['POST'],cors=True)
def create_order(tenant_id):
    return create('OrderInfo',app.current_request.json_body)

# Update Order
@app.route('/tenants/{tenant_id}/orders/{order_id}', methods=['PUT'],cors=True)
def update_order(tenant_id,order_id):
    return update('OrderInfo',app.current_request.json_body)

# Get Order
@app.route('/tenants/{tenant_id}/orders/{order_id}', methods=['GET'],cors=True)
def get_order(tenant_id,order_id):
    if order_id =='':
        return read_all('OrderInfo','TenantID',int(tenant_id))
    else:
        return read('OrderInfo','OrderID',order_id,'TenantID',int(tenant_id))

#Delete Order
@app.route('/tenants/{tenant_id}/orders/{order_id}', methods=['DELETE'],cors=True)
def del_order(tenant_id,order_id):
    return delete('OrderInfo','OrderID',order_id,'TenantID',int(tenant_id))

# Get All Orders
@app.route('/tenants/{tenant_id}/orders', methods=['GET'],cors=True)
def get_orders(tenant_id):
    return read_all('OrderInfo','TenantID',int(tenant_id))

# Get All Events
@app.route('/tenants/{tenant_id}/orders/{order_id}/events', methods=['GET'],cors=True)
def get_events(tenant_id, order_id):
    return read_all('Events','OrderID',order_id)

# Get Event
@app.route('tenants/{tenant_id}/orders/{order_id}/events/{event_id}', methods=['POST'],cors=True)
def get_event():
    return read_all('Events','EventId',event_id,'OrderID',order_id)

#Create Event
@app.route('/tenants/orders/{order_id}', methods=['POST'],cors=True)
def create_event(order_id):
    return create('Events',app.current_request.json_body)

#DynamoDB Trigger
@app.lambda_function()
def OrderInfo_Trigger(event, context):
    client = boto3.client('sns')
    print("This lambda function Triggered")
    print(event['Records'][0]['dynamodb']['NewImage'])
    return {}