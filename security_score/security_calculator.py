def calculate_security_score(
    spam_probability,
    phishing_score,
    keyword_score
):

    security_score = (
        100
        - (spam_probability * 0.5)
        - (phishing_score * 0.3)
        - (keyword_score * 0.2)
    )

    security_score = max(
        0,
        min(100, round(security_score))
    )

    if security_score >= 80:
        threat_level = "Safe"

    elif security_score >= 60:
        threat_level = "Low Risk"

    elif security_score >= 40:
        threat_level = "Medium Risk"

    elif security_score >= 20:
        threat_level = "High Risk"

    else:
        threat_level = "Dangerous"

    return {
        "security_score": security_score,
        "threat_level": threat_level
    }


if __name__ == "__main__":

    spam_probability = 85
    phishing_score = 70
    keyword_score = 50

    result = calculate_security_score(
        spam_probability,
        phishing_score,
        keyword_score
    )

    print(result)