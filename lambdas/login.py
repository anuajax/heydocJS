import json
import boto3
'''
converts Dynamodb dictionary format to python dictionary format
'''
def dictToJson(d):
    e={}
    for i in d.keys():
        for j in d[i].keys():
            e[i]=d[i][j]
    e['success']=True
    return e
        
'''
handles input request
'''
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    d={"statusCode": 200, "body": "results"}
    event=json.loads(event['body'])
    try:
        a=client.get_item(TableName=event['flag'],Key={
            'username': {'S': event['username'].lower()}
        })
        b=dictToJson(a['Item'])
        if b['username']==event['username'].lower() and b['password']==event['password']:
            d['body']=json.dumps({'success':True})
        else:
            d['body']=json.dumps({'success':False})
    except Exception as e:
            print(e)
            d['body'] =json.dumps({'success':False})
    return d
    