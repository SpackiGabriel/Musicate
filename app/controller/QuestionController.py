from flask import redirect
from app import app, session

import requests


database = f"https://musicate-78320-default-rtdb.firebaseio.com"

def loadQuestion(moduleName, moduleId, levelId):
    level = requests.get(f"{database}/modules/{moduleName}/{moduleId}/question-{levelId}/.json").json()
    return level

@app.route("/check/<moduleName>/<moduleId>/<levelId>/<value>", methods=["GET"])
def check(moduleName, moduleId, levelId, value):

    if int(value) == 1 and session["lifes"] > 0:
        return redirect(f"/jogar/{moduleName}/{moduleId}/{int(levelId) + 1}")
        
    if session["lifes"] == 1:
        session["playing"] = False
        del session["last"]
        return redirect(f"/derrota/{moduleName}/{moduleId}/")

    session["lifes"] -= 1
    return redirect(f"/jogar/{moduleName}/{moduleId}/{levelId}")