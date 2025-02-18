from datetime import datetime
import sys
sys.stdout.reconfigure(encoding = 'utf-8')
# прям қазіргі уақыт текущее время
now = datetime.now()
# to reduce microsecond
without_microseconds = now.replace(microsecond=0)

print("C микросекунда:", now)
print("без микросекунда:", without_microseconds)
