import json
import boto3
import jwt

'''
converts Dynamodb dictionary format to python dictionary format
'''
def dictToPy(d):
    e={}
    for i in d.keys():
        for j in d[i].keys():
            e[i]=d[i][j]
    e['success']=True
    return e

'''
removes extra spaces
'''    
def space(a):
    a=list(a)
    while a and a[-1]==' ':
        a.pop()
    a=a[::-1]
    while a and a[-1]==' ':
        a.pop()
    a=a[::-1]
    
    return ''.join(a)
    
        
'''
handles input request
'''
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    d={"statusCode": 200, "body": "results"}
    if event['httpMethod']=='GET':
        try:
            a=client.get_item(TableName=event['queryStringParameters']['flag'],Key={
                'username': {'S': str(event['queryStringParameters']['username'])}
            })
            print(a)
            b=dictToJson(a['Item'])
            d['body']=(json.dumps(b))
        except Exception as e:
            print(e)
            d['body'] =json.dumps({'success':False})
    else:
        event=json.loads(event['body'])
        try:
            a=client.get_item(TableName=event['flag'],Key={
                'username': {'S': event['username']}
            })
            if a['Item']:
                d['body']=json.dumps({'success':False})
        except Exception as e:
            print(e)
            if event['flag']=='doc':
                enc=jwt.encode({'iss':'heydoc', 'sub':event['username'],'exp':1633633866},'heydoc',algorithm='HS256')
                event['jwt']=enc.decode("utf-8")
                print(jwt.decode(enc, 'heydoc', algorithms=['HS256']))
                database = boto3.resource('dynamodb')
                table = database.Table('doc')
                event['username']=space(event['username'])
                event['pending']=[]
                event['approved']=[]
                event['ongoing']=[]
                r=list(event['Specialist'].split(','))
                for i in range(len(r)):
                    r[i]=(space(r[i])).lower()
                event['Specialist']=r
                r=list(event['degrees'].split(','))
                for i in range(len(r)):
                    r[i]=(space(r[i]))
                event['degrees']=r
                for i in event.keys():
                    if i in ['name','username','city']:
                        try:
                            event[i]=event[i].lower()
                        except:
                            pass
                table.put_item(Item = event)
            else:
                enc=jwt.encode({'iss':'heydoc', 'sub':event['username'],'exp':1633633866},'heydoc',algorithm='HS256')
                event['jwt']=enc.decode("utf-8")
                print(jwt.decode(enc, 'heydoc', algorithms=['HS256']))
                database = boto3.resource('dynamodb')
                table = database.Table('pat')
                event['username']=space(event['username'])
                event['pending']=[]
                event['approved']=[]
                event['ongoing']=[]
                for i in event.keys():
                    if i in ['name','username','city']:
                        try:
                            event[i]=event[i].lower()
                        except:
                            pass
                table.put_item(Item = event)
                
            d['body']=json.dumps({'success':True})
    return d