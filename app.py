import application 
import history
import datetime

def runApp():
    todayDate = str(datetime.datetime.now()).split(" ")[0]

    # output, iDay = application.gameDayDescription('2019-06-07')
    output, iDay = application.gameDayDescription(todayDate)

    historyOutput = history.getPastSeason(iDay)

    output+=historyOutput

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


#print(runApp())