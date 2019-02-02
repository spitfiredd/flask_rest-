from sqlite_testing.database_funcs import insert_csv_to_db
import os
import pandas as pd


def main():
    insert_csv_to_db(
        'postgresql://localhost/db',
        pd.read_csv(os.path.join(os.environ["API_FILES"], 'people.csv')),
        table="people",
    )


if __name__ == '__main__':
    main()
