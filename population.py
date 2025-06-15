import random
import datetime
from owlready2 import get_ontology

# Load the ontology
onto = get_ontology("out/healthcare_ontology.owl").load()

with onto:

    # Scenario 1: Chronic Disease Monitoring at Home
    patient1 = onto.Patient("Ahmed_ElMasri")
    patient1.hasPatientID = [1]
    patient1.hasFirstName = ["Ahmed"]
    patient1.hasFamilyName = ["ElMasri"]
    patient1.hasAge = [68]
    patient1.hasSex = [onto.Male()]
    patient1.hasBloodType = [onto.A_Positive()]
    patient1.hasMedicalHistory = [onto.Hypertension(), onto.Diabetes()]
    device1 = onto.SmartWatch("SmartWatch_Ahmed")
    device1.hasDeviceID = ["DEV001"]
    device1.hasBrand = ["FitPlus"]
    device1.hasModel = ["F1000"]
    device1.hasPrecision = [0.95]
    device1.hasSamplingRate = [5]
    device2 = onto.Glucometer("GlucoTrack_Ahmed")
    device2.hasDeviceID = ["DEV002"]
    device2.hasBrand = ["HealthTrack"]
    device2.hasModel = ["G200"]
    device2.hasPrecision = [0.92]
    device2.hasSamplingRate = [3]
    patient1.usesDevice = [device1, device2]

    for i in range(3):
        m = onto.Measurement(f"A1_Measurement_{i}")
        m.hasValue = [round(random.uniform(60, 140), 2)]
        m.hasUnit = ["bpm"]
        m.hasTimestamp = [datetime.datetime.now() - datetime.timedelta(hours=i * 6)]
        m.hasVitalSignType = [onto.HeartRate()]
        m.measuredBy = [device1]
        m.recordedFor = [patient1]

    actor1 = onto.GeneralPractitioner("Dr_Tariq")
    actor1.performsRole = [onto.RemoteCare()]
    structure1 = onto.TelemedicineCenter("RemoteCareCenter")
    actor1.worksIn = [structure1]
    patient1.treatedBy = [actor1]

    event1 = onto.Consultation("Consultation_Ahmed")
    event1.assignedTo = [patient1]
    care1 = onto.Curative("Care_Ahmed")
    event1.careType = [care1]
    care1.hasStartDate = [datetime.date.today() - datetime.timedelta(days=10)]
    care1.hasEndDate = [datetime.date.today()]
    care1.isEmergency = [False]
    care1.observedOutcome = ["Stable condition."]

    # Scenario 2: Emergency Hospitalization
    patient2 = onto.Patient("Youssef_Saidi")
    patient2.hasPatientID = [2]
    patient2.hasFirstName = ["Youssef"]
    patient2.hasFamilyName = ["Saidi"]
    patient2.hasAge = [50]
    patient2.hasSex = [onto.Male()]
    patient2.hasBloodType = [onto.B_Positive()]
    patient2.hasMedicalHistory = [onto.HeartDisease()]
    device3 = onto.BloodPressureMonitor("BPMonitor_Youssef")
    device3.hasDeviceID = ["DEV003"]
    device3.hasBrand = ["MediSense"]
    device3.hasModel = ["BP900"]
    device3.hasPrecision = [0.96]
    device3.hasSamplingRate = [1]
    patient2.usesDevice = [device3]

    m2 = onto.Measurement("Y2_BP_Critical")
    m2.hasValue = [180.5]
    m2.hasUnit = ["mmHg"]
    m2.hasTimestamp = [datetime.datetime.now()]
    m2.hasVitalSignType = [onto.BloodPressure()]
    m2.measuredBy = [device3]
    m2.recordedFor = [patient2]

    actor2 = onto.Specialist("Dr_Nour")
    actor2.performsRole = [onto.Intervention()]
    structure2 = onto.Hospital("CityHospital")
    actor2.worksIn = [structure2]
    structure2.hasService = [onto.ICU()]
    structure2.hasEquipment = [onto.Defibrillator()]
    structure2.numberOfBeds = [120]
    patient2.treatedBy = [actor2]

    event2 = onto.Hospitalization("Hospitalization_Youssef")
    event2.assignedTo = [patient2]
    care2 = onto.Curative("Care_Youssef")
    event2.careType = [care2]
    care2.hasStartDate = [datetime.date.today() - datetime.timedelta(days=5)]
    care2.hasEndDate = [datetime.date.today()]
    care2.isEmergency = [True]
    care2.observedOutcome = ["Stabilized, follow-up required."]

    # Scenario 3: Preventive Pediatric Visit
    patient3 = onto.Patient("Rami_Bakir")
    patient3.hasPatientID = [3]
    patient3.hasFirstName = ["Rami"]
    patient3.hasFamilyName = ["Bakir"]
    patient3.hasAge = [12]
    patient3.hasSex = [onto.Male()]
    patient3.hasBloodType = [onto.O_Negative()]
    device4 = onto.ConnectedThermometer("Thermo_Rami")
    device4.hasDeviceID = ["DEV004"]
    device4.hasBrand = ["ThermoPlus"]
    device4.hasModel = ["T100"]
    device4.hasPrecision = [0.93]
    device4.hasSamplingRate = [2]
    device5 = onto.SmartWatch("SmartWatch_Rami")
    device5.hasDeviceID = ["DEV005"]
    device5.hasBrand = ["KidHealth"]
    device5.hasModel = ["K200"]
    device5.hasPrecision = [0.95]
    device5.hasSamplingRate = [2]
    patient3.usesDevice = [device4, device5]

    m3 = onto.Measurement("R3_HeartRate")
    m3.hasValue = [75.2]
    m3.hasUnit = ["bpm"]
    m3.hasTimestamp = [datetime.datetime.now()]
    m3.hasVitalSignType = [onto.HeartRate()]
    m3.measuredBy = [device5]
    m3.recordedFor = [patient3]

    actor3 = onto.Nurse("Nurse_Aisha")
    actor3.performsRole = [onto.Monitoring()]
    structure3 = onto.Clinic("CityClinic")
    actor3.worksIn = [structure3]
    structure3.hasService = [onto.Emergency()]
    structure3.hasEquipment = [onto.Scanner()]
    structure3.numberOfBeds = [45]
    patient3.treatedBy = [actor3]

    event3 = onto.Consultation("Consultation_Rami")
    event3.assignedTo = [patient3]
    care3 = onto.Preventive("Care_Rami")
    event3.careType = [care3]
    care3.hasStartDate = [datetime.date.today()]
    care3.hasEndDate = [datetime.date.today()]
    care3.isEmergency = [False]
    care3.observedOutcome = ["Healthy, no issues."]
    
    # === Scenario 4: AI-Assisted Elderly Home Monitoring ===
    patient4 = onto.Patient("Samira_Haddad")
    patient4.hasPatientID = [4]
    patient4.hasFirstName = ["Samira"]
    patient4.hasFamilyName = ["Haddad"]
    patient4.hasAge = [85]
    patient4.hasSex = [onto.Female()]
    patient4.hasBloodType = [onto.AB_Negative()]
    patient4.hasMedicalHistory = [onto.Asthma(), onto.Hypertension()]

    device6 = onto.Oxymeter("Oxymeter_Samira")
    device6.hasDeviceID = ["DEV006"]
    device6.hasBrand = ["PulseCare"]
    device6.hasModel = ["OXY-85"]
    device6.hasPrecision = [0.94]
    device6.hasSamplingRate = [2]

    device7 = onto.SmartWatch("SmartWatch_Samira")
    device7.hasDeviceID = ["DEV007"]
    device7.hasBrand = ["ElderSafe"]
    device7.hasModel = ["ES-500"]
    device7.hasPrecision = [0.95]
    device7.hasSamplingRate = [3]

    patient4.usesDevice = [device6, device7]

    # Oxygen Measurement (abnormal spike)
    m4 = onto.Measurement("S4_OxygenAlert")
    m4.hasValue = [85.0]
    m4.hasUnit = ["%"]
    m4.hasTimestamp = [datetime.datetime.now()]
    m4.hasVitalSignType = [onto.OxygenLevel()]
    m4.measuredBy = [device6]
    m4.recordedFor = [patient4]

    actor4 = onto.AIAssistant("AI_Monitor_Samira")
    actor4.performsRole = [onto.Monitoring()]
    structure4 = onto.HomeCare("Samira_Home")
    actor4.worksIn = [structure4]
    patient4.treatedBy = [actor4]

    structure4.hasService = [onto.Emergency()]
    structure4.hasEquipment = [onto.Oxymeter()]
    structure4.numberOfBeds = [1]

    event4 = onto.Consultation("RemoteCheck_Samira")
    event4.assignedTo = [patient4]
    care4 = onto.Palliative("Care_Samira")
    event4.careType = [care4]
    care4.hasStartDate = [datetime.date.today() - datetime.timedelta(days=3)]
    care4.hasEndDate = [datetime.date.today()]
    care4.isEmergency = [False]
    care4.observedOutcome = ["Condition under watch."]

# Save the populated ontology
onto.save(file="out/healthcare_ontology_scenario.owl", format="rdfxml")
