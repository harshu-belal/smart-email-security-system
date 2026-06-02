import re

SUSPICIOUS_KEYWORDS = [
    "winner",
    "free",
    "urgent",
    "click here",
    "verify account",
    "claim prize",
    "limited time",
    "offer expires",
    "congratulations",
    "selected",
    "bonus",
    "reward",
    "gift card",
    "lottery",
    "cash prize",
    "bank account",
    "login now",
    "update account",
    "security alert",
    "password"
]

def detect_keywords(email_text):

    email_text = email_text.lower()

    found_keywords = []

    keyword_score = 0

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in email_text:

            found_keywords.append(keyword)

            keyword_score += 10

    keyword_score = min(keyword_score, 100)

    return {
        "keyword_score": keyword_score,
        "keywords_found": len(found_keywords),
        "detected_keywords": found_keywords
    }


if __name__ == "__main__":

    sample_email = """
    Congratulations!

    You are our lucky winner.

    Click here to claim prize.

    Verify account immediately.

    Limited time offer expires soon.
    """

    result = detect_keywords(sample_email)

    print(result)