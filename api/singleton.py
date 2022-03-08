import joblib
import pandas as pd

class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance


singleton = Singleton()

singleton.modelo = joblib.load(open("../train_models/model_risk.joblib", "rb"))
singleton.model_train = pd.read_csv('../data/output/train_model.csv')