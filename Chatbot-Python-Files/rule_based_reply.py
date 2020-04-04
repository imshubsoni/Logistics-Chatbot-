import re                           # import re

# defining classes and thier responses ->
greeting_response = ["hi", "hello", "hey"]
goodbye_response = ["bye", "talk to you later"]
parcel_inquiry_response = ["enter tracking id"] 
thank_response = ['happy to help','don\'t mention it','my pleasure']
inquiry_response = ['i\'m doing ok','ok','i\'ve been better']
future_response = ['yes','no','maybe']
tracking_id_response = ["under shipment","delivered","in process","started"]
what_you_response = ['nothing', 'not much']
are_you_response = ['yes','no', 'maybe']
when_response = ['soon','not now']
no_response = ['[No Suggestion]']

def bot_response(user_input):
    # searching patterns and making system response accordingly -->
    # greeting -->
    if re.match('hi|hi\s+there|hello|hey|good\s+[morning|afternoon|evening|day]', user_input):
        return greeting_response
    # goodbye -->
    elif re.match('goodbye|bye|see\s+ya|gotta\s+go', user_input):
        return goodbye_response
    # parcel_inquiry -->
    elif re.match('[want|please\s+check|look\s+in]\s+product\s+inquiry|where\s+is\s+product', user_input):
        return parcel_inquiry_response
    # tracking_id -->
    elif re.match('tracking\s+id|1|2|3|4|5|6|7|8|9|0', user_input):
        return tracking_id_response
    # how are you -->
    elif re.match('how\s+are\s+you.*|how.*going', user_input):
        return inquiry_response
    # thanks -->
    elif re.match('thank', user_input):
        return thank_response
    # are you -->
    elif re.match('are.*you', user_input):
        return are_you_response
    # when -->
    elif re.match('when.*you', user_input):
        return when_response
    # what's up -->
    elif re.match('sup|what.*[happening|up|you]', user_input):
        return what_you_response
    # else -->
    else:
        return no_response

print("Hello and welcome!, ask question and I will provide you with some answer to each question.")
flag = True
while flag:
    user_input = input('user:-  ').lower() # get input and convert to lowercase
    if not re.search('quit|exit', user_input):
        response = bot_response(user_input)
        for i in range(0, len(response)):
            print('Bot:- ' + response[i])
    else:
        flag = False
