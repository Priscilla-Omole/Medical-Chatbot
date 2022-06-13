#Import Libraries
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import numpy as np
import itertools
import pickle
import model # load model.py


app = Flask(__name__)
# render htmp page
@app.route('/')
def home():
    return render_template('multiple.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    #arr = ['skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze'];
    input_features = [x for x in request.form.values()]
    #s1 = input_features[0]
    
    # printing result 
    #print ("List with only nth tuple element (i.e names) : " + str(res)) 

    #s1 = request.form
    #print(s1['Symptoms'][0])
    
    #print(s1['Symptoms'][1])
    s1 =  input_features[0]
    s2 =  input_features[1]
    s3 =  input_features[2]
    s4 =  input_features[3]
    s5 =  input_features[4] 
    #choices = [(str(x), str(x)) for  x in arr]
    # test if value was passed in (e.g. GET method), default value is 1
    #selected = request.args.get('choice')
    # application 'state' variable with default value and test
   # state = {'choice': selected}
    #s1="No"    
    # predict the disease by calling model.py
    
    predicted_disease = model.predict_disease([s1,s2,s3,s4,s5])       
   # multiselect = request.form.getlist('select')
    print(predicted_disease)
    Dict = {'Fungal infection':'A fungal infection, also called mycosis, is a skin disease caused by a fungus. Home remedy: use an antibacterial soap that will disinfect your body and kill the fungal infection in its early stages. The drying effect of the soap will also help your condition.',
     'Allergy':'A condition in which the immune system reacts abnormally to a foreign substance. Home remedy: Apply calamine lotion and cover the area with bandage. Use Ice also to compressed the itching and redness.', 
     'GERD':'A digestive disorder that affects the ring of muscle between your esophagus and your stomach. Home remedy: Eat smaller meals more frequently rather than bigger meals less often, eat meals in a relaxed environment.', 
     'Chronic cholestasis':'A decrease in bile flow due to impaired secretion by hepatocytes or to obstruction of bile flow through intra-or extrahepatic bile ducts. Home remedy: Drink alot of water at several intervals of the day.',
       'Drug Reaction':'A change in the way a drug acts in the body when taken with certain other drugs, foods, or supplements or when taken while you have certain medical conditions. Home remedy: Withdrawal of the drug should help.', 
       'Peptic ulcer diseae':'A sore that develops on the lining of the oesophagus, stomach or small intestine. Home remedy: Avoid fatty and spicy food, Consume probiotic food and limite alcohol.', 
       'AIDS':'AIDS (acquired immune deficiency syndrome) is the name used to describe a number of potentially life-threatening infections and illnesses that happen when your immune system has been severely damaged by the HIV virus. Urgent!: Visit the hospital regarding this case.', 
       'Diabetes ':'A chronic, metabolic disease characterized by elevated levels of blood glucose (or blood sugar). Home remedy: By taking fluids like aloe vera, karela, amla, and mango juice, all these are helpful for your body. Also, doing regular exercise and maintaining your stress to live a healthy lifestyle. ',
       'Gastroenteritis':'Gastroenteritis is an inflammation of the digestive tract, particularly the stomach, and large and small intestines. Viral and bacterial gastroenteritis are intestinal infections associated with symptoms of diarrhea , abdominal cramps, nausea , and vomiting. Home remedy: Drink enough fluids to stay hydrated and get plenty of rest.', 
       'Bronchial Asthma':'A condition in which a persons airways become inflamed, narrow and swell and produce extra mucus, which makes it difficult to breathe. Home remedy: There are no home remedies for an asthma attack, kindly visit a doctor.', 
       'Hypertension ':'Hypertension (HTN or HT), also known as high blood pressure (HBP), is a long-term medical condition in which the blood pressure in the arteries is persistently elevated. High blood pressure typically does not cause symptoms. Home remedy: Eating a healthier diet with less salt, exercising regularly and taking medication can help lower blood pressure.', 
       'Migraine':'A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. Its often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Migraine attacks can last for hours to days, and the pain can be so severe that it interferes with your daily activities. Home remedy: Preventive and pain-relieving medication can help manage migraine headaches.',
       'Cervical spondylosis':'A general term for age-related wear and tear affecting the spinal disks in your neck. Home remedy: There are no home remedies for this, kindly visit a doctor.', 
       'Paralysis (brain hemorrhage)':'An emergency condition in which a ruptured blood vessel causes bleeding inside the brain. Home remedy: Emergency treatment is required for cerebral haemorrhage. It usually involves medication and close monitoring in an intensive care unit. In rare cases, surgery may be required to relieve pressure around the brain.', 
       'Jaundice':'A condition in which the skin, whites of the eyes and mucous membranes turn yellow because of a high level of bilirubin, a yellow-orange bile pigment. Home remedy: Place the child in a well-lit window for 10 minutes twice a day',
       'Malaria':'A serious and sometimes fatal disease caused by a parasite that commonly infects a certain type of mosquito which feeds on humans. Home remedy: Turmeric can help in flushing out harmful toxins from the body which build up because of plasmodium infection', 
       'Chicken pox':'A highly contagious viral infection causing an itchy, blister-like rash on the skin. Home remedy: Apply calamine lotion.', 
       'Dengue':'A viral infection transmitted to humans through the bite of infected mosquitoes. Home remedy: Drink a lot of coconut water and vegetable juice.', 
       'Typhoid':'An acute illness characterized by fever caused by infection with the bacterium Salmonella typhi. Typhoid fever has an insidious onset, with fever, headache, constipation, malaise, chills, and muscle pain. Diarrhea is uncommon, and vomiting is not usually severe. Home remedy: Treatment includes antibiotics and increased fluids intake.', 
       'hepatitis A':'A form of viral hepatitis transmitted in food, causing fever and jaundice. Home remedy: The condition clears up on its own in one or two months. Rest and adequate hydration can help.',
       'Hepatitis B':'A severe form of viral hepatitis transmitted in infected blood, causing fever, debility, and jaundice. Home remedy: The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant.', 
       'Hepatitis C':'A form of viral hepatitis transmitted in infected blood, causing chronic liver disease. It was formerly called non-A, non-B hepatitis. Home remedy: Take milk thistle and probiotics, newer medicines can eradicate the virus now.', 
       'Hepatitis D':'A liver infection you can get if you have hepatitis B. Home remedy: There are no known treatments for acute or chronic hepatitis D.', 
       'Hepatitis E':'An inflammation of the liver caused by infection with the hepatitis E virus. Home remedy: Hepatitis E usually resolves on its own within four to six weeks. Treatment focuses on supportive care, rehydration and rest',
       'Alcoholic hepatitis':'Liver inflammation caused by drinking too much alcohol. Home remedy: Take a lot of proteins and stop drinking alcohol, steroid drugs can help reduce liver inflammation.', 
       'Tuberculosis':'Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria. Tuberculosis generally affects the lungs, but can also affect other parts of the body. Most infections show no symptoms, in which case it is known as latent tuberculosis. Home remedy: Eat smaller meals several times a day instead of a few large ones and drink high-calorie protein shakes or other nutritious drinks with garlic.', 
       'Common Cold':'The common cold is a viral infection of your nose and throat (upper respiratory tract). Its usually harmless, although it might not feel that way. Many types of viruses can cause a common cold. Home remedy: Most people recover on their own within two weeks. Staying hydrated, resting and avoiding cold atmosphere will help.', 
       'Pneumonia':'Pneumonia is an infection in one or both lungs. Bacteria, viruses, and fungi cause it. The infection causes inflammation in the air sacs in your lungs, which are called alveoli. The alveoli fill with fluid or pus, making it difficult to breathe. Home remedy: Antibiotics can treat many forms of pneumonia',
       'Dimorphic hemmorhoids(piles)':'Hemorrhoids (piles) are swollen veins that form inside the rectum or outside the anus. Home remedy: They often go away without treatment, drinking water aids.', 
       'Heart attack':'The death of heart muscle due to the loss of blood supply. The loss of blood supply is usually caused by a complete blockage of a coronary artery, one of the arteries that supplies blood to the heart muscle. Home remedy: Call your doctor immediately, drink almond milk and eat alot of almonds.', 
       'Varicose veins':'Affected by a condition causing the swelling and tortuous lengthening of veins, most often in the legs. Home remedy: Treatment involves compression stockings, exercise or procedures to close or remove the veins.',
       'Hypothyroidism':'Abnormally low activity of the thyroid gland, resulting in slowing of growth and mental development in children and metabolic changes in adults. Home remedy: Taking a vitamin B-12 supplement may help you repair some of the damage hypothyroidism caused. Vitamin B-12 can help with the tiredness thyroid disease can cause.', 
       'Hyperthyroidism':'An overactivity of the thyroid gland, resulting in a rapid heartbeat and an increased rate of metabolism. Home remedy: Supplements like iodine, probiotics, and curcumin can do wonders for your thyroid. Reduce daily stress and get enough sleep.', 
       'Hypoglycemia':'A deficiency of glucose in the bloodstream. Home remedy: Consuming high-sugar foods or drinks, such as orange juice or regular fizzy drinks, can treat this condition.',
       'Osteoarthristis':'Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide. It occurs when the protective cartilage that cushions the ends of your bones wears down over time. Home remedy: Hot compresses are helpful for joint stiffness, and cold compresses are best for joint pain.', 
       'Arthritis':'A painful inflammation and stiffness of the joints. Home remedy: Try an anti-inflammatory, plant-based diet. Engage in physical activities and try heat/ice therapy.',
       '(vertigo) Paroymsal  Positional Vertigo':'A sensation of whirling and loss of balance, associated particularly with looking down from a great height, or caused by disease affecting the inner ear or the vestibular nerve; giddiness. Home remedy: Sitting on the edge of a bed and turning the head 45 degrees to the left, lying down quickly and facing head up on the bed at a 45-degree angle.', 
       'Acne':'Acne vulgaris is the formation of comedones, papules, pustules, nodules, and/or cysts as a result of obstruction and inflammation of pilosebaceous units (hair follicles and their accompanying sebaceous gland). Acne develops on the face and upper trunk. It most often affects adolescents. Home remedy: Conventional acne treatments, like salicylic acid, niacinamide, or benzoyl peroxide, are proven to be the most effective acne solutions.',
       'Urinary tract infection':'An infection of the kidney, ureter, bladder, or urethra. Abbreviated UTI. Not everyone with a UTI has symptoms, but common symptoms include a frequent urge to urinate and pain or burning when urinating. Home remedy: Drinking enough water can help prevent and treat UTIs. Also taking antibiotics and penicillin can help in fast treatment.', 
       'Psoriasis':'A skin disease marked by red, itchy, scaly patches. Home remedy: Topical ointments, light therapy and medication can offer relief.', 
       'Impetigo':'A contagious bacterial skin infection forming pustules and yellow crusty sores. Home remedy: The use of raw honey is effective in stopping it. Antibiotics shorten the infection and can help prevent spread to others.'}
    def get_values(k):
        for key, value in Dict.items():
             if k == key:
                 return value
     
        return "No Recommendations"
    medicine = get_values(predicted_disease[0])
    # render the html page and show the output
    return render_template('multiple.html',predicted = 'Predicted Disease : {}'.format((predicted_disease[0])),medicine = 'About Disease : {}'.format(medicine))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
    
if __name__ == "__main__":
    app.run()
    app.config["CACHE_TYPE"] = "null"
    