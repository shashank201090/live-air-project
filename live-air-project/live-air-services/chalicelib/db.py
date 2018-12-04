import json
import boto3

from boto3.dynamodb.conditions import Key, Attr
data=[]

with open('./chalicelib/config.json') as json_data_file:
    data = json.load(json_data_file)
    
DYNAMODB = boto3.resource('dynamodb', region_name = data['Region'])

def create(table_name,item_json):
    DYNAMODB.Table(table_name).put_item(Item=item_json)
    return item_json

# will need to search the resource first
def update(table_name,item_json):
    DYNAMODB.Table(table_name).put_item(Item=item_json)
    return item_json

def read_all(table_name, filter_key=None, filter_value=None): 
    table = DYNAMODB.Table(table_name)
    if filter_key and filter_value:
        filtering_exp = Key(filter_key).eq(filter_value)
        response = table.scan(FilterExpression=filtering_exp)
    else:
        response = table.scan()
 
    items = response['Items']
    while True:
        if response.get('LastEvaluatedKey'):
            if filter_key and filter_value:
                response = table.scan(FilterExpression=filtering_exp,ExclusiveStartKey=response['LastEvaluatedKey'])
            else:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        else:
            break
 
    return items

def read(table_name, pk_name, pk_value, sk_name=None,sk_value=None ):
    if sk_name and sk_value:
        lst = []
        lst.append(DYNAMODB.Table(table_name).get_item(Key={pk_name: pk_value,sk_name: sk_value})['Item'])
        return lst
    else:
        lst = []
        lst.append(DYNAMODB.Table(table_name).get_item(Key={pk_name: pk_value})['Item'])
        return lst

            
def delete(table_name, pk_name, pk_value, sk_name=None,sk_value=None ):
    if sk_name and sk_value:
        return  DYNAMODB.Table(table_name).delete_item(Key={pk_name: pk_value,sk_name: sk_value})
    else:
        return  DYNAMODB.Table(table_name).delete_item(Key={pk_name: pk_value})
    