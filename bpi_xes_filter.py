from opyenxes.model.XLog import XLog
from opyenxes.data_in.XUniversalParser import XUniversalParser
from opyenxes.classification.XEventAttributeClassifier import XEventAttributeClassifier
from opyenxes.out.XesXmlSerializer import XesXmlSerializer
from sklearn.cluster import KMeans
from opyenxes.factory.XFactory import XFactory
import random



if __name__ == '__main__':
    path = "input_log.xes"

    
    with open(path) as log_file:
        logs = XUniversalParser().parse(log_file)  
       	
    
    classifier_doctype = XEventAttributeClassifier("doctype", ["doctype"])
    classifier_subprocess = XEventAttributeClassifier("subprocess", ["subprocess"])

    

    new_log=XFactory.create_log()

    for log in logs:
    	
    	random_list_of_traces=random.sample(log,5)

    	for trace in random_list_of_traces:
    		list_trace=[]
    		new_trace=XFactory.create_trace()
    		for event in trace:
    			
    			doctype= classifier_doctype.get_class_identity(event)
    			subprocess = classifier_subprocess.get_class_identity(event)

    			if len(list_trace)!=0:
    			    if list_trace[-1][0]==doctype and list_trace[-1][1]==subprocess:
    				    pass
    				
    			    else:
    				    
    				    
    				    new_trace.append(event)
    			else:
    				new_trace.append(event)

    			list_trace.append([doctype,subprocess])
    			

    		new_log.append(new_trace)




 	

    with open("output_log.xes", "w") as file:
    	XesXmlSerializer().serialize(new_log, file)





