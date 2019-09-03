launch_message = "Today is Friday, June 28 is day 20 of 25 of the Women's World cup in France. Today, France plays USA in the Quarter-final at 03:00PM in Parc des Princes stadium in Paris. Today in history, USA played Nigeria to a score of 7 to 1 in Women's World Cup USA 1999, scored for USA by Mia Hamm, Kristine Lillly, Michelle Akers, Cindy Cone, Tiffeny Milbrett, scored for Nigeria by Nkiru Okosieme . "
card_title = "Today's Game Schedule"
output_repromt = " Would you like to hear more history?"
more_history = "Today in history, Argentina played Japan to a score of 0 to 1 in Women's World Cup China 2007, scored for Japan by Yuki Nagasto. "


def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()
#------------------------------Part3--------------------------------
# Here we define the Request handler functions
def on_start():
    print("Session Started.")

def on_launch(event):
    return output_json_builder_with_reprompt_and_card(launch_message+output_repromt, launch_message, card_title, output_repromt, False)

def on_end():
    print("Session Ended.")
#-----------------------------Part3.1-------------------------------
# The intent_scheme(event) function handles the Intent Request. 
# Since we have a few different intents in our skill, we need to 
# configure what this function will do upon receiving a particular 
# intent. This can be done by introducing the functions which handle 
# each of the intents.
def intent_scheme(event):
    
    intent_name = event['request']['intent']['name']
    
    if intent_name == "AMAZON.YesIntent":
        return tell_me_more()
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)
#---------------------------Part3.1.1-------------------------------
# Here we define the intent handler functions
# def game_schedule():
#     todaySchedule = app.getTodaySchedule()
#     more_MSG = todaySchedule + "Would you like to hear today's history?"
#     reprompt_MSG = "Do you want to hear more history?"
#     card_TEXT = todaySchedule
#     card_TITLE = "Today's game schedule"
#     return output_json_builder_with_reprompt_and_card(more_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)


def tell_me_more():
    return output_json_builder_with_reprompt_and_card(more_history+output_repromt, more_history, "Today in History", output_repromt, False)


def stop_the_skill(event):
    stop_MSG = "Enjoy the World Cup. Good bye."
    reprompt_MSG = ""
    card_TEXT = "Enjoy the World Cup. Good bye."
    card_TITLE = "Exit skill"
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "Do you want to hear more history?"
    reprompt_MSG = "Do you want to hear more history?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear more history?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
#------------------------------Part4--------------------------------
# The response of our Lambda function should be in a json format. 
# That is why in this part of the code we define the functions which 
# will build the response in the requested format. These functions
# are used by both the intent handlers and the request handlers to 
# build the output.
def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict

def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict
    
def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict    

def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict

def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict