# import requests
import json
from datetime import datetime
import util
from MatchDay import MatchDay

#timezone global variable - 

def getGameData(day, gameData):
    """get WC gameData from https://givevoicetofootball.fifa.com/api/v1/calendar/matches?idSeason=278513&idCompetition=103
    input: (object) day Matchday 
    input: (object) gameData
    return: (string) homeTeam, awayTeam, stadium, city, country
    """
    dayDescription = "Today, "
    for gameIndex in day.matchIndex:

            try: 
                homeTeam = gameData['Results'][gameIndex]['Home']['TeamName'][0]['Description']
                awayTeam = gameData['Results'][gameIndex]['Away']['TeamName'][0]['Description']
            except TypeError: 
                #TODO: add advance stage if data is not available
                homeTeam = 'knockout stage team 1'
                awayTeam = 'knockout stage team 2'

            stadium = gameData['Results'][gameIndex]['Stadium']['Name'][0]['Description']
            city = gameData['Results'][gameIndex]['Stadium']['CityName'][0]['Description']
            country = 'France'

            localTime = util.convertUTCtoLocal(gameData['Results'][gameIndex]['Date'])
            localTime = localTime.split('T')[1]

            dayDescription += ("%s plays %s at %s in %s stadium in %s.\n" \
            %(homeTeam, awayTeam, localTime, stadium, city))


    return dayDescription



def getMatchDatesList(data):
    """take json object data and return list of match dates
    input: (object) data
    return: (list) of unique match date ordered
    """
    matchDateList = []

    for match in data['Results']:
        matchDate = match['Date'].split('T')[0]
        if matchDate not in matchDateList:
            matchDateList.append(matchDate)
    return matchDateList


def getCompetitionDates(data):
    """determine date and match number
    input: (object) data - json object
    return: (list) list of Matchday objects
    """
    matchDateList = []
    matchObjectList = []

    gameIndex = 0;
    for match in data['Results']:
        matchDate = match['Date'].split('T')[0]
        if matchDate not in matchDateList:
            matchDateList.append(matchDate)
            day = MatchDay(matchDate)
            day.matchIndex.append(gameIndex)
            matchObjectList.append(day)
        else:
            matchObjectList[-1].matchIndex.append(gameIndex)
        gameIndex+=1

    # Test
    # for day in matchObjectList:
    #     print(day.date,day.matchIndex)

    return matchObjectList


def day_ofCompetition(date,matchDaysList): #could stored in MatchDay object or return from getCompetitionDates()
    """ calculate day # of total # 
    input: (string) date to match
    input: (list) matchDaysList
    return: (string) number of date of total
    """

    return (matchDaysList.index(date)+1, (len(matchDaysList)+2))



with open('match_data.txt', 'r') as f:
    gameData = json.load(f)


#test of creating json file
# with open('computeData.txt', 'w') as outfile:
#     json.dump({"match_day": getMatchDatesList(gameData)}, outfile)

# outfile.close()

#serialize
with open('computeData.txt') as json_file:  
    data = json.load(json_file)['match_day']
json_file.close()




def gameDayDescription(date):

    iDay = day_ofCompetition(date,data)[0]

    dateOut = datetime.strptime(date, '%Y-%m-%d').strftime('%A, %B %d')
    day, ofTotal = day_ofCompetition(date, data)

    output = "Today %s is day %s of %s of the Women's World cup in France. \n"\
    % (dateOut, day, ofTotal)


    dayNumber = (day_ofCompetition(date, data))[0]
    # print("day number %s inside"%dayNumber)

    gameDayList = getCompetitionDates(gameData)

    for gameDate in gameDayList:
        if gameDate.date == date:
            output += getGameData(gameDate, gameData)
            break

    return output, iDay



#print(gameDayDescription('2019-06-07'))


# print("day number outside %s" % dayNumber)