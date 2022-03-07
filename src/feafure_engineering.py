import pandas as pd
from datetime import datetime, date
from storage import Storage 

storage = Storage()
storage.download()

df = pd.read_csv('../data/input/dataset_credit_risk.csv')
df = df.sort_values(by=["id", "loan_date"])
df = df.reset_index(drop=True)
df["loan_date"] = pd.to_datetime(df.loan_date)
df_grouped = df.groupby("id")
df["nb_previous_loans"] = df_grouped["loan_date"].rank(method="first") - 1
df['avg_amount_loans_previous'] = (
    df.groupby('id')['loan_amount'].apply(lambda x: x.shift().expanding().mean())
)


df['birthday'] = pd.to_datetime(df['birthday'], errors='coerce')
df['age'] = (pd.to_datetime('today').normalize() - df['birthday']).dt.days // 365
df['job_start_date'] = pd.to_datetime(df['job_start_date'], errors='coerce')
df['years_on_the_job'] = (pd.to_datetime('today').normalize() - df['job_start_date']).dt.days // 365
df['flag_own_car'] = df.flag_own_car.apply(lambda x : 0 if x == 'N' else 1)
df = df[['id', 'age', 'years_on_the_job', 'nb_previous_loans', 'avg_amount_loans_previous', 'flag_own_car', 'status']]
df.to_csv('../data/output/train_model.csv', index=False)

#storage.upload()