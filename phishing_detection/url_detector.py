import re
from urllib.parse import urlparse

# Short URL Services
SHORT_URLS = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "buff.ly",
    "is.gd",
    "cutt.ly"
]

def detect_urls(email_text):

    urls = re.findall(
        r'https?://[^\s]+',
        email_text
    )

    phishing_score = 0

    detected_risks = []

    for url in urls:

        parsed = urlparse(url)

        domain = parsed.netloc.lower()

        # Short URL Detection
        if any(short in domain for short in SHORT_URLS):
            phishing_score += 30
            detected_risks.append(
                f"Shortened URL: {url}"
            )

        # IP Address URL Detection
        if re.search(
            r'^\d+\.\d+\.\d+\.\d+$',
            domain
        ):
            phishing_score += 40
            detected_risks.append(
                f"IP Address URL: {url}"
            )

        # Suspicious Keywords in URL
        suspicious_words = [
            "login",
            "verify",
            "update",
            "account",
            "bank",
            "secure",
            "confirm",
            "password"
        ]

        if any(
            word in url.lower()
            for word in suspicious_words
        ):
            phishing_score += 10
            detected_risks.append(
                f"Suspicious URL: {url}"
            )

    # Too many links
    if len(urls) > 3:
        phishing_score += 20
        detected_risks.append(
            "Too Many Links Detected"
        )

    # Limit score to 100
    phishing_score = min(
        phishing_score,
        100
    )

    return {
        "urls_found": len(urls),
        "phishing_score": phishing_score,
        "detected_risks": detected_risks
    }


# Testing
if __name__ == "__main__":

    sample_email = """
    Congratulations!
    Click here:
    http://bit.ly/free-prize

    Verify account:
    http://192.168.1.1/login

    """

    result = detect_urls(
        sample_email
    )

    print(result)