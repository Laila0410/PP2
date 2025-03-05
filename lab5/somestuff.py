import re
8[\s\(]?\d{3}[\s\)\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}
import re

camel = "thisIsCamelCase"

# Регулярка: найти место, где маленькая буква перед большой буквой
pattern = r'([a-z])([A-Z])'

# Заменяем такие места на: маленькая буква + _ + большая буква в нижнем регистре
snake = re.sub(pattern, r'\1_\2', camel).lower()

print(snake)  # this_is_camel_case
