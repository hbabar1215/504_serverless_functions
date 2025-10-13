import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'hba1c" (or query params as fallback).
    Returns a JSON classification of HbA1c level. 
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    hba1c = data.get("hba1c") or args.get("hba1c")

    # Presence check
    if hba1c is None:
        return (
            json.dumps({"error": "hba1c is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        hba1c_val = float(hba1c)
        
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'hba1c' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    if hba1c_val >= 6.5:
        status = "abnormal"
        category = "Diabetes (≥6.5%)"
    else:
        status = "normal"
        category = "Normal (<6.5%)"

    payload = {
        "hba1c": hba1c_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}