# FluVaxDES
Optimizing Flu Clinic Staffing Schedule

By: Alisa Hamilton, Emi Siler, and Parikshit Ranjeet Raje (in partial fullfillment of the course Operation Research)

Problem description: A university requires all affiliates to receive the flu vaccine and has clinics open on different days and campuses during the flu season. Clinic A is open four days and sees 800-1300 patients per day and has four nurses administering vaccinations each day. Students have reported waiting over 30 minutes to get vaccinated at Clinic A. We want to determine how many nurses are needed each hour to keep wait times under 30 minutes.

Methods: We use the Simpy library and simpy_helpers package in python to build a Discrete Event Simulation (DES). First, we simulate the peak hour at Clinic A with the current number of nurses (4) and plot the number of patients arrived, balked, and vaccinated over the course of the the hour. Second, we simulate one day (8 hours) at Clinic A and record maximum wait times as a function of the number of patients arriving per hour and the number of nurses working per hour. 

Assumptions:

1. Clinic A is open 9am - 5pm (8 hours) and a total of 1300 patients arrive during that day.
2. Patients visit Clinic A at different times throughout the day with the majority arriving between 2-3pm (hour 5). To approximate the arrival schedule, we assume 50 patients arrive in hour 1, 100 in hour 2, 150 in hour 3, 200 in hour 4, 300 in hour 5, 250 in hour 6, 150 in hour 7, and 100 in hour 8.
3. Upon arrival, patients will balk (leave without getting vaccinated) if the queue size is over 30 people.
4. It takes approximately 4 minutes to fill out paperwork and 2 minutes to get vaccinated so the total service time is roughly 6 minutes.
5. We assume patients arrive at even intervals over the hour. For example, in an hour with 300 patients, a patient will arrive roughly every 0.2 minutes. This is because simy_helpers uses the mean time between arrivals to schedule when entities enter the simulation.
6. To introduce stochasticity, we assign exponential distributions around the balk tolerance, mean time between arrivals, and mean service time.

Workflow:

Run FluVaxDES.py. This file contains all code with detailed comments and is separated into the following sections: 
1. Simpy classes: Define classes for Entity, Resource, and Source (see Reference 1 below for descriptions)
2. Run for peak hour: Run the simulation for the peak hour with 300 patients and 4 nurses and record the number of patients arrived, balked, and vaccinated as well as maximum wait time and average wait time.
3. Visualizations for peak hour: Outputs tables and graphs for peak hour (See Output).
4. Loop through hours in a day: Loop through the number of patients each hour (Assumption 2) and record maximum wait times as a function of the number of nurses working per hour. Outputs table_maxwait_perhour_pernurses.csv.

Output:

1. table_peakhour_stats.csv: Results for a simulation of the peak hour with 300 patients and 4 nurses.
2. graph_queue_size.png: Line graph of queue size over time.
3. graph_wait_times.png: Line graph of max wait time over time.
4. graph_arrived_balked_vaccinated.png: Line graph of arrived, balked, and vaccinated over time. NOTE: This graph overestimates the number of patients vaccinated as it included patients still waiting at the end of the simulation.
5. histogram_wait_times.png: Histogram of the number of students per wait time.
6. table_maxwait_perhour_pernurses.csv: Maximum wait time as a function of the number of patients in the hour and the number of nurses working that hour.

References:

The following resources were used in building the model:
1. GitHub tutorial on simpy_helpers: https://github.com/bambielli/simpy_helpers/blob/master/Using_Simpy_Helpers_Package.ipynb
2. Video tutorial on simpy_helpers: https://www.youtube.com/watch?app=desktop&v=TALKZZV0TiU
3. GitHub CoPilot was used to figure out how to implement balking into the process function.








