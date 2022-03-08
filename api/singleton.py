import joblib
import os


class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance


singleton = Singleton()

singleton.reporter = joblib.load(open("../train_models/model_risk.joblib", "rb"))