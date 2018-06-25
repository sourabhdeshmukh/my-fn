import json
import urlparse

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    qs = urlparse.parse_qs(req)
    if "user_name" in qs:
        if not qs["user_name"][0] == "slackbot":
            emoticons = ""
            msg = qs["text"][0]
            if "dockercon" in msg:
                emoticons = ":whale:"
            elif "serverless" in msg:
                emoticons = ":openfaas: :robot_face:"
            elif "azure" in msg:
                emoticons = ":cloud:"
            elif "sofia" in msg:
                emoticons = ":flag-bg:"
            
            ret = { "text": qs["user_name"][0] + " sent a message with a length of... '" + str(len(req)) + "' " + emoticons }
            return json.dumps(ret)

    return req

