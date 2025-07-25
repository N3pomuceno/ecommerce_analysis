# import os
import pandas as pd

# from sqlalchemy import create_engine
# from dotenv import load_dotenv
from logger import setup_logger
import util

logger = setup_logger(log_dir="logs", log_filename="config", level="INFO")


def turn_csv_to_db(csv_file: str, table_name, engine) -> None:
    """
    Converts a CSV file to a database table.

    Args:
        csv_file (str): The path to the CSV file.
        table_name (str): The name of the table to create in the database.
        engine: The SQLAlchemy engine connected to the database.
    """
    logger.info("Carregando dados para o banco de dados")
    df = pd.read_csv(csv_file)
    save_to_database(df, table_name, engine)
    logger.info("Dados carregados com sucesso!")


def save_to_database(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def main():
    logger.info("Definindo variáveis de ambiente")
    env_vars = util.load_environment_variables_for_db()
    engine = util.get_database_engine(env_vars)

    turn_csv_to_db(
        csv_file="data/processed_data.csv",
        table_name=env_vars["TABLE_NAME"],
        engine=engine,
    )


if __name__ == "__main__":
    main()
