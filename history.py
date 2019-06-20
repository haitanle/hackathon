import json
from botocore.vendored import requests
import random
import application

# https://givevoicetofootball.fifa.com/api/v1/competitionstatistics/competition/103

# https://givevoicetofootball.fifa.com/api/v1/calendar/matches?idSeason=251475&idCompetition=103

# https://givevoicetofootball.fifa.com/api/v1/playerstatistics/match/300144337/team/1882879/players

# https://givevoicetofootball.fifa.com/api/v1/seasonstatistics/season/251475/team/1882879/players




def randomizeSeason(data):
    randomSel = random.choice(data)
    return {'seasonId': randomSel['IdSeason'],
            'name': randomSel['Name'][0]['Description']}


def getScorer(matchId, teamId):
    apiURL = "https://givevoicetofootball.fifa.com/api/v1/playerstatistics/\
match/%s/team/%s/players" %(matchId, teamId)

    r = requests.get(apiURL)
    gameStateByTeam = r.json()
    r.close()

    playerList = gameStateByTeam['Results']

    scorerListbyId = []
    for player in playerList: 
        for stat in player['Stats']:
            if stat["Type"] == 1 and stat['Value'] > 0:
                scorerListbyId.append(player['IdPlayer'])

    return scorerListbyId

def getScorerName(seasonId, teamId, scorerListById):
    apiURL = "https://givevoicetofootball.fifa.com/api/v1/seasonstatistics/\
season/%s/team/%s/players" % (seasonId, teamId)

    r = requests.get(apiURL)
    teamStatForSeason = r.json()
    r.close()

    playerList = teamStatForSeason['Results']

    scorerListByName = []
    for player in playerList:
        playerId = player['IdPlayer']
        if playerId in scorerListById:
            scorerListByName.append(player['PlayerName'][0]['Description'])

    return scorerListByName


def getStartIndexFrom(ithDay,matchList):
    matchDateList = []

    index = -1
    try: 
        while True:
            index += 1
            matchDate = matchList[index]['LocalDate'].split('T')[0]
            if matchDate not in matchDateList:
                matchDateList.append(matchDate)
            if len(matchDateList) == ithDay:
                # print (matchDateList, index)
                return index
    except IndexError:
        return 13 # catch-all for tournaments that last for more than 14 days


def getPastSeason(dayNumber):

    r = requests.get('https://givevoicetofootball.fifa.com/api/v1/competitionstatistics/competition/103')
    datastore = r.json()
    r.close()

    randomSeason = randomizeSeason(datastore['SeasonStats'][:-1])

    seasonId = randomSeason['seasonId']
    seasonName = randomSeason['name'].split('FIFA')[1].lstrip()

    requestUri = 'https://givevoicetofootball.fifa.com/api/v1/calendar/matches?\
idSeason=%s&idCompetition=103'%seasonId

# print(requestUri)

    r = requests.get(requestUri)
    seasonData = r.json()
    r.close()

    startIndex = getStartIndexFrom(dayNumber, seasonData['Results'])

    dayObj = seasonData['Results'][startIndex]

    homeName = dayObj['Home']['TeamName'][0]['Description']
    homeId = dayObj['Home']['IdTeam']
    homeScore = dayObj['Home']['Score']

    awayName = dayObj['Away']['TeamName'][0]['Description']
    awayId = dayObj['Away']['IdTeam']
    awayScore = dayObj['Away']['Score']
    matchId = dayObj['IdMatch']


    output = "Today in history, %s played %s to a score of %s to %s in %s," \
    %(homeName,awayName,homeScore,awayScore, seasonName)

    if homeScore > 0: 
        scorerListById = getScorer(matchId,homeId)

        output+= " scored for %s by " % homeName
        for player in getScorerName(seasonId, homeId, scorerListById):
            output += "%s," % player

    if awayScore > 0: 
        scorerListById = getScorer(matchId,awayId)

        output+= " scored for %s by " % awayName
        for player in getScorerName(seasonId, awayId, scorerListById):
            output += "%s," % player

    return output




#print(getPastSeason(16))