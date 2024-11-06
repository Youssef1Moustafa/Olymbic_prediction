# **Summer Olympics Medals (1896-2024)**

**Project Overview:**
This project analyzes the performance of athletes in the Summer Olympics from 1896 to 2024, predicting medal outcomes based on historical data using machine learning models. The dataset includes information about each athlete, their performance, the sport they competed in, and the medal they won. The goal is to explore trends in Olympic results and predict future outcomes using predictive modeling.

**Key Features:**
The dataset includes the following features for each athlete:
- `player_id`: Unique identifier for each athlete.
- `Name`: Name of the athlete.
- `Sex`: Gender of the athlete (Male (M) / Female (F)).
- `Team`: Country the athlete represented.
- `NOC`: National Olympic Committee code for the country.
- `Year`: Year of the Olympic Games.
- `Season`: Season of the Olympic Games (Summer).
- `City`: Host city of the Olympic Games.
- `Sport`: Sport category in which the athlete competed.
- `Event`: Specific event within the sport.
- `Medal`: Type of medal awarded (Gold, Silver, Bronze) or "No medal" if no medal was awarded.

**Machine Learning Models:**
To predict medal outcomes, the following models were applied:
1. **Random Forest**: Used to handle large datasets and make accurate predictions.
2. **Logistic Regression**: Implemented for binary classification (predicting if an athlete would win a medal or not).
3. **Decision Tree**: Applied to interpret the decision-making process and visualizations.
4. **XGBoost**: A highly effective boosting model used for enhancing prediction accuracy.

**Tools and Technologies:**
- **Python**: Main programming language used for data analysis, model training, and evaluation.
- **Power BI**: Used for creating visualizations and dashboards to explore Olympic performance trends.
- **Streamlit**: Web application framework for building interactive dashboards.
- **GitHub**: Code repository and project sharing platform.
- **Kaggle**: Dataset repository for accessing Olympic data.

**Project Goals:**
- Analyze historical Olympic data to identify performance trends over the years.
- Predict the likelihood of athletes winning medals in future Olympics.
- Visualize trends by sport, country, and gender.
- Understand factors influencing Olympic success.

**Installation:**
To get started with the project, follow the instructions below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/summer-olympics-medals.git
   cd summer-olympics-medals
   ```

2. **Install Required Libraries**:
   Use the `requirements.txt` file to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   To run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

**Project Structure:**
- `/data`: Contains the raw and cleaned datasets.
- `/models`: Includes the trained models and scripts used for model training.
- `/notebooks`: Jupyter notebooks for data exploration and analysis.
- `/visualizations`: Power BI files and other visualization outputs.
- `app.py`: Streamlit application for displaying the interactive dashboard.
- `requirements.txt`: List of dependencies for the project.

**Contributing:**
Feel free to fork the repository and submit pull requests for any improvements or new features. Contributions are always welcome!

**Acknowledgements:**
A huge thank you to my instructor **Eng. Hussein Zayed** for guidance throughout the project, and to my fantastic team members **Eng. Kareem Wesam**, **Eng. Mohamed Moussad**, **Eng. Mohamed Zayed**, and **Eng. Ibrahim Hassen** for their teamwork and collaboration.

**License:**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
