# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/sulianova/cardiovascular-disease-dataset?select=cardio_train.csv

Задача: предсказать наличие или отсутствие сердечно-сосудистых заболеваний (поле cardio) по данным, собранным на момент медицинского осмотра. Бинарная классификация

Используемые признаки:

- age- возраст в днях (int)
- height- рост в см (int)
- weigh - вес в кг (float)
- gende - пол (categorical code)
- ap_hi - систолическое артериальное давление (int)
- ap_lo - диастолическое артериальное давление (int)
- cholesterol - холестерин (1: нормальный, 2: выше нормы, 3: значительно выше нормы)
- gluc - глюкоза (1: нормальная, 2: выше нормы, 3: значительно выше нормы)
- smoke - курение (binary)
- alco - употребление алкоголя (binary)
- active - физическая активность (binary)


Преобразования признаков: StandardScaler, OHEEncoder

Модель: xgboost

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/bew-bit/Disease_Prediction_ML_docker_flask.git
$ cd Disease_Prediction_ML_docker_flask
$ docker build -t bew-bit/Disease_Prediction_ML_docker_flask .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models bew-bit/Disease_Prediction_ML_docker_flask
```

### Переходим на localhost:8181
