# projet_python
Ce script se concentrera sur la récupération des données de Yahoo Finance à l'aide de yfinance, la chargemrnt de ces données dans une BDD Mongo et l'affichage des tableaux et des visuel à l'aide de la bibliothèque Streamlit.
la classe Yfinancee  prend trois arguments: symbol pour le symbole boursier que nous voulons récupérer, debut et fin pour les dates de début et de fin des données que nous voulons récupérer. La méthode gdata(): utilise yfinance pour récupérer les données à partir de Yahoo Finance. 
La classe Mongobdd prend trois arguments: data pour les données que nous voulons insérer dans la base de données, db_name pour le nom de la base de données dans laquelle nous voulons insérer les données, et collection_name pour le nom de la collection dans laquelle nous voulons insérer les données.
La méthode insert_data() utilise la bibliothèque pymongo pour se connecter à la base de données, créer une collection et insérer les données récupérées.
La classe Streamlitappli s'occupe de interrogation de l'API/BDD pour récupérer les données, puis sur l'affichage de ces données sous forme de graphique/tableau sur un Dashboard Streamlit.
