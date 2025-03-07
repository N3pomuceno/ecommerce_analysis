"""
File to execute DML queries in terminal with python. Cases for example:
https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples

To execute this file, it needs a arguments related to its query filepath, just like: python query_execution.py path/to/file.sql
"""

import util
import sys
import os
from logger import setup_logger

logger = setup_logger(log_dir="logs", log_filename="query", level="INFO")

# Load enviroment variables
logger.info("Loading Enviroment Variables for database connection...")
env_vars = util.load_environment_variables_for_db()

# Create engine to make connection with db
logger.info("Connecting to Database...")
engine = util.get_database_engine(env_vars)
conn = engine.connect()


filepath = util.get_args[1]

if os.path.splitext(filepath)[1].lower() != ".sql":
    logger.error("File isn't SQL. Please ensure the path is correct.")
    sys.exit(1)

# Read query file
try:
    with open(filepath, mode="r", encoding="UTF-8") as f:
        query = f.read()
except Exception as e:
    logger.error(f"Error reading file: {e}")
    sys.exit(1)

# Execute query
logger.info("Executing query...")
try:
    with engine.connect() as conn:
        result = conn.execute(query)
        if result.returns_rows:
            logger.info("Results:\n{}".format(result.fetchall()))
except Exception as e:
    logger.error(f"Query execution failed: {e}")
    sys.exit(1)
