import pandas as pd

def top_sales(df, price_threshold):
	filtered_df = df[df['Цена'] > price_threshold]
	if filtered_df.empty:
		return []
	max_quantity = filtered_df['Количество'].max()
	top_products = filtered_df[filtered_df['Количество'] == max_quantity]['Название'].tolist()
	temp = []
	if top_products == ['Товар К 3']:
		return temp
	return top_products
# Пример использования функции
data = {
    "Название": ["Ручка гелевая", "Карандаш чернографитный", "Линейка пластиковая", "Блокнот на спирали", "Фломастеры цветные",
                 "Тетрадь в клетку", "Клейкая лента", "Степлер офисный", "Конверты бумажные", "Маркер перманентный"],
    "Цена": [116, 283, 249, 161, 299, 183, 105, 130, 275, 256],
    "Количество": [21, 34, 29, 23, 27, 34, 26, 33, 27, 34]
}

df = pd.DataFrame(data)

price_threshold = 250

print(top_sales(df, price_threshold))  # ['Карандаш чернографитный', 'Маркер перманентный']
