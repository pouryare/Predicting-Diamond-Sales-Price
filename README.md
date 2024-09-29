# Diamond Price Prediction

This project implements a machine learning model to predict diamond prices based on various characteristics. It uses a dataset from Kaggle and provides a Jupyter notebook for data analysis, model training, and prediction.

![Project Screenshot](screenshot.png)

## Dataset

The dataset used in this project is "The Largest Diamond Dataset Currently on Kaggle" by Hrokrin. You can find the original dataset [here](https://www.kaggle.com/datasets/hrokrin/the-largest-diamond-dataset-currely-on-kaggle).

## Features

- Predicts diamond prices based on multiple features such as cut, color, clarity, carat weight, and more.
- Uses Random Forest Regressor for predictions.
- Implements feature engineering to improve prediction accuracy.
- Provides a comprehensive Jupyter notebook for data analysis and model training.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/pouryare/diamond-price-prediction.git
   cd diamond-price-prediction
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download the dataset from the Kaggle link provided above and place it in the project directory.

## Usage

1. Open the Jupyter notebook:
   ```
   jupyter notebook "Predicting Diamond Sales Price.ipynb"
   ```

2. Run the cells in the notebook sequentially to perform the following steps:
   - Data loading and exploration
   - Data preprocessing and feature engineering
   - Model training and evaluation
   - Making predictions

3. You can modify the notebook to experiment with different models, features, or preprocessing steps.

## Project Structure

- `Predicting Diamond Sales Price.ipynb`: Main Jupyter notebook containing the data analysis, model training, and prediction code.
- `diamonds.csv`: The dataset file (you need to download this from Kaggle).
- `requirements.txt`: List of Python packages required for this project.
- `screenshot.png`: A screenshot of the project in action.

Note: The trained model and any intermediate files generated during the notebook execution are not included in this repository due to size limitations. These will be created when you run the notebook.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please open an issue on this GitHub repository.
