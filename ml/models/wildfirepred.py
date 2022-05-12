from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib


def process_data():
    forest_data = pd.read_csv("../datasets/fire_archive.csv")

    forest_data = forest_data.drop(["track"], axis=1)
    forest_data = forest_data.drop(["instrument", "version"], axis=1)

    daynight_map = {"D": 1, "N": 0}
    satellite_map = {"Terra": 1, "Aqua": 0}

    forest_data["daynight"] = forest_data["daynight"].map(daynight_map)
    forest_data["satellite"] = forest_data["satellite"].map(satellite_map)

    types = pd.get_dummies(forest_data["type"])
    forest_data = pd.concat([forest_data, types], axis=1)

    forest_data = forest_data.drop(["type"], axis=1)
    forest_data = forest_data.rename(columns={0: "type_0", 2: "type_2", 3: "type_3"})

    bins = [0, 1, 2, 3, 4, 5]
    labels = [1, 2, 3, 4, 5]
    forest_data["scan_binned"] = pd.cut(forest_data["scan"], bins=bins, labels=labels)

    forest_data["acq_date"] = pd.to_datetime(forest_data["acq_date"])
    forest_data = forest_data.drop(["scan"], axis=1)

    forest_data["year"] = forest_data["acq_date"].dt.year
    forest_data["month"] = forest_data["acq_date"].dt.month
    forest_data["day"] = forest_data["acq_date"].dt.day

    y = forest_data["confidence"]
    fin = forest_data.drop(
        ["confidence", "acq_date", "acq_time", "bright_t31", "type_0"], axis=1
    )

    return fin, y


def train_data(X, y):
    random_model = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    random_model.fit(X.iloc[:, :500], y)

    return random_model


def create_model(model):
    joblib.dump(model, "model_jlib")


def test_model():
    model = joblib.load("./model_jlib")
    predict = model.predict(
        [
            [
                float(123.5674),
                float(234.5678),
                float(432.1),
                int(1),
                float(456.9),
                int(0),
                int(1),
                int(0),
                int(3),
                int(2020),
                int(11),
                int(19),
            ]
        ]
    )

    print(predict)


if __name__ == "__main__":
    X, y = process_data()
    model = train_data(X, y)
    create_model(model)
