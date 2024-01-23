# FluVaxDES
Optimizing Flu Clinic Staffing Schedule

Final project for the course Operations Research at the Whiting School of Engineering, Johns Hopkins University

Problem description: A university requires all affiliates to receive the flu vaccine and has clinics open on different days and campuses during the flu season. Clinic A is open four days and sees 800-1300 patients per day and has four nurses administering vaccinations each day. Students have reported waiting over 30 minutes to get vaccinated at this clinic. We want to determine how many nurses are needed each hour to keep wait times under 10 minutes.

Assumptions:

1. The clinic is open 9am - 5pm (8 hours) and a total of 1300 patients arrive during that day.
2. Patients arrive at different times throughout the day with the majority arriving between 2-3pm (hour 5). To approximate the arrival schedule, we assume 50 patients arrive in hour 1, 100 in hour 2, 150 in hour 3, 200 in hour 4, 300 in hour 5, 250 in hour 6, 150 in hour 7, and 100 in hour 8.
3. Upon arrival, patients will balk (leave without getting vaccinated) if the queue size is over a certain balk tolerance.
4. It takes approximately 2 minutes to get vaccinated.
5. We assume patients arrive at roughly even intervals over the hour. For example, in an hour with 300 patients, a patient will arrive roughly every 0.2 minutes. This is because simy_helpers uses the mean time between arrivals to schedule when entities enter the simulation (see Methods).

Methods: We use the Simpy library and simpy_helpers package in python to build a Discrete Event Simulation (DES) model. First, we build the base model without any stochasticity or balking. Second, we introduce stochasticity by assigning exponential distributions around the balk tolerance, mean time between arrivals, and mean service time. Next, we run the simulation for different scenarios:
1. Scenario 1: Slow hour with 100 patients, 4 nurses, service time of 2 minutes, and balk tolerance of 30
2. Scenario 2: Busy hour with 300 patients, 4 nurses, service time of 2 minutes, and balk tolerance of 30
3. Scenario 3: Busy hour with 300 patients, 4 nurses, service time of 2 minutes, and balk tolerance of 50
4. Scenario 4: Busy hour with 300 patients, 4 nurses, service time of 6 minutes, and balk tolerance of 30

Finally, we run the simulation for 8 hours in the day and record max wait times and pateints vaccinated as a function of the number of patients arriving in that hour and the number of nurses working that hour. For these runs, we assume a mean balk tolerance of 30 and a mean service time of 2 minutes.

Workflow:

Run FluVaxDES.py. This file contains all code with detailed comments and is separated into the following sections: 
1. Simpy classes: Define classes for Entity, Resource, and Source (see Reference 1 below for descriptions)
2. Functions: Define functions for assigning parameters and generating tables and figures.
3. Base model: Run the model without any stochasticity or balking.
4. Simpy classes with stochasticity: Redefine Simpy classes to include distributions around key parameters.
5. Scenarios: Run the model with stochasticity for scenarios 1-4
6. Loop through hours in a day: Loop through the number of patients each hour (Assumption 2) and record maximum wait time and patients vaccinated as a function of the number of nurses working per hour. 

Outputs:

The following tables and figures are exported for the base model, base model with stochasticity, and the four scenarios. A table with results looping over each our of the day is also exported.
1. [scenario]_table_results.csv: Results for a simulation of the peak hour with 300 patients and 4 nurses.
2. [scenario]_graph_queue_size.png: Line graph of queue size over time.
3. [scenario]_graph_wait_times.png: Line graph of max wait time over time.
4. [scenario]_graph_arrived_balked_vaccinated.png: Line graph of arrived (blue), balked (red), and vaccinated (green) over time. 
5. [scenario]_histogram_wait_times.png: Histogram of the number of students per wait time.
6. table_maxwait_perhour_pernurses.csv: Maximum wait time each hour as a function of the number of patients in the hour and the number of nurses working that hour.
7. table_served_perhour_pernurses.csv: Patients vaccinated each hour as a function of the number of patients in the hour and the number of nurses working that hour.

References:

The following resources were used in building the model:
1. GitHub tutorial on simpy_helpers: https://github.com/bambielli/simpy_helpers/blob/master/Using_Simpy_Helpers_Package.ipynb
2. Video tutorial on simpy_helpers: https://www.youtube.com/watch?app=desktop&v=TALKZZV0TiU
3. GitHub CoPilot was used to figure out how to implement balking into the process function.


