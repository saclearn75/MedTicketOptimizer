from openai import OpenAI

patient_record_samples = []
with open ('samples.txt') as f: 
    for each in f: 
        # print (each.strip())
        patient_record_samples.append(each.strip())

# for i in range(3, 10): 
#     print (patient_record_samples[i])

