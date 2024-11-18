import streamlit as st

# Список компьютеров с дополнительными характеристиками
computers = [
    {"name": "Acer Aspire 5", "category": "бюджетный", "type": "работа", "portability": True, "os": "Windows", "ram": 8, "ssd": True, "screen_size": 15.6},
    {"name": "Lenovo IdeaPad 1", "category": "бюджетный", "type": "работа", "portability": True, "os": "Windows", "ram": 4, "ssd": False, "screen_size": 14},
    {"name": "HP Stream 14", "category": "бюджетный", "type": "работа", "portability": True, "os": "Windows", "ram": 4, "ssd": False, "screen_size": 14},
    {"name": "ASUS VivoBook 15", "category": "бюджетный", "type": "работа", "portability": True, "os": "Windows", "ram": 8, "ssd": True, "screen_size": 15.6},
    {"name": "Dell Inspiron 15 3000", "category": "бюджетный", "type": "учеба", "portability": True, "os": "Windows", "ram": 8, "ssd": True, "screen_size": 15.6},
    {"name": "Apple MacBook Air M1", "category": "средний", "type": "работа", "portability": True, "os": "macOS", "ram": 8, "ssd": True, "screen_size": 13.3},
    {"name": "Dell XPS 13", "category": "средний", "type": "работа", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 13.4},
    {"name": "HP Pavilion Gaming", "category": "средний", "type": "игры", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 15.6},
    {"name": "ASUS TUF Gaming F15", "category": "средний", "type": "игры", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 15.6},
    {"name": "Lenovo Legion 5", "category": "средний", "type": "игры", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 15.6},
    {"name": "Microsoft Surface Laptop 4", "category": "средний", "type": "работа", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 13.5},
    {"name": "Acer Nitro 5", "category": "средний", "type": "игры", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 15.6},
    {"name": "ASUS ZenBook 14", "category": "средний", "type": "работа", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 14},
    {"name": "HP Envy x360", "category": "средний", "type": "работа", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 15.6},
    {"name": "Lenovo ThinkPad E15", "category": "средний", "type": "работа", "portability": True, "os": "Windows", "ram": 8, "ssd": True, "screen_size": 15.6},
    {"name": "Apple MacBook Pro 16\" M2", "category": "высокий", "type": "графика и видео", "portability": True, "os": "macOS", "ram": 32, "ssd": True, "screen_size": 16},
    {"name": "Razer Blade 15", "category": "высокий", "type": "игры", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 15.6},
    {"name": "Dell XPS 17", "category": "высокий", "type": "работа", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 17},
    {"name": "MSI Creator Z16", "category": "высокий", "type": "графика и видео", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 16},
    {"name": "ASUS ROG Zephyrus G14", "category": "высокий", "type": "игры", "portability": True, "os": "Windows", "ram": 16, "ssd": True, "screen_size": 14},
    {"name": "HP ZBook Fury 15 G8", "category": "высокий", "type": "графика и видео", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 15.6},
    {"name": "Alienware m17 R5", "category": "высокий", "type": "игры", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 17},
    {"name": "Lenovo ThinkPad P1 Gen 5", "category": "высокий", "type": "работа", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 15.6},
    {"name": "Apple iMac 24\" M1", "category": "высокий", "type": "графика и видео", "portability": False, "os": "macOS", "ram": 16, "ssd": True, "screen_size": 24},
    {"name": "Microsoft Surface Studio 2", "category": "высокий", "type": "графика и видео", "portability": False, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 28},
    {"name": "Origin PC EON17-X", "category": "высокий", "type": "игры", "portability": True, "os": "Windows", "ram": 64, "ssd": True, "screen_size": 17.3},
    {"name": "ASUS ProArt Studiobook 16 OLED", "category": "высокий", "type": "графика и видео", "portability": True, "os": "Windows", "ram": 32, "ssd": True, "screen_size": 16},
    {"name": "HP Omen 45L", "category": "высокий", "type": "игры", "portability": False, "os": "Windows", "ram": 64, "ssd": True, "screen_size": 27},
    {"name": "Corsair One Pro i200", "category": "высокий", "type": "работа", "portability": False, "os": "Windows", "ram": 64, "ssd": True, "screen_size": 27},
    {"name": "Falcon Northwest Talon", "category": "высокий", "type": "игры", "portability": False, "os": "Windows", "ram": 64, "ssd": True, "screen_size": 27}
]

# Интерфейс Streamlit
st.title("Выбор компьютера")
st.sidebar.header("Фильтры")

budget_category = st.sidebar.selectbox("Категория бюджета:", ["бюджетный", "средний", "высокий"])
usage_type = st.sidebar.selectbox("Тип использования:", [ "работа", "игры", "графика и видео"])
portability = st.sidebar.radio("Портативность:", ["Да", "Нет"])
os = st.sidebar.selectbox("Операционная система:", ["Windows", "macOS"])
ram = st.sidebar.selectbox("Объем оперативной памяти (ГБ):", [8, 16, 32, 64])
ssd = st.sidebar.radio("Наличие SSD:", ["Да", "Нет"])
screen_size = st.sidebar.slider("Диагональ экрана (дюймы):", 13, 32, (13, 27))

# Фильтрация компьютеров
filtered_computers = [
    comp for comp in computers
    if comp["category"] == budget_category and
    comp["type"] == usage_type and
    comp["portability"] == (portability == "Да") and
    comp["os"] == os and
    comp["ram"] == ram and
    comp["ssd"] == (ssd == "Да") and
    screen_size[0] <= comp["screen_size"] <= screen_size[1]
]

# Вывод результатов
if filtered_computers:
    st.subheader("Рекомендованные компьютеры:")
    for comp in filtered_computers:
        st.write("- " + comp["name"])
else:
    st.write("Подходящих моделей не найдено.")
