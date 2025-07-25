# Project sql_project

## Description

Project focused on practices for SQL using Python and Docker. The main idea is to answer some questions about a e-commerce db, and see the difference between using raw SQL, SQLAlchemy and the DBT tool, were I can get more experience in the area.

The questions will be in `documentation/questions.md`

All of the python code can be seen in `src` folder and the queries in the `sql` folder. The DBT will be in the `dbt_project` folder. My conclusions will be in the `documentation/conclusions.md`.

If you want to reproduce my experiment, there is no problem, just take make sure to keep the MIT License.

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

To use the database, Docker Desktop or Engine must be installed and running. Once set up, start the database with:

```bash
docker-compose up -d
```

After this, the database will be running and accessible through tools like DBeaver or TablePlus using the credentials stored in `.database_env`.

To stop the database, run:

```bash
docker-compose down
```

Additionally, the project includes the Data Build Tool ([DBT](https://docs.getdbt.com/docs/introduction)), which facilitates data transformation, validation, and efficiency monitoring in the database.


## Documentation and Planning

For better alignment among team members, a repository will include two markdown files:

- `documentation.md`: Defines project goals and guidelines.
- `todo.md`: Tracks completed, ongoing, and upcoming tasks.

## Best Practices

- Always activate the virtual environment before working on the project to ensure correct dependencies.
- Keep `pyproject.toml` or `requirements.txt` updated with necessary dependencies.
- Use Git for version control and commit regularly to track progress.

---

I can't emphasize enough the impact of [Pedro Almeida](https://github.com/allmeidaapedro)'s work, which greatly influenced the structure of the `src` folder through his [project](https://github.com/allmeidaapedro/Churn-Prediction-Credit-Card).