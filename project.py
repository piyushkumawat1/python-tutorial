import time
import re
from collections import Counter


# ----------------------------------------
# RULE-BASED DETECTION
# ----------------------------------------
def rule_based_detection(log_line):
    """
    Simple rule-based detection using fixed keywords.
    Returns True if any threat keyword is present in the log line.
    """
    threat_keywords = ["FAILED LOGIN", "UNAUTHORIZED", "MALWARE", "PORT SCAN"]
    log_upper = log_line.upper()
    return any(keyword in log_upper for keyword in threat_keywords)


# ----------------------------------------
# STATISTICAL DETECTION
# ----------------------------------------
def statistical_detection(log_line, common_words):
    """
    Statistical detection based on 'rarity' of words.
    If a log line contains more than 3 rare words (not in common_words),
    it is classified as a threat.
    """
    words = re.findall(r"\w+", log_line.lower())
    rare_score = sum(1 for w in words if w not in common_words)
    return rare_score > 3


# ----------------------------------------
# READ LOG FILE + AUTO FIX
# ----------------------------------------
def read_logs(filename):
    """
    Reads logs from a file.
    Expected format per line:
        <log text> | <label>
    where label is SAFE or THREAT.
    Automatically skips malformed lines and fixes invalid labels.
    """
    logs = []
    labels = []

    with open(filename, "r", encoding="utf-8") as file:
        for raw in file:
            raw = raw.strip()

            # Skip empty lines
            if not raw:
                continue

            # Line must contain a separator
            if "|" not in raw:
                print(f"[WARNING] Skipping line without separator: {raw}")
                continue

            # Use rsplit in case there are extra '|' in the log text
            try:
                text, label = raw.rsplit("|", 1)
            except ValueError:
                print(f"[WARNING] Skipping malformed line: {raw}")
                continue

            text = text.strip()
            label = label.strip().upper()

            # Auto-fix invalid labels
            if label not in ["SAFE", "THREAT"]:
                print(f"[WARNING] Invalid label '{label}', converting to SAFE")
                label = "SAFE"

            logs.append(text)
            labels.append(label)

    return logs, labels


# ----------------------------------------
# EVALUATE ALGORITHM
# ----------------------------------------
def evaluate(logs, labels, detector, extra=None):
    """
    Evaluates a detection function (detector) on given logs and labels.
    Returns metrics: TP, FP, TN, FN, Accuracy, Runtime.
    """
    TP = FP = TN = FN = 0
    start = time.time()

    for log, actual in zip(logs, labels):
        # Only pass extra if detector expects it
        if extra is None:
            predicted = detector(log)
        else:
            predicted = detector(log, extra)

        if predicted and actual == "THREAT":
            TP += 1
        elif predicted and actual == "SAFE":
            FP += 1
        elif not predicted and actual == "SAFE":
            TN += 1
        elif not predicted and actual == "THREAT":
            FN += 1

    runtime = time.time() - start

    if len(labels) == 0:
        accuracy = 0.0
    else:
        accuracy = (TP + TN) / len(labels) * 100.0

    return {
        "TP": TP,
        "FP": FP,
        "TN": TN,
        "FN": FN,
        "Accuracy": round(accuracy, 2),
        "Runtime": round(runtime, 6),
    }


# ----------------------------------------
# MAIN
# ----------------------------------------
def main():
    # Change this path to your actual log file (NOT the .py file)
    log_file = "/Users/mac/Documents/python-tutorial/project.py"

    print("Reading logs...")
    try:
        logs, labels = read_logs(log_file)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {log_file}")
        return

    if not logs:
        print("No valid logs found. Exiting.")
        return

    # Build vocabulary of all words
    all_words = []
    for log in logs:
        all_words.extend(re.findall(r"\w+", log.lower()))

    # Common words: those that appear at least twice
    common_words = {w for w, c in Counter(all_words).items() if c >= 2}

    print("\n=== Rule-Based Detection ===")
    rb = evaluate(logs, labels, rule_based_detection)
    print(rb)

    print("\n=== Statistical Detection ===")
    sd = evaluate(logs, labels, statistical_detection, common_words)
    print(sd)

    print("\n=== FINAL REPORT ===")
    print("Rule-Based Accuracy :", rb["Accuracy"], "%")
    print("Statistical Accuracy:", sd["Accuracy"], "%")

    if rb["Runtime"] < sd["Runtime"]:
        faster = "Rule-Based"
    elif sd["Runtime"] < rb["Runtime"]:
        faster = "Statistical"
    else:
        faster = "Tie"

    print("Faster Algorithm    :", faster)


if __name__ == "__main__":
    main()
