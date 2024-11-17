
import argparse
import json
import datetime
import os
from .times import times
from colorama import init, Fore, Style  # idk what is style i didn;t used it


def main():
    init()  # for initialising colours not the other class


intitial_structure = {  # json for storing data , i could also use simple file but someone said json is good
    "sessions": []  # it goes inside this list
}
if not os.path.exists('log.json'):
    with open('log.json', 'w') as file:
        json.dump(intitial_structure, file, indent=2)

parser = argparse.ArgumentParser(
    description="A CLI Program that tracks time", add_help=True)
parser.add_argument('-start_warhawking',
                    action='store_true', help='start the time')
parser.add_argument('-spread_peace', action='store_true', help='end the timer')
parser.add_argument('-log', action='store_true', help='show all your report')
parser.add_argument('-log_del', action='store_true',
                    help='delete your log report')
arguments = parser.parse_args()

start = None
start_time = None
clock = times()
if arguments.start_warhawking:

    start = clock.createtime()
    if os.path.exists('start.json'):
        print(
            f'{Fore.LIGHTRED_EX}ERROR :TIMER IS ALREADY RUNNING STOP THE TIMER BY -spread_peace')
    else:
        start_str = start.strftime('%Y-%m-%d %H:%M:%S')
        with open('start.json', 'w') as file1:
            json.dump(start_str, file1)
        print(f'{Fore.RED}Project started at {start_str}')
elif arguments.spread_peace:
    end = clock.createtime()
    try:
        end_time_str = end.strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strptime(
            end_time_str, '%Y-%m-%d %H:%M:%S')
        with open('start.json', 'r') as file:
            start_str = json.load(file)
            start_time = datetime.datetime.strptime(
                start_str, '%Y-%m-%d %H:%M:%S')

        time_diff = end_time - start_time

        totalseconds = int(time_diff.total_seconds())
        hours = totalseconds//3600
        minutes = (totalseconds % 3600)//60
        seconds = totalseconds % 60
        # pushing into log.json 
        new_session = {
            "start time": start_str,
            "end_time": end_time_str,
            "duration": {
                "hours": hours,
                "minutes": minutes,
                "seconds": seconds,

            },

        }
        with open('log.json', 'r') as file:
            data = json.load(file)
        data["sessions"].append(new_session)
        with open('log.json', 'w') as file:
            json.dump(data, file, indent=2)
        if (hours == 0 and minutes == 0 and seconds != 0):
            print(f'{Fore.RED}You spend {seconds} seconds working (you are lazy)')
        elif (hours == 0 and minutes != 0):
            print(
                f'{Fore.RED}You spend {minutes} minutes and {seconds} seconds working (you can do better ;))')
        elif (hours != 0 and minutes != 0 and seconds != 0):
            {
                print(
                    f'{Fore.RED}{hours}you spend {hours} hours {minutes} minutes and {seconds} seconds working (good work cya tomorrow)')
            }
        os.remove('start.json')
    except FileNotFoundError:
        print(
            f'{Fore.GREEN}Error : start time not found . please run with -start_warhawking first')
elif arguments.log:

    with open('log.json', 'r') as file:
        data = json.load(file)
    for session in data["sessions"]:
        print("---------------------------")
        print(f"{Fore.RED}Start: {session['start time']}")
        print(f"{Fore.GREEN}End: {session['end_time']}")
        print(
            f"{Fore.BLUE}Total time spend on this session {session['duration']['hours'] } hours {session['duration']['minutes']} minutes {session['duration']['seconds']} seconds")
elif arguments.log_del:
    os.remove('log.json')
if __name__ == '__main__':
    main()
