# import application 
# import history
# import datetime
def runApp():
    
    output = "Today is day 28 of 28 of the Women World Cup 2019 in France. Today, USA won 2 to 0 against Netherland in the final match, played in Olympic Lyonnaise stadium in Lyon, France. Goal scorer for the US by Megan Rapinoe and Rose Lavelle. Today in history, Germany played Brazil to a score of 2 to 0 in World Cup China. Goal scorer for Germany by Birgit Prinz and Simone Laudehr."

    return output

def getTodaySchedule():
    todayDate = str(datetime.datetime.now()).split(" ")[0]

    # output, iDay = application.gameDayDescription('2019-06-07')
    output, iDay = application.gameDayDescription(todayDate)

    return output

def getMoreHistory():

    todayDate = str(datetime.datetime.now()).split(" ")[0]

    # output, iDay = application.gameDayDescription('2019-06-07')
    output, iDay = application.gameDayDescription(todayDate)

    historyOutput = history.getPastSeason(iDay)

    return historyOutput

print(runApp())