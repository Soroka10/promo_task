#Promo Code Scraper + Gemini Rewriter

Цей Python-скрипт збирає актуальні промокоди з сайту [dealspotr.com](https://dealspotr.com) у категорії fashion, а також автоматично переписує описи кожного коду за допомогою Google Gemini API для покращення стилю.

##Функціонал

- Парсить посилання на сторінки з промокодами.
- Для кожного коду збирає:
  - URL магазину
  - Промокод (текст)
  - Оригінальний опис
  - Переписаний опис за допомогою Gemini
  - Дату збору
- Результати зберігаються у `promos_with_urls.csv`.

## Запуск

```bash
# Клонування репозиторію
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Створення та активація віртуального середовища (опціонально)
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Встановлення залежностей
pip install -r requirements.txt

# Створення .env з ключем API Gemini
echo GENIMI_API_KEY=your_api_key_here > .env

# Запуск скрипту
python main.py
