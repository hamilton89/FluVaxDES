# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Simpy library and simpy_helpers package resources:
# GitHub tutorial: https://github.com/bambielli/simpy_helpers/blob/master/Using_Simpy_Helpers_Package.ipynb
# YouTube tutorial: https://www.youtube.com/watch?app=desktop&v=TALKZZV0TiU

import simpy
from simpy_helpers import Entity, Resource, Source, Stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

###############################################################################
############################## Globals ########################################
###############################################################################

# Parameters
MEAN_SERVICE_TIME = 6                                                          # We assume it takes 6 minutes to fill out paper work and get vaccinated.                              
BALK_TOLERANCE = 30                                                            # Entering patients will leave if the line is longer than 30 people.
SIMULATION_TIME = 60                                                           # We run the simulation for 1 hour.

# Counters
arrived_count = 0                                                              # Counter for tracking how many patients have arrived.
balked_count = 0                                                               # Counter for tracking how many patients have balked.
served_count = 0                                                               # Counter for tracking how many patients have been vaccinated.
                                                                               # Some patients are still waiting after 60 minutes so balked + served != arrived.
# Lists for data collection
arrived_lst = []                                                               # List of patients arrived.
balked_lst = []                                                                # List of patients balked.
served_lst = []                                                                # List of patients served (vaccinated). 

###############################################################################
############################ Simpy classes ####################################
###############################################################################

class processEntity(Entity):                                                   # Entity is a "patient" passing through the clinic simulation. 
    def process(self):                                                         # The process function outlines a patient's actions or steps during simulation.
        global arrived_count, balked_count, served_count                       
        arrived_count += 1                                                     # First, the patient arrives and is added to the arrived counter.
        arrived_lst.append(1)                                      # Append arrived_count to arrived_lst.
        if len(my_resource.queue) <= BALK_TOLERANCE:                           # If the line is less than or equal to the patient's balk tolerance,
            served_lst.append(1)                                               # add 1 to the served_lst and
            balked_lst.append(0)                                               # add a 0 to the balked_lst.
        if len(my_resource.queue) > BALK_TOLERANCE:                            # If the line is longer than patients' balk tolerance,
            balked_count += 1                                                  # increment the balked_count,
            balked_lst.append(1)                                               # add 1 to the balked_lst, and
            served_lst.append(0)                                               # add a 0 to the served_lst.
            return
        else:                                                                  # If the patient does not balk,
            yield self.wait_for_resource(my_resource)                          # they wait for the next free nursing station and
            yield self.process_at_resource(my_resource)                        # are vaccinated.
            served_count += 1                                                  # 1 is added to the served count.
            self.release_resource(my_resource)                                 # Finally, the patient exists the simulation.

class myResource(Resource):                                                    # Resource represents a nurse administering vaccinations.
    def service_time(self, entity):                                            # The time it takes to vaccinate a patient is
        return np.random.exponential(MEAN_SERVICE_TIME)                        # is drawn from an exponential distribution around the assigned mean service time.
    
class generateCustomers(Source):                                               # Source is where Entities (patients) are coming from.
    def interarrival_time(self):                                               # Patients arrive at intervals
        return np.random.exponential(MEAN_TIME_BETWEEN_ARRIVALS)               # drawn from an exponential distribution around the mean time between arrivals.
    def build_entity(self):
        attributes = {}                                                        # Entities can have attributes (e.g., standard vs. priority customer) but we do not use any.
        return processEntity(env,attributes)

###############################################################################
##################### Loop through hours in a day #############################
###############################################################################

                                                                               # We assume that 1,300 patients will arrive throughout the day
                                                                               # with the majority arriving around 2pm (the 5th hour between 9am -5pm).
                                                                               # We run the simulation for each hour of the day (each with a different number of patients)
                                                                               # and for different numbers of nurses (1-10) to determine wait times given the number of nurses.
# Lists for loop
num_lst = [50,100,150,200,300,250,150,100]                                     # List to loop through different numbers of patients for each hour of the day.
cap_lst = [1,2,3,4,5,6,7,8,9,10]                                               # List to loop through different numbers of nurses.
data_lst = []                                                                  # Data collection list.                                       

i = 1                                                                          # Counter for 8 hours in the day.
for num in num_lst:                                                            # Loop through the different number of patients for each hour.
    data_lst.append(i)                                                         # Append the hour (i) for which we are simulating to the data_lst.
    i += 1                                                                     # Increment i so the next iteration will be the next hour.
    NUM_ENTITIES = num                                                         # The number of entities in this iteration will be the number of patients for this hour.
    data_lst.append(NUM_ENTITIES)                                              # Append the number of patients in this iteration to the data_lst.
    MEAN_TIME_BETWEEN_ARRIVALS = SIMULATION_TIME / NUM_ENTITIES                # We assume that patients arrive at roughly even intervals over the hour.
    for c in cap_lst:                                                          # Loop through the number of nurses (1-10). 
        np.random.seed(34)                                                     # c is for 'capacity' or the number of entities that can be processed at the same time.                                       
        env = simpy.Environment()                                              # Create the Environment using simpy library.
        my_resource = myResource(env, capacity = c)                            # Create the Resource (i.e., a flu clinic with c nurses administering vaccinations)
        my_source = generateCustomers(env, number = NUM_ENTITIES)              # Create the Source where entities come from (i.e., num patients)
        env.process(my_source.start(debug=False))                              # Assign the steps in the process function to the Environment.
        env.run(until=SIMULATION_TIME)                                         # Run the simulation for 60 minutes.
        data_lst.append(np.max(Stats.get_waiting_times()))                     # Append the max waiting time for the ith hour and c number of nurses.
        
# Output data
max_wait = pd.DataFrame(np.array(data_lst).reshape(8,12))                      # Create array out of collected data in data_lst.
max_wait = max_wait.rename(columns={0: "Hour",                                 # Rename columns.
                            1: "No. of patients", 
                            2: "Nurses=1",
                            3: "Nurses=2", 
                            4: "Nurses=3", 
                            5: "Nurses=4", 
                            6: "Nurses=5", 
                            7: "Nurses=6", 
                            8: "Nurses=7", 
                            9: "Nurses=8", 
                            10:"Nurses=9", 
                            11:"Nurses=10"})
max_wait = max_wait.transpose()
max_wait.to_csv('table_maxwait_perhour_pernurses.csv',header=False)                                    # Ouput csv to FluVaxDES folder.

###############################################################################
##################### Run for peak hour #######################################
###############################################################################

NUM_ENTITIES = 300                                                             # ~300 patients arrive during the peak hour of 2-3pm.
MEAN_TIME_BETWEEN_ARRIVALS = SIMULATION_TIME / NUM_ENTITIES                    # We assume patients arrive at roughly even intervals over the hour.
NUM_NURSES = 4                                                                  # There will be this many nursing stations for this run.
arrived_count = 0                                                              # Counter for patients arrived.
balked_count = 0                                                               # Counter for patients balked.
served_count = 0                                                               # Counter for patients vaccinated.
arrived_lst = []                                                               # List for patients arrived.
balked_lst = []                                                                # List for patients balked.
served_lst = []                                                                # List for patients served.

env = simpy.Environment()                                                      # Create Environment using Simpy.
my_resource = myResource(env, capacity = NUM_NURSES)                           # Create the Resource (i.e., 4 nursing stations)               
my_source = generateCustomers(env, number = NUM_ENTITIES)                      # Create the Source where patients come from.
env.process(my_source.start(debug=False))                                      # Assign steps in process function to the Environment.
env.run(until=SIMULATION_TIME)                                                 # Run for 60 minutes.

# Results for peak hour
peak_dic = {}
peak_dic['1Hour'] = 5
peak_dic['2No. of pations'] = NUM_ENTITIES
peak_dic['3No. of nurses'] = NUM_NURSES
peak_dic['4Arrived'] = arrived_count
peak_dic['5Balked'] = arrived_count
peak_dic['6Served'] = arrived_count
peak_dic['7Still waiting'] = arrived_count - balked_count - served_count
peak_dic['8Max wait time'] = np.max(Stats.get_waiting_times())
peak_dic['9Mean wait time'] = np.mean(Stats.get_waiting_times())
peak_df = pd.DataFrame.from_dict(peak_dic, orient='index').reset_index()
peak_df['index'] = peak_df['index'].str[1:]
peak_df = peak_df.rename(columns={'index': "", }).transpose()
peak_df.to_csv('table_peakhour_stats.csv', index=False, header=False)

###############################################################################
##################### Vizualizations for peak hour ############################
###############################################################################

# No. Patients per wait time (histogram)                                                                      
waiting_times = Stats.get_waiting_times()
sns.histplot(waiting_times,bins =20)
plt.ylabel('No. of patients');
plt.xlabel('Wait time (min)');
plt.title('Patients per wait time during peak');
plt.savefig('histogram_wait_times.png');
plt.clf()

# Queue size over time (line graph)
resource_queue = Stats.queue_size_over_time(my_resource)
sns.lineplot(y=resource_queue,x=range(0,len(resource_queue)))
plt.title('Queue size over time');
plt.ylabel('No. of patients');
plt.xlabel('Simulation length (min)');
plt.title('Queue size over time durin peak hour');
plt.savefig('graph_queue_size.png');
plt.clf()

# Wait times over time (line graph) ?????????????????????????????????????????????????????????????????????
resource_wait = Stats.get_waiting_times(my_resource)
time = np.linspace(0, 61, num=len(resource_wait))
sns.lineplot(y=resource_wait,x=time)
plt.ylabel('Wait time (min)');
plt.xlabel('Simulation length (min)');
plt.title('??? Max wait time over time during peak hour ???');
plt.savefig('graph_wait_times.png');
plt.clf()


# Arrived, balked, served over time (line graph)                               # The green line of patients vaccinated is an over-estimate as it assumes 
arrived_arr = np.array(arrived_lst)                                            # that the people still waiting at the end of the simulation (60 min) have been vaccinated.   
balked_arr = np.array(balked_lst)
served_arr = np.array(served_lst)                                              
counts_arr = np.stack((arrived_arr,balked_arr,served_arr), axis=1)
counts_df = pd.DataFrame(counts_arr)
counts_df = counts_df.rename(columns={0: "Arrived", 
                                      1: "Balked",
                                      2: "Served"})
counts_df['Arrived_cum'] = counts_df['Arrived'].cumsum()
counts_df['Balked_cum'] = counts_df['Balked'].cumsum()
counts_df['Served_cum'] = counts_df['Served'].cumsum()
arrived = np.array(counts_df['Arrived_cum'])
balked = np.array(counts_df['Balked_cum'])
served = np.array(counts_df['Served_cum'])
time = np.linspace(0, 61, num=arrived_count)
plt.plot(time,arrived,color='blue');
plt.plot(time,balked,color='red');
plt.plot(time,served,color='green');
plt.ylabel('No. of patients');
plt.title('Patients arrived (blue), balked (red), and vaccinated (green) \n over time during the peak hour');
plt.title('Arrived, balked, and vaccinated over time during peak hour');
plt.savefig('graph_arrived_balked_vaccinated.png');
plt.clf()


