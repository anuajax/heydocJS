import json
import boto3
def dictToJson(d):
    e={}
    for i in d.keys():
        for j in d[i].keys():
            e[i]=d[i][j]
    e['success']=True
    return e
    
def space(a):
    a=list(a)
    while a and a[-1]==' ':
        a.pop()
    a=a[::-1]
    while a and a[-1]==' ':
        a.pop()
    a=a[::-1]
    
    return ''.join(a)
    
        

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    d={"statusCode": 200, "body": "results"}
    if event['httpMethod']=='GET':
        event=event['queryStringParameters']
        try:
            a=client.get_item(TableName='doc',Key={
                'username': {'S': str(event['doc'])}
            })
            b=client.get_item(TableName='pat',Key={
                'username': {'S': str(event['pat'])}
            })
            a=dictToJson(a['Item'])
            b=dictToJson(b['Item'])
            us=a['username']+'#'+b['username']
            oa=a['pending'][us]
            ob=b['pending'][us]
            a['approved'][us]=oa
            b['approved'][us]=ob
            database = boto3.resource('dynamodb')
            table = database.Table('doc')
            response = table.update_item(
                    Key={
                        'username': a['username']
                        
                    },
                    UpdateExpression="SET approved.#us = :oa",
                    ExpressionAttributeNames = { "#us" : us},
                    ExpressionAttributeValues={
                        ':oa': event,
                    },
                    ReturnValues="UPDATED_NEW"
                    )
            response = table.update_item(
                Key={
                    'username': a['username']
                    
                },
                UpdateExpression="REMOVE pending.#us",
                ExpressionAttributeNames = { "#us" : us},
                ReturnValues="UPDATED_NEW"
                )
            table = database.Table('pat')
            response = table.update_item(
                    Key={
                        'username': b['username']
                        
                    },
                    UpdateExpression="SET approved.#us = :oa",
                    ExpressionAttributeNames = { "#us" : us},
                    ExpressionAttributeValues={
                        ':oa': event,
                    },
                    ReturnValues="UPDATED_NEW"
                    )
            response = table.update_item(
                Key={
                    'username': b['username']
                    
                },
                UpdateExpression="REMOVE pending.#us",
                ExpressionAttributeNames = { "#us" : us},
                ReturnValues="UPDATED_NEW"
                )
            d['body']=json.dumps({'result':'Success'})
        except Exception as e:
            print(e)
            d['body'] =json.dumps({'result':'Error'})
            return d
    elif event['httpMethod']=='POST':
        event=json.loads(event['body'])
        try:
            a=client.get_item(TableName='doc',Key={
                'username': {'S': event['doc']}
            })
            b=client.get_item(TableName='pat',Key={
                'username': {'S': event['pat']}
            })
            us=event['doc']+'#'+event['pat']
            a=dictToJson(a['Item'])
            b=dictToJson(b['Item'])
            if us not in a['pending'].keys() and us not in b['pending'].keys() and us not in a['approved'].keys() and us not in b['approved'].keys():
                database = boto3.resource('dynamodb')
                table = database.Table('doc')
                response = table.update_item(
                    Key={
                        'username': a['username']
                        
                    },
                    UpdateExpression="SET pending.#us = :oa",
                    ExpressionAttributeNames = { "#us" : us},
                    ExpressionAttributeValues={
                        ':oa': event,
                    },
                    ReturnValues="UPDATED_NEW"
                    )
                table = database.Table('pat')
                response = table.update_item(
                    Key={
                        'username': b['username']
                        
                    },
                    UpdateExpression="SET pending.#us = :oa",
                    ExpressionAttributeNames = { "#us" : us},
                    ExpressionAttributeValues={
                        ':oa': event,
                    },
                    ReturnValues="UPDATED_NEW"
                    )
                
                
                d['body']=json.dumps({'result':'Success'})
            else:
                d['body']=json.dumps({'result':'Appointment already exists'})
                return d
        except Exception as e:
            print(e)
            d['body']=json.dumps({'result':'Unidentified Error'})
            return d
    else:
        event=json.loads(event['body'])
        try:
            a=client.get_item(TableName='doc',Key={
                'username': {'S': event['doc']}
            })
            b=client.get_item(TableName='pat',Key={
                'username': {'S': event['pat']}
            })
            us=event['doc']+'#'+event['pat']
            a=dictToJson(a['Item'])
            b=dictToJson(b['Item'])
            if us not in a['pending'].keys() and us not in b['pending'].keys() and us in a['approved'].keys() and us in b['approved'].keys():
                database = boto3.resource('dynamodb')
                table = database.Table('doc')
                response = table.update_item(
                        Key={
                            'username': a['username']
                            
                        },
                        UpdateExpression="SET previous = list_append(previous, :oa)",
                        ExpressionAttributeValues={
                            ':oa': [event],
                        },
                        ReturnValues="UPDATED_NEW"
                        )
                response = table.update_item(
                    Key={
                        'username': a['username']
                        
                    },
                    UpdateExpression="REMOVE approved.#us",
                    ExpressionAttributeNames = { "#us" : us},
                    ReturnValues="UPDATED_NEW"
                    )
                table = database.Table('pat')
                response = table.update_item(
                        Key={
                            'username': b['username']
                            
                        },
                        UpdateExpression="SET previous = list_append(previous, :oa)",
                        ExpressionAttributeValues={
                            ':oa': [event],
                        },
                        ReturnValues="UPDATED_NEW"
                        )
                response = table.update_item(
                    Key={
                        'username': b['username']
                        
                    },
                    UpdateExpression="REMOVE approved.#us",
                    ExpressionAttributeNames = { "#us" : us},
                    ReturnValues="UPDATED_NEW"
                    )
                d['body']=json.dumps({'result':'Success'})
            else:
                d['body']=json.dumps({'result':'Invalid Appointment'})
                return d
        except Exception as e:
            print(e)
            d['body']=json.dumps({'result':'Unidentified Error'})
            return d
    e={}
    a=client.get_item(TableName='doc',Key={'username': {'S': str(event['doc'])}})
    b=client.get_item(TableName='pat',Key={'username': {'S': str(event['pat'])}})
    e['result']='success'
    x=dictToJson(a['Item'])
    y=dictToJson(b['Item'])
    z=[]
    for i in x['previous']:
        z.append(dictToJson(i['M']))
    x['previous']=z
    z=[]
    for i in x['pending'].keys():
        z.append(dictToJson(x['pending'][i]['M']))
    x['pending']=z
    z=[]
    for i in x['approved'].keys():
        z.append(dictToJson(x['approved'][i]['M']))
    x['approved']=z
    z=[]
    for i in y['previous']:
        z.append(dictToJson(i['M']))
    y['previous']=z
    z=[]
    for i in y['pending'].keys():
        z.append(dictToJson(y['pending'][i]['M']))
    y['pending']=z
    z=[]
    for i in y['approved'].keys():
        z.append(dictToJson(y['approved'][i]['M']))
    y['approved']=z
    e['pat']=y
    e['doc']=x
    d['body']=json.dumps(e)
    print(d)
    return d