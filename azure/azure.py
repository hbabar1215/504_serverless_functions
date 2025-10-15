import azure.functions as func
import logging
import json
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing HbA1c request.')

    # Try to get data from JSON or query parameters
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    hba1c = data.get("hba1c") or req.params.get("hba1c")

    # Check if hba1c is provided
    if hba1c is None:
        return func.HttpResponse(
            json.dumps({"error": "'hba1c' is required."}),
            status_code=400,
            mimetype="application/json"
        )

    # Validate numeric input
    try:
        hba1c_val = float(hba1c)
    except (TypeError, ValueError):
        return func.HttpResponse(
            json.dumps({"error": "'hba1c' must be a number."}),
            status_code=400,
            mimetype="application/json"
        )

    # Classification
    if hba1c_val < 5.7:
        status = "Normal"
        category = "No diabetes (<5.7)"
    elif 5.7 <= hba1c_val < 6.5:
        status = "Prediabetic"
        category = "At risk for diabetes (5.7–6.4)"
    else:
        status = "Abnormal"
        category = "Diabetes (≥6.5)"

    payload = {
        "hba1c": hba1c_val,
        "status": status,
        "category": category
    }

    return func.HttpResponse(
        json.dumps(payload, ensure_ascii=False),
        status_code=200,
        mimetype="application/json"
    )