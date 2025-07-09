import re

from backend.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_number': self.get_field('patient_number'),
            'hepatitis_vaccinated':self.get_field('hepatitis_vaccinated'),
            'medical_problems': self.get_field('medical_problems')
        }

    def get_field(self,field_name):
        pattern_dict ={
            'patient_name':{'pattern': r'Patient\s+Information.*([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4}','flags':re.DOTALL},
            'patient_number': {'pattern': r'(\(\d{3}\) \d{3}\-\d{4})', 'flags': 0},
            'hepatitis_vaccinated': {'pattern': r'Hepatitis.*?(Yes|No)','flags':re.DOTALL },
            'medical_problems': {'pattern': r'Problems.*\s*\n+\s*(.+)', 'flags':0},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text,pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()

if __name__ == '__main__':
    document_text = '''17/12/2020

Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 . Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States ght.
170

In Case of Emergency
meee

Joe Lucas 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone . United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles:

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

_ Yes

List any Medical Problems (asthma, seizures, headaches):
N/A'''

    pp = PatientDetailsParser(document_text)
    print(pp.parse())
