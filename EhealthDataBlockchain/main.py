#!/usr/bin/env python

from extractData import *
from experiment import *

def main():
    # catching data in json
    dataObject = open_data()
    for i in range(200):
        print(dataObject[i])

    # show the data by name
    out = 1
    while(out != 0):
        name = input('Enter the name of json data:\n[heartBeats]'
                     '\n[speed]\n[acelerometerX]\n[acelerometerY]\n'
                     '[acelerometerZ]\n[indexData]\n')
        print('Start printing json data ... ')
        show_data_by_name(name= name, json_data= dataObject)
        out = int(input('Press 0 to out and 1 to continue: '))


    print('Enter one of the options: \n'
          '1 - Experiment I\n2 - Experiment II\n'
          '3 - Experiment III\n4 - Experiment IV')
    option = int(input('Number: '))

    out = 0
    while(out != 1):
        if (option ==  1):
            first_experiment(dataObject)
        elif (option == 2):
            second_experiment(dataObject)
        elif (option == 3):
            third_experiment(dataObject)
        elif (option == 4):
            fourth_experiment(dataObject)
        else:
            print('Invalid Number\n')
        # asking for a new experiment
        out = int(input('Press 1 to finish and 0 to continue: '))


if __name__ == '__main__':
    main()


