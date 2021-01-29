from DatabaseConnection import getResults
from classes.Move import Move
from classes.Coach import Coach
from classes.Team import Team
from classes.TeamPerformance import TeamPerformance
from classes.teamPerformanceDetails import TeamPerformanceDetails


def get_Performance_Details_List_By_PerformanceId(performanceId):
    teamPerformanceDetailsList = []
    query = "SELECT t.`moveId`, a.name , " \
            "t.`id` , t.`totalCorrectMoves`, t.`totalwrongMoves`, " \
            "t.`totalDuration`, t.`performancePercentage` " \
            "FROM `teamperformancedetails` AS t " \
            "JOIN `activity` AS a " \
            "ON (a.id = t.moveId) " \
            "WHERE t.isdeleted = 0 " \
            "AND a.isdeleted = 0 " \
            f"AND t.`teamPerformanceId` = {performanceId}"
    for row in getResults(query):
        move = Move(row[0], row[1])
        teamPerformanceDetails = TeamPerformanceDetails(row[2], move.__dict__, row[3], row[4], row[5], row[6])
        teamPerformanceDetailsList.append(teamPerformanceDetails.__dict__)

    return teamPerformanceDetailsList


def getPerformanceList(teamId):
    performanceList = []
    query = "SELECT `id`, `totalCorrectMoves`, `totalWrongMoves`, `totalDuration`, `year`, `month`, `performancePercentage` " \
            "FROM `teamperformance` " \
            f"WHERE `teamId`= {teamId} AND `isdeleted` = 0"

    for row in getResults(query):
        performanceDetailsList = get_Performance_Details_List_By_PerformanceId(row[0])
        performance = TeamPerformance(performanceDetailsList, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        performanceList.append(performance.__dict__)
    return performanceList


def getTeamsByCoachId(coachId):
    teams = []
    query = "SELECT t.id , t.name " \
            "FROM `team` AS t " \
            "JOIN `teammembers` AS tm " \
            "ON (t.id = tm.teamId) " \
            f"WHERE `coachId` = {coachId} " \
            "AND t.isdeleted = 0 " \
            "AND tm.isdeleted = 0 "
    print(query)
    for row in getResults(query):
        team = Team(row[0],row[1])
        teams.append(team)
    return teams


def getCoachTeamsList(coachId):
    teamsList = []
    teams = getTeamsByCoachId(coachId)
    for team in teams:
        performances = getPerformanceList(team.id)
        team.setTeamPerformance(performances)
    for team in teams:
        teamsList.append(team.__dict__)
    return teamsList


def get_sessionDetailsListbySessionId(id):
    pass


def getSessionsList(playerId):
    SessionsList = []
    query = "";
    for session in session:
        sessiondetailsList = get_sessionDetailsListbySessionId(session.id)
        session = Session(id, sessiondetailsList)
        SessionsList.append(session);


def gfetUserSessionsData(playerId):
    player = Player(getSessionsList(playerId))
    return player.__dict__