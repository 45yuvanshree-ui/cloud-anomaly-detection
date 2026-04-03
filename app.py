from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

# -------------------------
# LOAD FILES
# -------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

ip_map = pickle.load(open("ip_map.pkl", "rb"))
event_map = pickle.load(open("event_map.pkl", "rb"))
region_map = pickle.load(open("region_map.pkl", "rb"))

print("All files loaded successfully!")

# -------------------------
# ROUTE
# -------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        try:
            file = request.files["file"]
            df = pd.read_csv(file, low_memory=False)

            # Select columns
            df = df[['eventTime','sourceIPAddress','userAgent','eventName',
                     'eventSource','awsRegion','userIdentitytype',
                     'eventType','errorCode','requestParametersinstanceType']]

            # Feature engineering
            df['is_error'] = df['errorCode'].notnull().astype(int)

            df['ip_frequency'] = df['sourceIPAddress'].map(ip_map).fillna(1)
            df['event_frequency'] = df['eventName'].map(event_map).fillna(1)
            df['region_frequency'] = df['awsRegion'].map(region_map).fillna(1)

            # TF-IDF
            tfidf_matrix = tfidf.transform(df['eventName'])
            tfidf_df = pd.DataFrame(
                tfidf_matrix.toarray(),
                columns=tfidf.get_feature_names_out()
            )

            # Combine features
            X = pd.concat([
                df[['is_error','ip_frequency','event_frequency','region_frequency']].reset_index(drop=True),
                tfidf_df.reset_index(drop=True)
            ], axis=1)

            # Scale
            X_scaled = scaler.transform(X)

            # Predict
            preds = model.predict(X_scaled)

            anomaly_count = (preds == -1).sum()

            return f"""
            <h2>Total Records: {len(df)}</h2>
            <h2>Anomalies Detected: {anomaly_count}</h2>
            """

        except Exception as e:
            return f"<h3>Error:</h3><p>{str(e)}</p>"

    return '''
    <h2>AWS Cloud Log Anomaly Detection</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <br><br>
        <input type="submit" value="Upload and Detect">
    </form>
    '''

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run()