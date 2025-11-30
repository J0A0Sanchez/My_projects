import pandas as pd

def my_df():
    path = 'C:\\Python Cursos\\My Projects\\StudentGrades.csv'
    df = pd.read_csv(path)
    # print("csv File:")
    # print(df)
    # print("")


    df = df.rename(columns={"Module 1": "Chemistry", "Module 2": "Physics", "Module 3": "Biology"})
    # print(f"Columns after renaming: {df.columns.tolist()}")
    # print("")


    cols = list(df.columns[:3])
    for col in cols:
        df[col] = df[col].astype(str).str[-2:].astype(int)

    # print(f"The columns {cols} have been changed.")
    # print(df)
    # print("")


    df[["Name", "Surname"]] = df["Student Name"].str.split(" ", n=1, expand=True)
    df = df.drop(columns=["Student Name"])
    # print("The column 'Student Name' has been split into 'Name' and 'Surname'")
    # print(df)
    # print("")


    df["Total"] = (df["Chemistry"] * 0.5) + (df["Physics"] * 0.25) + (df["Biology"] * 0.25)
    print(df)
    return df




def df_analyser(dataframe):
    df_chemistry = dataframe[["Chemistry", "Name", "Surname"]]
    df_physics = dataframe[["Physics", "Name", "Surname"]]
    df_biology = dataframe[["Biology", "Name", "Surname"]]

    df_chemistry = df_chemistry.sort_values(by="Surname")
    df_physics = df_physics.sort_values(by="Surname")
    df_biology = df_biology.sort_values(by="Surname")

    df_chemistry.to_csv('C:\\Python Cursos\\My Projects\\df_chemistry.csv')
    df_physics.to_csv('C:\\Python Cursos\\My Projects\\df_physics.csv')
    df_biology.to_csv('C:\\Python Cursos\\My Projects\\df_biology.csv')
    
    print(df_chemistry)
    print("")
    print(df_physics)
    print("")
    print(df_biology)





df_analyser(my_df())
