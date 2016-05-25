import j_DBfunctions
import j_users
import sqlite3
import j_weather




cor_cities = {'Los Gatos':'Castle Rock', 'Berkeley':'Mortar and Indian Rock', 'Yosemite':'Yosemite', 'Sonora,us':'Columbia Boulders', 'Bolinas':'Stinson and Mickey\'s Beach', 'San Anselmo':'Mt. Tam', 'South Lake Tahoe':'Lake Tahoe', 'Monte Rio': 'Fort Ross'}
cities = ['Los Gatos', 'Berkeley', 'Yosemite', 'Sonora,us', 'Bolinas', 'San Anselmo', 'South Lake Tahoe', 'Monte Rio']

#StartProgram will start the application
def StartProgram():
    while True:
        try:
            j_DBfunctions.CreateDB()
            first_user = j_users.NewUserInstance()
            j_DBfunctions.saveUser(first_user)

            climbday1 = j_weather.dayIndex()
            city_data_list = [j_weather.CreateCityInsta(x, climbday1) for x in cities]

            city_matches = j_weather.MatchList(city_data_list, first_user)
            actual_matches = [cor_cities[x] for x in city_matches]
            print'\n'
            for places in actual_matches:
                print places
            print '\nThe above areas fit your criteria.  Happy Climbing!\n'
            print '*'*80
            
            quit_option = raw_input('Type \"quit\" to exit enter anything else to run the program again. ')
            if quit_option == 'quit':
                break

        except sqlite3.OperationalError:
            for names in j_DBfunctions.nameQuery():
                print names[0]

            print '\n'
            option = raw_input('Enter a username from list above or type \"create new\". ')

            if option == 'create new':
                additional_user = j_users.NewUserInstance()
                j_DBfunctions.saveUser(additional_user)

                climbday2 = j_weather.dayIndex()
                city_data_list2 = [j_weather.CreateCityInsta(x, climbday2) for x in cities]

                city_matches2 = j_weather.MatchList(city_data_list2, additional_user)
                actual_matches2 = [cor_cities[x] for x in city_matches2]
                print '\n' 
                for places in actual_matches2:
                    print places
                print '\nThe above areas fit your criteria.  Happy Climbing!\n'
                print '*'*80
                
                quit_option = raw_input('Type \"quit\" to exit enter anything else to run the program again. ')
                if quit_option == 'quit':
                    break

            else:
                print '\nHello',option

                option2 = raw_input('\nType \"run\" to find areas that match your preferences, \"overwrite\"\nto enter new information, or \"delete\" to erase this username. ')          
            
                if option2 == 'run':
                    try:
                        query_results = j_DBfunctions.userQuery(option)
                        iso_tuple = query_results[0]
                        new_user = j_users.User(iso_tuple[0], iso_tuple[1], iso_tuple[2])

                        climbday3 = j_weather.dayIndex()
                        city_data_list3 = [j_weather.CreateCityInsta(x,climbday3) for x in cities]

                        city_matches3 = j_weather.MatchList(city_data_list3, new_user)
                        actual_matches3 = [cor_cities[x] for x in city_matches3]
                        print '\n'
                        print 'Name:'+str(new_user.name)+' '+'Temperature(F):'+str(new_user.temp)+' '+'Humidity(%):'+str(new_user.humid)+'\n'
                        for places in actual_matches3:
                            print places
                        print '\nThe above areas fit your criteria.  Happy Climbing!\n'
                        print '*'*80

                        quit_option = raw_input('Type \"quit\" to exit enter anything else to run the program again. ')
                        if quit_option == 'quit':
                            break
                    
                    except IndexError:
                        print '\nLooks like \"{}\" is not in our database.  Try another name or create a new username.\n'.format(option)

                elif option2 =='delete':
                    j_DBfunctions.deleteUser(option)

                elif option2 == 'overwrite':
                    j_DBfunctions.deleteUser(option)
                    replace_user = j_users.NewUserInstance()
                    j_DBfunctions.saveUser(replace_user)

                    climbday4 = j_weather.dayIndex()
                    city_data_list = [j_weather.CreateCityInsta(x, climbday4) for x in cities]

                    city_matches4 = j_weather.MatchList(city_data_list, replace_user)
                    actual_matches4 = [cor_cities[x] for x in city_matches4]
                    print '\n'
                    for places in actual_matches4:
                        print places
                    print '\nThe above areas fit your criteria.  Happy Climbing!\n'
                    print '*'*80
                
                    quit_option = raw_input('Type \"quit\" to exit enter anything else to run the program again. ')
                    if quit_option == 'quit':
                        break
                
                else:
                    print 'Didn\'t get that.  Try again.'

if __name__ == '__main__':
    print '\n'
    print '*'*80
    print '''BAY AREA CLIMBING TEMPS:

    The program will return a list of local bouldering 
    areas that match your preferences for temperature and humidity; additionally, 
    the list will not include any areas where it is forecasted to rain.

    Happy Climbing!'''
    print '*'*80
    print '\n'

    StartProgram()
