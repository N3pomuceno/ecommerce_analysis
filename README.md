# Project sql_project

## Description

Projeto dedicado para prática e análises com SQL.

## Setting Up the Virtual Environment

Follow these steps to create the virtual environment, activate it, and install the project dependencies:

```bash
# Create the virtual environment:
poetry install

# If you don't have the poetry plugin installed, run:
poetry self add poetry-plugin-shell

# Enter the project's virtual environment:
poetry shell

# Start Jupyter Notebook or JupyterLab (if preferred):
jupyter notebook # or jupyter lab

# Alternatively, run it directly with poetry:
poetry run jupyter lab
```

## Using the Database

To use the database, Docker Desktop must be installed and running. Once set up, start the database with:

```bash
docker-compose up -d
```

After this, the database will be running and accessible through tools like DBeaver or TablePlus using the credentials stored in `.database_env`.

To stop the database, run:

```bash
docker-compose down
```

Additionally, the project includes the Data Build Tool ([DBT](https://docs.getdbt.com/docs/introduction)), which facilitates data transformation, validation, and efficiency monitoring in the database.

## Initializing Git Repository

By default, Git is not initialized. If you want to link the project to a repository, follow these steps:

```bash
# Initialize the repository
git init

# Add a remote repository
git remote add origin <your_repo_https_or_ssh_link>

# Push the main branch to the remote repository
git push origin main
```

## Project Structure

The project is structured to streamline data science workflows. Below is an overview of the main directories:

```
sql_project
├── README.md                # Project overview and setup instructions
├── data                     # Directory for dataset storage
│   ├── processed            # Processed datasets
│   ├── raw                  # Raw datasets
│   └── summary.json         # Summary of data
├── docker-compose.yml       # Configuration for containerized services
├── documentation            # Project documentation and task tracking
│   ├── documentation.md     # Project goals and guidelines
│   └── todo.md              # Task tracking file
├── logs                     # Directory for storing log files
├── pyproject.toml           # Dependency management and project metadata
├── sql                      # SQL-related files
│   ├── queries              # SQL queries for data extraction and analysis
│   └── schemas              # Database schema definitions
├── src                      # Source code for the project
│   ├── __init__.py          # Package initialization
│   ├── eda_util.py          # Utility functions for EDA
│   ├── exception.py         # Custom exception handling
│   ├── logger.py            # Logging utility for debugging
│   └── util.py              # General utility functions
└── tests                    # Directory for unit and integration tests
```


I can't emphasize enough the impact of [Pedro Almeida](https://github.com/allmeidaapedro)'s work, which greatly influenced the structure of the `src` folder through his [project](https://github.com/allmeidaapedro/Churn-Prediction-Credit-Card). Additionally, the idea of documenting model results follows an established [standard](https://arxiv.org/pdf/1810.03993), which particularly caught my attention.  



## Documentation and Planning

For better alignment among team members, a repository will include two markdown files:

- `documentation.md`: Defines project goals and guidelines.
- `todo.md`: Tracks completed, ongoing, and upcoming tasks.

## Best Practices

- Always activate the virtual environment before working on the project to ensure correct dependencies.
- Keep `pyproject.toml` or `requirements.txt` updated with necessary dependencies.
- Use Git for version control and commit regularly to track progress.

