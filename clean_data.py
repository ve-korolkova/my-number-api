import pandas as pd
import numpy as np
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_data_short(df):
    """Упрощённая очистка данных: дубликаты, выбросы, мусор, типы."""
    info = {'original_rows': len(df)}
    logger.info(f"Начало очистки. Исходных строк: {info['original_rows']}")

    # 1. Удаление дубликатов
    df = df.drop_duplicates()
    duplicates_removed = info['original_rows'] - len(df)
    if duplicates_removed:
        logger.info(f"Удалено дубликатов: {duplicates_removed}")
        info['duplicates_removed'] = duplicates_removed

    # 2. Очистка числовых колонок (выбросы по IQR)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outliers_removed = 0
    for col in numeric_cols:
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        mask = (df[col] >= lower) & (df[col] <= upper)
        outliers_count = len(df) - mask.sum()
        df = df[mask]
        outliers_removed += outliers_count
    if outliers_removed:
        logger.info(f"Удалено выбросов: {outliers_removed}")
        info['outliers_removed'] = outliers_removed

    # 3. Очистка текстовых колонок (мусор, пробелы)
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = (df[col].astype(str)
                     .str.strip()
                     .str.lower()
                     .str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
                     .replace('', np.nan))

    # 4. Удаление пропусков
    missing_removed = df.isnull().sum().sum()
    df = df.dropna()
    if missing_removed:
        logger.info(f"Удалено пропусков: {missing_removed}")
        info['missing_removed'] = missing_removed

    # 5. Приведение типов
    for col in df.columns:
        if df[col].dtype == 'object':
            numeric_col = pd.to_numeric(df[col], errors='coerce')
            if not numeric_col.isna().all():
                df[col] = numeric_col

    # Финальная статистика
    info['final_rows'] = len(df)
    info['total_removed'] = info['original_rows'] - info['final_rows']
    logger.info(f"Очистка завершена. Осталось строк: {info['final_rows']} "
              f"({info['total_removed']} удалено)")

    return df, info

# Пример использования
if __name__ == '__main__':
    # Тестовые данные с мусором и выбросами
    np.random.seed(42)
    test_df = pd.DataFrame({
        'A': np.random.normal(10, 2, 100),
        'B': np.random.uniform(0, 100, 100),
        'C': ['text' + str(i) for i in range(100)],
        'D': np.random.choice(['X', 'Y', 'Z'], 100)
    })
    # Добавляем проблемы
    test_df.loc[10:15, 'A'] = [1000, -500, 999, -800, 1200, -700]  # выбросы
    test_df.loc[20:25, 'C'] = ['@@@garbage@@@', '!!!', '***', '???', '$$$', '###']  # мусор
    test_df.loc[30:35, 'B'] = [np.nan, None, '', 'N/A', 'NULL', 'missing']  # пропуски

    print("Исходный размер:", test_df.shape)
    cleaned_df, clean_info = clean_data_short(test_df)
    print("Очищенный размер:", cleaned_df.shape)

    # Вывод информации об очистке
    print("\n" + "="*40)
    print("СТАТИСТИКА ОЧИСТКИ")
    print("="*40)
    for k, v in clean_info.items():
        print(f"{k}: {v}")
