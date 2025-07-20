# 📊 Streamlit Data Analysis App with Conda Environment

This project sets up a simple **Streamlit** app for data analysis using a **Conda virtual environment**. It also includes installation of essential Python libraries like `pandas`, `matplotlib`, `numpy`, and more.

## 🧰 Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Python 3.7 or higher

##  Setup Instructions

### 1️. Create a Conda Environment

Create a new virtual environment named `streamlit_env` with Python:

```bash
conda create --name streamlit_env python=3.10
```

### 2️. Activate the Environment

```bash
conda activate streamlit_env
```

### 3️. Install Streamlit

```bash
pip install streamlit
```

You can test it by running:

```bash
streamlit hello
```

### 4. Install External Libraries

To perform data analysis, install the following packages:

```bash
pip install pandas matplotlib numpy seaborn scikit-learn
```

Or install them all together:

```bash
pip install streamlit pandas matplotlib numpy seaborn scikit-learn
```

### 5. Run the app with

```bash
streamlit run app.py
```

## Contact

For questions or support, contact: [jamil138.amin@gmail.com]


