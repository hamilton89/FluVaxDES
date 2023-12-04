# FluVaxDES
Discrete Event Simulation of a flu vaccine clinic using Simpy

Problem: A university requires all affiliates to receive the flu vaccine and has clinics open on different days and campuses during the flu season. Clinic A is open four days and sees 800-1300 patients each day with four nurses administering vaccinations. Students have reported waiting over 30 minutes to get vaccinated at Clinic A. 

Methods: Using the Simpy library and simpy_helpers package in python, we simulate a day at Clinic A and record maximum wait times as a function of the number of patients visiting per hour and the number of nurses working per hour. Results indicate how many nurses are needed each hour in order to keep wait times under 30 minutes. Then we simulate the peak hour at Clinic A with the current number of nurses (4) and plot the number of patients arrived, balked, and vaccinated over the course of the the hour. 

Assumptions:
1. 
