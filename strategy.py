import pandas as pd
import ta

def generate_signals(price_history: dict):
    signals = []
    for sym, history in price_history.items():
        df = pd.DataFrame({"close": history})
        df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
        last = df.iloc[-1]
        if last["rsi"] < 30:
            signals.append({
                "instrument": sym,
                "direction": "Buy",
                "confidence": int(100 - last["rsi"]),
                "entry": float(last["close"]),
                "exit": float(last["close"] * 1.02),
                "reason": f"RSI {last['rsi']:.1f} < 30"
            })
    return signals
