def analyze_issue(issue):
    rules = {
        "phishing": "Possible phishing attack detected.",
        "malware": "Possible malware infection detected.",
        "ddos": "Potential DDoS attack identified."
    }

    return rules.get(issue.lower(), "No matching rule found.")
