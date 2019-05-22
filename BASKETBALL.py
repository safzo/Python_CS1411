#a_int = 5
#b_int = 3
#if a_int > b_int:
#    print ('a_it is larger than b_int')
#else:
#    print ('b_int is larger than a_int')

team1_points = int (input ( ' Enter team 1\'s points: '))
team2_points = int (input (' Enter team2\'s points: '))
time_left = float (input (' Enter the time left in minutes: '))

#Shortcut to time_left = time_left * 60
time_left *= 60

team_ball= int(input("Which team has the ball?: 1 or 2?:" ))

if team1_points > team2_points:
    points_ahead = team1_points - team2_points
else:
    points_ahead = team2_points - team1_points
    points_ahead -=3

if team1_points > team2_points:
    if team_ball ==1:
        points_ahead -= .5
    else:
        points_ahead -= .5
else:
    if team_ball == 2:
        points_ahead += .5
    else:
        points_ahead -= .5

points_squared = points_ahead**2

if points_squared > time_left:
    if team1_points > team2_points:
        print ('Team1\'s lead of ', team1_points-team2_points, 'is safe')
    else:
        print(' Team2\'s lead of', team2_points-team1_points, 'is safe')
    if team1_points < team2_points:
        print ('Team1\'s lead of ' ,team1_points-team2_points, ' is not safe')
    else:
        print ('Team2\'s lead of ' ,team2_points-team1_points, ' is not safe')

                            
