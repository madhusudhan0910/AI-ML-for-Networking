import pickle
import urllib.parse
def preprocess_url(input_string):
    try:
        parsed = urllib.parse.urlparse(input_string)
        query = urllib.parse.parse_qs(parsed.query)
        path = parsed.path
        query_values = [str(v) for q in query.values() for v in q]
        return " ".join([parsed.netloc, path] + query_values)
    except Exception:
        return input_string
def detect_threat(input_data, is_file=False):
    with open("app/model.pkl", "rb") as f_model:
        model = pickle.load(f_model)
    with open("app/vectorizer.pkl", "rb") as f_vec:
        vectorizer = pickle.load(f_vec)
    if is_file:
        try:
            lines = input_data.decode("utf-8").splitlines()
        except UnicodeDecodeError:
            return [{"error": "Invalid encoding"}]
        results = []
        for line in lines:
            clean = line.strip()
            if clean:
                processed = preprocess_url(clean)
                vec = vectorizer.transform([processed])
                prediction = model.predict(vec)[0]
                results.append({
                    "payload": clean,
                    "result": prediction  
                })
        return results
    processed = preprocess_url(input_data)
    vec = vectorizer.transform([processed])
    prediction = model.predict(vec)[0]
    return prediction  
