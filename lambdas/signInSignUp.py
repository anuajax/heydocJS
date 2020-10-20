import json
import boto3
import jwt
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
    #eve = {'resource': '/test', 'path': '/test', 'httpMethod': 'GET', 'headers': None, 'multiValueHeaders': None, 'queryStringParameters': {'name': 'ravi'}, 'multiValueQueryStringParameters': {'name': ['ravi']}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': '0dkh3z', 'resourcePath': '/test', 'httpMethod': 'GET', 'extendedRequestId': 'UGGHIHz9oAMFqAw=', 'requestTime': '08/Oct/2020:14:08:32 +0000', 'path': '/test', 'accountId': '429229607726', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1602166112729, 'requestId': '651a351c-ffa2-41c3-a48c-1681629984c8', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:sts::429229607726:assumed-role/vocstartsoft/user723695=2017uec1633@mnit.ac.in', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'aws-internal/3 aws-sdk-java/1.11.848 Linux/4.9.217-0.3.ac.206.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation', 'accountId': '429229607726', 'caller': 'AROAWH4AUBMXM2BMJHPGJ:user723695=2017uec1633@mnit.ac.in', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIAWH4AUBMXHBRJZAFS', 'cognitoAuthenticationProvider': None, 'user': 'AROAWH4AUBMXM2BMJHPGJ:user723695=2017uec1633@mnit.ac.in'}, 'domainName': 'testPrefix.testDomainName', 'apiId': 'j4z72d2uie'}, 'body': None, 'isBase64Encoded': False}
    client = boto3.client('dynamodb')
    d={"statusCode": 200, "body": "results"}
    if event['httpMethod']=='GET':
        try:
            a=client.get_item(TableName=event['queryStringParameters']['flag'],Key={
                'username': {'S': str(event['queryStringParameters']['username'])}
            })
            print(a)
            x=dictToJson(a['Item'])
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
            d['body']=(json.dumps(x))
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
                event['pending']={}
                event['approved']={}
                event['ongoing']=[]
                event['previous']=[]
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
                event['pending']={}
                event['approved']={}
                event['ongoing']=[]
                event['previous']=[]
                for i in event.keys():
                    if i in ['name','username','city']:
                        try:
                            event[i]=event[i].lower()
                        except:
                            pass
                table.put_item(Item = event)
                
            d['body']=json.dumps({'success':True})
    return d
    