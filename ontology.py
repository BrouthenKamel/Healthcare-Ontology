from owlready2 import get_ontology, Thing, DataProperty, ObjectProperty, datetime

# Create a new ontology with a specific IRI
onto = get_ontology("http://brouthen-akeb.esi.dz/healthcare_ontology.owl")

with onto:

    # === Core Concept: Patient ===
    class Patient(Thing):
        """Represents an individual receiving medical care in the system."""
        pass

    # === Enumerations: Sex ===
    class Sex(Thing):
        """Enumeration for patient biological sex."""
        pass

    class Male(Sex):
        """Male sex."""
        pass

    class Female(Sex):
        """Female sex."""
        pass

    # === Enumerations: Blood Types ===
    class BloodType(Thing):
        """Enumeration for patient blood types."""
        pass

    class A_Positive(BloodType): pass
    class A_Negative(BloodType): pass
    class B_Positive(BloodType): pass
    class B_Negative(BloodType): pass
    class AB_Positive(BloodType): pass
    class AB_Negative(BloodType): pass
    class O_Positive(BloodType): pass
    class O_Negative(BloodType): pass

    # === Disease Categories (for medical history) ===
    class Disease(Thing):
        """Class representing a known disease used in medical history records."""
        pass

    class Diabetes(Disease): pass
    class Hypertension(Disease): pass
    class Asthma(Disease): pass
    class HeartDisease(Disease): pass
    class Cancer(Disease): pass

    # === Patient Data Properties ===
    class hasPatientID(Patient >> int, DataProperty):
        """Unique identifier for the patient."""
        pass

    class hasFirstName(Patient >> str, DataProperty):
        """Patient's first name."""
        pass

    class hasFamilyName(Patient >> str, DataProperty):
        """Patient's last name."""
        pass

    class hasAge(Patient >> int, DataProperty):
        """Patient's age in years."""
        pass

    # === Patient Object Properties ===
    class hasSex(Patient >> Sex, ObjectProperty):
        """Biological sex of the patient."""
        pass

    class hasBloodType(Patient >> BloodType, ObjectProperty):
        """Blood type of the patient."""
        pass

    class hasMedicalHistory(Patient >> Disease, ObjectProperty):
        """Known medical history or diagnosed diseases for the patient."""
        pass

    # === Vital Signs (as categories, not actual values) ===
    class VitalSign(Thing):
        """Represents a type of vital sign measured for a patient."""
        pass

    class HeartRate(VitalSign): pass
    class Temperature(VitalSign): pass
    class BloodPressure(VitalSign): pass
    class GlucoseLevel(VitalSign): pass
    class OxygenLevel(VitalSign): pass

    # === Medical Personnel ===
    class MedicalActor(Thing):
        """Represents any medical professional or system agent."""
        pass

    class GeneralPractitioner(MedicalActor): pass
    class Specialist(MedicalActor): pass
    class Nurse(MedicalActor): pass
    class CareAssistant(MedicalActor): pass
    class AIAssistant(MedicalActor): pass

    # === Roles performed by medical actors ===
    class MedicalRole(Thing):
        """Represents a functional role in the healthcare process."""
        pass

    class Diagnosis(MedicalRole): pass
    class Monitoring(MedicalRole): pass
    class Intervention(MedicalRole): pass
    class RemoteCare(MedicalRole): pass

    # === Medical Devices for Vital Monitoring ===
    class MedicalDevice(Thing):
        """Electronic or smart device used to collect patient vital data."""
        pass

    class SmartWatch(MedicalDevice): pass
    class Oxymeter(MedicalDevice): pass
    class BloodPressureMonitor(MedicalDevice): pass
    class ConnectedThermometer(MedicalDevice): pass
    class Glucometer(MedicalDevice): pass

    # === Medical Device Properties ===
    class hasDeviceID(MedicalDevice >> str, DataProperty):
        """Unique ID assigned to the device."""
        pass

    class hasBrand(MedicalDevice >> str, DataProperty):
        """Brand or manufacturer of the device."""
        pass

    class hasModel(MedicalDevice >> str, DataProperty):
        """Model number or name of the device."""
        pass

    class hasPrecision(MedicalDevice >> float, DataProperty):
        """Precision level of the device measurements."""
        pass

    class hasSamplingRate(MedicalDevice >> int, DataProperty):
        """Sampling rate of the device (in Hz or samples/sec)."""
        pass

    # === Healthcare Facilities ===
    class CareStructure(Thing):
        """Location or facility where care is delivered."""
        pass

    class Hospital(CareStructure): pass
    class Clinic(CareStructure): pass
    class TelemedicineCenter(CareStructure): pass
    class HomeCare(CareStructure): pass

    # === Services & Equipment ===
    class MedicalService(Thing):
        """Type of healthcare service provided by a care structure."""
        pass

    class Emergency(MedicalService): pass
    class Surgery(MedicalService): pass
    class ICU(MedicalService): pass

    class MedicalEquipment(Thing):
        """Medical machines or hardware used in treatment or diagnostics."""
        pass

    class Ventilator(MedicalEquipment): pass
    class Defibrillator(MedicalEquipment): pass
    class Scanner(MedicalEquipment): pass

    class numberOfBeds(CareStructure >> int, DataProperty):
        """Number of patient beds available in the facility."""
        pass

    # === Medical Events (Patient lifecycle actions) ===
    class MedicalEvent(Thing):
        """Any event representing a healthcare action involving a patient."""
        pass

    class Admission(MedicalEvent): pass
    class Consultation(MedicalEvent): pass
    class Hospitalization(MedicalEvent): pass
    class Intervention(MedicalEvent): pass
    class Discharge(MedicalEvent): pass

    # === Types of Medical Care ===
    class MedicalCare(Thing):
        """Classification of healthcare based on purpose and goal."""
        pass

    class Preventive(MedicalCare): pass
    class Curative(MedicalCare): pass
    class Palliative(MedicalCare): pass

    # === Medical Care Properties ===
    class hasStartDate(MedicalCare >> datetime.date, DataProperty):
        """Start date of a medical treatment or intervention."""
        pass

    class hasEndDate(MedicalCare >> datetime.date, DataProperty):
        """End date of a medical treatment or intervention."""
        pass

    class isEmergency(MedicalCare >> bool, DataProperty):
        """True if the care is urgent or emergency-based."""
        pass

    class observedOutcome(MedicalCare >> str, DataProperty):
        """Observed result of the care (e.g. recovery, transfer)."""
        pass

    # === Measurement of Vital Signs (actual values captured) ===
    class Measurement(Thing):
        """An instance of a recorded vital sign with its value, time, and device."""
        pass

    class hasValue(Measurement >> float, DataProperty):
        """Numerical value of the vital sign recorded."""
        pass

    class hasUnit(Measurement >> str, DataProperty):
        """Measurement unit (e.g., bpm, °C, mmHg)."""
        pass

    class hasTimestamp(Measurement >> datetime.datetime, DataProperty):
        """Time when the measurement was taken."""
        pass

    class hasVitalSignType(Measurement >> VitalSign, ObjectProperty):
        """The type of vital sign (e.g., heart rate, blood pressure) being recorded."""
        pass

    class measuredBy(Measurement >> MedicalDevice, ObjectProperty):
        """The medical device that performed the measurement."""
        pass

    class recordedFor(Measurement >> Patient, ObjectProperty):
        """The patient for whom the measurement was taken."""
        pass

    # === General Object Properties: Semantic Links Across Core Concepts ===

    # --- Patient-Centric ---
    class usesDevice(Patient >> MedicalDevice, ObjectProperty):
        """Links a patient to a medical device they are using or assigned to."""
        pass

    class treatedBy(Patient >> MedicalActor, ObjectProperty):
        """Specifies the medical actor responsible for treating a patient."""
        pass

    # --- Medical Event Related ---
    class careType(MedicalEvent >> MedicalCare, ObjectProperty):
        """Links a medical event to its type of care (e.g., preventive)."""
        pass

    class assignedTo(MedicalEvent >> Patient, ObjectProperty):
        """Assigns a medical event to a specific patient."""
        pass

    # --- Role Assignment ---
    class performsRole(MedicalActor >> MedicalRole, ObjectProperty):
        """Defines which role (e.g., diagnosis) a medical actor performs."""
        pass

    class worksIn(MedicalActor >> CareStructure, ObjectProperty):
        """Specifies the facility where a medical actor works."""
        pass

    # --- Facility Capabilities ---
    class hasService(CareStructure >> MedicalService, ObjectProperty):
        """Lists services offered by a care facility."""
        pass

    class hasEquipment(CareStructure >> MedicalEquipment, ObjectProperty):
        """Indicates what equipment a facility contains."""
        pass

# Save the structured ontology to OWL file
onto.save(file="out/healthcare_ontology.owl", format="rdfxml")
