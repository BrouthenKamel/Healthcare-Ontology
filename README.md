# 🏥 Healthcare Ontology – Semantic Modeling with Owlready2

This project provides a semantic ontology model for healthcare systems, designed using **Python** and **Owlready2**, and exportable to **OWL** for use in ontology editors like **Protégé**.

## 📘 Description

The ontology models core healthcare concepts including:

- Patients, diseases, and medical history
- Medical actors and their roles
- Devices and vital signs
- Healthcare structures and services
- Events such as hospitalization, consultation, etc.
- Vital measurements and device precision

The ontology supports reasoning, query execution, and semantic interoperability.


## 📂 Project Structure

```

ontology/
├── out/
│   ├── healthcare\_ontology.owl              # Defined ontology in OWL
│   └── healthcare\_ontology\_scenario.owl     # Populated ontology with instances
├── ontology.py       # Ontology structure and classes
├── population.py     # Instance population with realistic scenarios
├── requirements.txt  # Python dependencies
└── README.md

````

## 🧪 Example Scenarios

Four realistic scenarios are modeled:
1. **Chronic disease monitoring at home**
2. **Emergency hospitalization**
3. **Preventive pediatric visit**
4. **AI-assisted elderly home monitoring**


## 🚀 Getting Started

### 📦 Install dependencies
```bash
pip install -r requirements.txt
````

### ▶️ Run the ontology creation and population

```bash
python ontology.py
python population.py
```

Then, open `out/healthcare_ontology.owl` or `out/healthcare_ontology_scenario.owl` in **Protégé**.

## 🛠️ Tools Used

* 🐍 Python 3
* 🧠 [Owlready2](https://owlready2.readthedocs.io)
* 🦉 Protégé (for ontology visualization and reasoning)


## 👨‍💻 Author

- Kamel BROUTHEN
- Abdelaziz AKEB