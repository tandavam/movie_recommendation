import traceback
from flask import jsonify


def catch_exception(error):
    try:
        return jsonify({
            "status_id": 0,
            "error_response": {
                "traceback": traceback.format_exc().splitlines(),
                "error_message": str(error)
            }
        })
        pass

    except Exception:
        print("Error in Catching Exception:  " + str(error))
        return jsonify({
            "status_id": 0,
            "error_response": {
                "error_message": "Unexpected Error Occurred"
            }
        })
