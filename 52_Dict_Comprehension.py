def main():
    temp = {0,10,25,50,67,99,100}

    newDict = {t: (t * 9/5) + 32 for t in temp}  #t:(t * 9/5) + 32 is k:v pair for temp in celcius:fahrenhiet
    print(newDict)

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    newTeam = {k:v for team in (team1,team2) for k,v in team.items()}  #Adding both teams dict into one
    print(newTeam)


if __name__ == "__main__": main()
