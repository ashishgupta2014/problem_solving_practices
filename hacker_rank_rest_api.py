import requests


def getHomeTeam(team, year, page=1):
    response = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}".format(year=year, team=team, page=page)).json()
    score=0
    for i in response['data']:
        score += int(i['team1goals'])
    if response['total_pages'] > page:
        page += 1
        score+=getHomeTeam(team, year, page)
    return score


def getOppTeam(team, year, page=1):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team2="+team+"&page="+str(page)).json()
    score=0
    for i in response['data']:
        score += int(i['team2goals'])
    if response['total_pages'] > page:
        page += 1
        score+=getHomeTeam(team, year, page)
    return score


def getTotalGoals(team, year):
    return getHomeTeam(team, year) + getOppTeam(team, year)


if __name__ == '__main__':

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)
    print(result)
