'''
    {
        "name": "Marco"
    }
'''


def lambda_handler(event,context):
    if event["name"] == "Marco":
        return "Polo"



        
