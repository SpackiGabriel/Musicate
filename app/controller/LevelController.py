from flask import flash
from app import db, session
from app.model.Level import Level

import requests


database = f"https://musicate-78320-default-rtdb.firebaseio.com"

def createLevel():
    level = Level(level=1, xp=0)

    db.session.add(level)
    db.session.commit()

    return level.getId()

def updateXp(moduleId):
    xp = gainXp(moduleId)

    try:
        level = Level.query.filter_by(id=session["idlevel"]).first()
        level.xp += xp

        db.session.add(level)
        db.session.commit()
        
        checkLevel(level, xp)
        
    except Exception as e:
        print(e)
        return

def gainXp(moduleId):
    xp = (int(moduleId) + 1) * 100 + (int(session["lifes"]) * 10)
    return xp

def checkLevel(level, xp):
    levels = requests.get(f"{database}/levels/.json").json()

    if levels[level.level + 1] and int(levels[level.level + 1]["xp"]) <= level.xp:
        
        try:
            level.level += 1
            db.session.add(level)
            db.session.commit()

            flash("LEVEL UP+++", "flash__win")

        except:
            return "deu erro"
    else:
        flash(f"+{xp} XP")


def getLevelName(levelId):

    levelname = requests.get(f"{database}/levels/{levelId}/.json").json()
    return levelname["name"]