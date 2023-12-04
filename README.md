# FluVaxDES
Problem description: 

A university requires all affiliates to receive the flu vaccine and has clinics open on different days and campuses during the flu season. Clinic A is open four days and sees 800-1300 patients per day and has four nurses administering vaccinations each day. Students have reported waiting over 30 minutes to get vaccinated at Clinic A. 

Methods: 

Using the Simpy library and simpy_helpers package in python, we simulate one day at Clinic A, recording maximum wait times as a function of the number of patients visiting per hour and the number of nurses working per hour. Results indicate how many nurses are needed each hour in order to keep wait times under 30 minutes. Then we simulate the peak hour at Clinic A with the current number of nurses (4) and plot the number of patients arrived, balked, and vaccinated over the course of the the hour. 

Assumptions:

1. Clinic A is open 9am - 5pm (8 hours) and a total of 1300 patients arrive during that day.
2. Patients visit Clinic A at different times throughout the day with the majority arriving between 2-3pm (hour 5). To approximate the arrival schedule, we assume 50 patients arrive in hour 1, 100 in hour 2, 150 in hour 3, 200 in hour 4, 300 in hour 5, 250 in hour 6, 150 in hour 7, and 100 in hour 8.
3. Upon arrival, patients will balk (leave without getting vaccinated) if the queue size is over 30 people.
4. It takes approximately 4 minutes to fill out paperwork and 2 minutes to get vaccinated so the total service time is roughly 6 minutes.

Workflow:

Run FluVaxDES.py. This file contains all the code with detailed comments and is separated into the following sections: 
1. Globals: Define parameters (MEAN_SERVICE_TIME, BALK_TOLERANCE, and SIMULATION_LENGTH)
2. Simpy classes: Define classes for Entity, Resource, and Source (see Reference 1 below for descriptions)
3. Loop through hours in a day: Loop through the number of patients each hour (Assumption 2) and record maximum wait times as a function of the number of nurses working per hour. Outputs table_maxwait_perhour_pernurses.csv.
4. Run for peak hour: Run the simulation for the peak hour with 300 patients and 4 nurses and record the number of patients arrived, balked, and vaccinated as well as maximum wait time and average wait time.
5. Visualizations for peak hour: Outputs tables and graphs for peak hour (See Output).

Output:

1. table_maxwait_perhour_pernurses.csv: Maximum waiting time as a function of the number of patients in the hour and the number of nurses working that hour.
2. table_peakhour_stats.csv: Results for a simulation of the peak hour with 300 patients and 4 nurses.
3. graph_queue_size.png: Line graph of queue size over time.
4. graph_wait_times.png: Line graph of max wait time over time.
5. graph_arrived_balked_vaccinated.png: Line graph of arrived, balked, and vaccinated over time. NOTE: This graph overestimates the number of patients vaccinated as it included patients still waiting at the end of the simulation.
6. histogram_wait_times.png: Histogram of the number of students per wait time.

References:

The following resources were used in building the model:
1. GitHub tutorial of simpy_helpers: https://github.com/bambielli/simpy_helpers/blob/master/Using_Simpy_Helpers_Package.ipynb
2. Video tutorial of simpy_helpers: https://www.youtube.com/watch?app=desktop&v=TALKZZV0TiU
3. GitHub CoPilot was used to figure out how to implement balking into the process function.








