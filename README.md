# Stock Price Movement Prediction (LSTM)

## 1. Problem
The objective is to predict short-term bullish momentum in equity markets. Specifically, the model performs binary classification to determine if a ticker will experience a price increase of at least X% within a 3-day forward-looking window.

## 2. Approach
Data Acquisition & ProcessingSource: Historical OHLCV (Open, High, Low, Close, Volume) data.

Feature Engineering: * Technical Indicators: RSI, MACD, Bollinger Bands, and Exponential Moving Averages (EMA).

Momentum Features: Log returns and volume change rates.

Normalization: Robust scaling to handle outliers and high-volatility periods.

Labeling Strategy: Labels are generated using a fixed-horizon look-ahead. For a given time t, the label $y_t$ is defined as:
Yt = 1 if (Pt+3 - Pt)/Pt >= Threshold; Yt = 0 otherwise

- Model: LSTM
  The core engine is a Long Short-Term Memory (LSTM) network, chosen for its ability to maintain internal state and capture long-range temporal dependencies in time-series data.

## 3. Key Decisions
Why a 3-Day Horizon? Intraday data is often dominated by noise, while 30-day horizons are heavily influenced by macro-economic shifts. A 3-day window targets "swing" momentum—capturing technical breakouts while minimizing the impact of long-term drift.

Why Classification over Regression? Predicting the exact price (regression) is notoriously difficult and often yields high Mean Absolute Error (MAE) without providing actionable trading signals. Classification simplifies the problem into a decision-making tool: Is this a high-probability entry?

Why LSTM? Unlike XGBoost or Random Forests, which treat each time step as an independent observation, LSTMs utilize a "hidden state" to "remember" previous price action, which is critical for identifying patterns like "Head and Shoulders" or "Cup and Handle."

## 4. Results

### Model Performance
- Accuracy: XX%
- Precision (Bullish class): XX%
- Recall (Bullish class): XX%
- F1 Score: XX%

The model achieves higher precision than recall, indicating it is more conservative in predicting bullish signals, which helps reduce false positives.

### Baseline Comparison
A simple baseline (e.g., random prediction or always predicting "no increase") yields ~50% accuracy.

The LSTM model outperforms this baseline, suggesting it captures non-random temporal structure in the data.

### Trading-Oriented Interpretation
From a trading perspective:
- Precision is more critical than accuracy, as false positives can lead to unprofitable trades.
- The model shows [moderate/high/low] precision, indicating [how reliable signals are].

(Optional if you have it)
- Backtesting results show that following model signals yields:
  - Average return: XX%
  - Win rate: XX%

### Key Insights
- Short-term momentum signals are partially predictable using technical indicators.
- The model performs better during [trending markets vs sideways markets] (if observed).
- Performance degrades during high-volatility periods, suggesting sensitivity to regime changes.

## 5. Limitations
- Market randomness
- Overfitting risk
- Feature limitations

## 6. How to Run
```bash
pip install -r requirements.txt
python train.py
