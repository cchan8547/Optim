# Portfolio optimization via QUBO
# Quantum-Inspired Portfolio Optimizer (QUBO Portfolio Optimizer)

This is a Streamlit-based application designed to leverage quantum-inspired optimization methods (Quadratic Unconstrained Binary Optimization, QUBO) for constructing and analyzing investment portfolios. It offers multiple models, ranging from basic portfolio optimization to advanced parameter search and rolling backtesting functionalities, helping users explore optimal asset allocation under different risk preferences.

## Features

### Model 1: Basic Portfolio Optimization (7251.py)

This model provides an intuitive interface for performing basic portfolio optimization. Users can select predefined ETF types (e.g., QQQ, DOW30, 0050) or custom stock tickers, and set the investment period. The system will optimize based on default return weight (p) and risk weight (q), and display key performance indicators of the portfolio, including expected annualized return, annualized volatility, Sharpe ratio, Maximum Drawdown (MDD), and a comparison chart with the SPY index.

- **Stock Selection:** Supports various ETF types and custom stock selection.
- **Optimization Parameters:** Optimizes using fixed return weight (p) and risk weight (q).
- **Performance Metrics:** Displays Sharpe ratio, expected return, volatility, MDD, etc.
- **Benchmark Comparison:** Provides performance comparison with the SPY index.
- **Supercomputer API Integration:** Optional use of an external supercomputer API for QUBO solving to accelerate the optimization process.

### Model 2: Parameter Search and Optimization (8021.py)

Building upon Model 1, Model 2 introduces parameter search functionality, allowing users to explore the impact of different combinations of return weight (p) and risk weight (q) on portfolio performance. Users can choose between grid search or random search strategies to find the optimal p and q values, thereby achieving specific investment goals (e.g., maximizing the Sharpe ratio).

- **Multi-dimensional Parameter Search:** Supports both Grid Search and Random Search modes to find the optimal p and q parameter combinations.
- **Visual Analysis:** Displays the relationship between return and volatility under different parameter combinations via scatter plots, color-coded by Sharpe ratio.
- **Optimal Parameter Recalculation:** After finding the best parameters, users can recalculate and display detailed portfolio performance using these parameters.
- **Supercomputer API Integration:** Optional use of an external supercomputer API during both parameter search and final recalculation.

### Model 3: Rolling Backtest (812.py)

Model 3 provides a more rigorous investment strategy validation method – rolling backtesting. Users can define the lengths of the training window and testing window, and the system will simulate dynamic adjustments and performance of the portfolio on historical data. This helps evaluate the strategy's robustness and adaptability under different market conditions.

- **Rolling Window Analysis:** Simulates the dynamic performance of the portfolio over different time periods, evaluating the long-term effectiveness of the strategy.
- **Customizable Window Sizes:** Flexible setting of training and testing window lengths.
- **Performance Metrics:** Calculates total return, Compound Annual Growth Rate (CAGR), Maximum Drawdown (MDD), and Turnover Rate.
- **Historical Composition:** Visualizes changes in portfolio composition during the backtest period.
- **Supercomputer API Integration:** Optional use of an external supercomputer API in each optimization step of the backtest.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Launch the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your default browser. You can select different model pages via the left navigation bar.

## Configuration

### Supercomputer API (Optional)

This application supports connecting to an external supercomputer API (e.g., Inventec's QUBO solving service) to accelerate complex QUBO solving processes. If you wish to use this feature, please ensure that the `SERVER_URI` variable in `7251.py`, `8021.py`, and `812.py` files points to the correct API endpoint. The default value is `http://60.250.149.247:8080`.

```python
SERVER_URI = "http://60.250.149.247:8080" # or your API endpoint
```

## Dependencies

All necessary Python dependencies are listed in the `requirements.txt` file, including:

- `streamlit`
- `yfinance`
- `numpy`
- `pandas`
- `scipy`
- `pyqubo`
- `requests`
- `python-socketio`
- `openjij` (for local solver)
- `matplotlib`
- `seaborn`
- `plotly`

## Contribution

Contributions of any kind are welcome! If you have any suggestions or find bugs, feel free to submit an Issue or Pull Request.

## License

[Please fill in license information here, e.g., MIT License.]


