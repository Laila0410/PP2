from datetime import datetime, timedelta
# орысша кириллицага аударады
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Получаем сегодняшнюю дату
today = datetime.today()

# Вычитаем 5 дней
yesterday= today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
#today = today + timedelta(days=0)
print("Сегодня:", today.strftime("%y.%m.%d"))
print("1 дней назад:", yesterday.strftime("%y.%m.%d"))
print("после одного дня:", tomorrow.strftime("%y.%m.%d"))