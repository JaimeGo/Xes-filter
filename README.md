# Xes-filter

Custom filters for data in the 2018 Business Process Intelligence Challenge. 

The Xes file uses the Opyenxes module for filtering the log, while the Csv file parses data obtained from the original Xes log file through Disco (https://fluxicon.com/disco) with the csv module in Python. 

The data is filtered so that events with the same doctype and subprocess attribute are grouped together, if they are consecutive.
