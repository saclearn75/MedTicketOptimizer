from openai import OpenAI
import json

import tools.classifier as classifier
import tools.extractor as extractor 
import tools.recommendor as recommendor

patient_record_samples = []
with open ('samples.txt') as f: 
    for each in f: 
        patient_record_samples.append(each.strip())

# for i in range(3, 10): 
#     print (patient_record_samples[i])




if __name__ == "__main__":
    ticket = (
        "Patient attempted to walk unassisted, fell near bedside, "
        "and was later found to have received the wrong evening medication "
        "due to a charting error. Physician notified. Patient stable."
    )

    # json_classification = classifier.classify_ticket(ticket)
    # json_info =extractor.extract_info(ticket)

    # OUTPUT_FORMAT = f'''
    # -------------------------------------------------------------
    #     Ticket No: {i}

    #     Incident type: {json_classification["primary_category"]}
    #     Any other classifications: {', '.join(map(str, json_classification["secondary_categories"])) if json_classification["secondary_categories"] else 'None recorded'}
    #     Severity: {json_classification["severity"]}

    #     Brief summary: 
    #         {json_info["event_summary"]}
        
    #     Immediate actions taken:
    #         {', '.join(map(str, json_info["actions_taken"])) if json_info["actions_taken"] else 'None recorded'}

    #     Patient injury / current state: 
    #         {json_info["patient_harm"]}
        
    #     People notified: 
    #         {', '.join(map(str,json_info["people_involved"])) if json_info["people_involved"] else 'None'}

    #     Any immediate uncertainties / Risks: 
    #         {', '.join(map(str, json_info["uncertainties"])) if json_info["uncertainties"] else 'None recorded'}
    
    # -------------------------------------------------------------
    
    # '''

    
    # print (f'\n {json_classification=} \n\n')
    # print (f'{json_info=} \n\n')

    # print(OUTPUT_FORMAT)

    for i in range (2,5):
        json_classification = classifier.classify_ticket(patient_record_samples[i])
        json_info =extractor.extract_info(patient_record_samples[i])
        json_next_steps =recommendor.recommend_next_steps(json_classification, json_info)

        print (f"\t Ticket: {patient_record_samples[i]}")

        OUTPUT_FORMAT = f'''
        -------------------------------------------------------------
            Incident Ticket: {i}

            Primary classification: {json_classification["primary_category"]}
            Secondary classifications: {', '.join(map(str, json_classification["secondary_categories"])) if json_classification["secondary_categories"] else 'None recorded'}
            Severity: {json_classification["severity"]}

            Brief summary: 
                {json_info["event_summary"]}
            
            Immediate actions taken:
                {', '.join(map(str, json_info["actions_taken"])) if json_info["actions_taken"] else 'None recorded'}

            Patient condition: 
                {json_info["patient_harm"]}
            
            People notified: 
                {', '.join(map(str,json_info["people_involved"])) if json_info["people_involved"] else 'None'}

            Open risks or uncertainties: 
                {', '.join(map(str, json_info["uncertainties"])) if json_info["uncertainties"] else 'None recorded'}
        
            Next Steps: 
                {', '.join(map(str, json_next_steps["recommended_actions"])) if json_next_steps["recommended_actions"] else 'None'}

            Priority: 
                {json_next_steps["priority"]}

            Escalation Target: 
                {json_next_steps["escalation_target"]}

            Rationale
                {json_next_steps["rationale"]}
        -------------------------------------------------------------
     
        '''
        # print (f'\n {json_classification=} \n\n')
        # print (f'{json_info=} \n\n')
        print(OUTPUT_FORMAT)

