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
    d={"statusCode": 200, "body": "results"}
    dynamodb = boto3.resource('dynamodb')
    event=json.loads(event['body'])
    table = dynamodb.Table('doc')
    response = table.scan()
    data = response['Items']
    ans=[]
    for i in data:
        #print(i)
        if (space(event['name'])=='' or i['name']==(space(event['name'])).lower()) and (space(event['specialist'])=='' or (space(event['specialist'])).lower() in i['Specialist']) and (space(event['city'])=='' or (space(event['city'])).lower() == i['city']):
            ans.append(i)
    d['body']=json.dumps({'values':ans})
    print(ans)
    print(d)
    return d
    