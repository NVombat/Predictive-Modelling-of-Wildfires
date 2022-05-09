import joblib

model = joblib.load('./model_jlib')

predict = model.predict([[float(123.5674),
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
    ]])

print(predict)