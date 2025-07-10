import time

class LowBalanceAlertManager:
    def __init__(self, thresholds, cooldown_ms):
        self.thresholds = thresholds
        self.cooldown_ms = cooldown_ms
        self.last_alert_time = {}  # wallet_idx -> timestamp_ms

    def check_and_alert(self, idx, address, sol_balance, alert_fn):
        if idx >= len(self.thresholds):
            return
        thresh = self.thresholds[idx]
        now_ms = int(time.time() * 1000)
        last = self.last_alert_time.get(idx, 0)
        if sol_balance < thresh and (now_ms - last) >= self.cooldown_ms:
            msg = f"⚠️ Low SOL alert `{address[:6]}...`: {sol_balance:.6f} SOL (< {thresh})"
            alert_fn(msg)
            self.last_alert_time[idx] = now_ms
