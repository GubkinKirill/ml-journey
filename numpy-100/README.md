# 100 задач по numpy

Учебный набор задач на основе [rougier/numpy-100](https://github.com/rougier/numpy-100):
только условия (английский + перевод), без решений.

## Запуск

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter lab 100_numpy_exercises.ipynb
```

## Помощники

Первая ячейка ноутбука подключает `initialise.py`:

| Функция | Что делает |
|---|---|
| `question(n)` | условие задачи |
| `hint(n)` | подсказка — какие функции смотреть |
| `pick()` | случайная задача |

Условия и подсказки лежат в `source/exercises.ktx`.
Лицензия исходного материала — MIT, см. `LICENSE.txt`.
