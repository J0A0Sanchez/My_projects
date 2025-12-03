import pandas as pd
from CA2_tasks_pandas import my_df, df_generator

#Task 3:

def df_choices(df_name):
    df_choice = df_generator(my_df(),subject=df_name)


    if df_name in ("Chemistry", "Physics", "Biology"):
        max_value = df_choice[df_name].max()
        min_value  = df_choice[df_name].min()
        mean_value  = df_choice[df_name].mean()
        std_value  = df_choice[df_name].std()

        print(f"{df_name} information:")
        print(f"Max {df_name}: {max_value}")
        print(f"Min {df_name}: {min_value}")
        print(f"Mean {df_name}: {mean_value:.2f}")
        print(f"Standard Deviation {df_name}: {std_value:.2f}")

    elif df_name == "all":
        max_value = my_df()["Total"].max()
        min_value  = my_df()["Total"].min()
        mean_value  = my_df()["Total"].mean()
        std_value = my_df()["Total"].std()

        print(f"{df_name} information (total column):")
        print(f"Max Total: {max_value}")
        print(f"Min Total: {min_value}")
        print(f"Mean Total: {mean_value:.2f}")
        print(f"Standard Deviation Total: {std_value:.2f}")


stats = ""
while stats != 'q':

    stats  = str(input("What stats you want to check:  'Chemistry', 'Physics', 'Biology', 'all'? Type 'Q' to quit: "))
    if stats == 'q':
        break

    df_choices(stats)

