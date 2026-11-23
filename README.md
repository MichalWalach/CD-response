# Predicting Patient Response to Infliximab Therapy in IBD

## Overview

**Infliximab** is a monoclonal antibody targeting TNF-$\alpha$ widely used in the treatment of Inflammatory Bowel Disease (IBD), specifically **Crohn’s disease (CD)** and **Ulcerative Colitis (UC)**. Despite its clinical effectiveness and broad adoption, a significant proportion of patients either fail to respond to the initial therapy (primary non-response) or lose responsiveness over time (secondary loss of response).

Predicting treatment outcomes prior to therapy initiation can help clinicians personalize treatment plans, avoid unnecessary drug exposure, and reduce healthcare costs.

## Objective

The goal of this project is to develop a machine learning model capable of predicting whether an IBD patient will **respond** or **not respond** to Infliximab treatment based on intestinal mucosal gene expression profiles.

## Datasets

This project utilizes publicly available microarray gene expression datasets from the **Gene Expression Omnibus (GEO)** repository:

| Accession ID | Platform / Data Type | Source Link |
| :--- | :--- | :--- |
| **GSE73661** | Microarray gene expression | [View on NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE73661) |
| **GSE23597** | Microarray gene expression | [View on NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE23597) |
| **GSE16879** | Microarray gene expression | [View on NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16879) |
| **GSE52746** | Microarray gene expression | [View on NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52746) |

## Planned Workflow

1. **Data Acquisition & Parsing:** Download expression matrices and clinical metadata (responder vs. non-responder labels) from GEO.
2. **Preprocessing & Integration:** Map probes to gene symbols, normalize expression values, and address batch effects across the four cohorts.
3. **Feature Selection:** Reduce high-dimensional microarray features to identify the most informative genes/biomarkers.
4. **Model Training & Hyperparameter Tuning:** Train and optimize classification pipelines using cross-validation.
5. **Evaluation & Interpretability:** Assess generalization performance (e.g., ROC-AUC, precision, recall, confusion matrix) and analyze key predictive genes.

## Project Structure

```text
├── data/               # Raw and processed GEO datasets (ignored in git)
├── notebooks/          # Exploratory data analysis and modeling notebooks
├── src/                # Reusable Python modules for preprocessing and modeling
├── results/            # Generated figures, metrics, and evaluation reports
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites

* Python 3.10+
* `pip` or `conda` for package management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## License

This project is created for educational/research purposes. Add your preferred license (e.g., MIT) here.