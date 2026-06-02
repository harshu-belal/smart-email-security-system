import joblib

from phishing_detection.url_detector import detect_urls
from keyword_analysis.keyword_detector import detect_keywords
from security_score.security_calculator import calculate_security_score

# Load ML files
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("best_model.pkl")


def analyze_email(email_text):

    # ----------------------------
    # SPAM DETECTION
    # ----------------------------

    email_vector = vectorizer.transform(
        [email_text]
    )

    prediction = model.predict(
        email_vector
    )

    probability = model.predict_proba(
        email_vector
    )

    spam_probability = round(
        float(probability[0][1] * 100),
        2
    )

    classification = (
        "SPAM"
        if prediction[0] == 1
        else "SAFE"
    )

    # ----------------------------
    # PHISHING DETECTION
    # ----------------------------

    phishing_result = detect_urls(
        email_text
    )

    phishing_score = phishing_result[
        "phishing_score"
    ]

    # ----------------------------
    # KEYWORD DETECTION
    # ----------------------------

    keyword_result = detect_keywords(
        email_text
    )

    keyword_score = keyword_result[
        "keyword_score"
    ]

    # ----------------------------
    # SECURITY SCORE
    # ----------------------------

    security_result = calculate_security_score(
        spam_probability,
        phishing_score,
        keyword_score
    )

    # ----------------------------
    # FINAL RESULT
    # ----------------------------

    result = {

        "prediction":
            classification,

        "spam_probability":
            spam_probability,

        "phishing_score":
            phishing_score,

        "keyword_score":
            keyword_score,

        "security_score":
            security_result[
                "security_score"
            ],

        "threat_level":
            security_result[
                "threat_level"
            ],

        "urls_found":
            phishing_result[
                "urls_found"
            ],

        "detected_risks":
            phishing_result[
                "detected_risks"
            ],

        "keywords_found":
            keyword_result[
                "keywords_found"
            ],

        "detected_keywords":
            keyword_result[
                "detected_keywords"
            ]
    }

    return result


# ----------------------------
# TESTING
# ----------------------------

if __name__ == "__main__":

    sample_email = """
    Congratulations!

    You are our lucky winner.

    Click here:
    http://bit.ly/free-prize

    Verify account immediately.

    Claim your free gift card.
    """

    result = analyze_email(
        sample_email
    )

    print("\n===== ANALYSIS RESULT =====")

    for key, value in result.items():
        print(f"{key}: {value}")