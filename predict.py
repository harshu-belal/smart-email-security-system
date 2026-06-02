import joblib

# Load saved files
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("best_model.pkl")

print("Smart Email Security System")
print("Type 'exit' to quit")

while True:

    email = input("\nEnter Email: ")

    if email.lower() == "exit":
        print("Program Closed")
        break

    # Convert email to vector
    email_vector = vectorizer.transform([email])

    # Prediction
    prediction = model.predict(email_vector)

    # Probability
    probability = model.predict_proba(email_vector)

    spam_probability = probability[0][1] * 100
    safe_probability = probability[0][0] * 100

    print("\n========== RESULT ==========")

    if prediction[0] == 1:
        print("Classification : SPAM")
    else:
        print("Classification : SAFE")

    print(f"Spam Probability : {spam_probability:.2f}%")
    print(f"Safe Probability : {safe_probability:.2f}%")

    print("============================")