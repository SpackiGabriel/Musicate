from flask import redirect
from app import db, session

from app.model.User import User
from app.model.Progress import Progress


def createProgress():
    progress = Progress(sheetmodule=0, ciphermodule=0)

    db.session.add(progress)
    db.session.commit()

    return progress.getId()

def unlockModule(moduleName):
    try:
        progress = Progress.query.filter_by(id=session["idprogress"]).first()

        if moduleName == "init" and progress.sheetmodule == 0 and progress.ciphermodule == 0:
            progress.sheetmodule  += 1
            progress.ciphermodule += 1

        elif moduleName == "sheet" and progress.sheetmodule <= 2:
            progress.sheetmodule  += 1
        
        elif moduleName == "cipher" and progress.ciphermodule <= 2:
            progress.ciphermodule += 1

        db.session.add(progress)
        db.session.commit()
        
    except Exception as e:
        print(e)
        return