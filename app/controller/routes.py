from app import app, session
from flask import redirect, render_template, flash

from app.controller import QuestionController
from app.controller import ProgressController
from app.controller import LevelController

import random

from app.model.Progress import Progress
from app.model.Level import Level

@app.route("/")
def index():
    if "login" not in session:
        return render_template('home.html')
    return redirect('/feed/')
    
@app.route("/registrar/", methods=["GET"])
def register():
    if "login" not in session:
        return render_template('register.html')
    return redirect('/feed/')

@app.route("/login/", methods=["GET"])
def login():
    if "login" not in session:
        return render_template('login.html')
    return redirect('/feed/')

@app.route("/feed/", methods=["GET", "POST"])
def feed():
    if "login" in session:
        progress = Progress.query.filter_by(id=session["idprogress"]).first()
        level = Level.query.filter_by(id=session["idlevel"]).first()

        sheetprogress = progress.sheetmodule
        cipherprogress = progress.ciphermodule

        levelId = level.level

        levelname = LevelController.getLevelName(levelId)
        xp = level.xp

        if session["playing"]:
            session["playing"] = False
            del session["lifes"]
            del session["last"]

        return render_template('feed.html', cipherprogress=cipherprogress, sheetprogress=sheetprogress, username=session["name"].split()[0], level=levelname, xp=xp)
    else:
        return redirect("/")

@app.route("/logout/", methods=["GET"])
def logout():
    if "login" in session:
                
        del session["login"]
        del session["name"]
        del session["email"]

        return redirect("/")
    else:
        return redirect("/feed/")

@app.route("/esqueceu/", methods=["GET"])
def forgot():
    if "login" not in session:
        return render_template('forgot.html')
    return redirect('/feed/')

@app.route("/recuperar/")
def recover():
    if "login" not in session:
        return render_template('recover.html')
    return redirect('/feed/')

@app.route("/jogar/<moduleName>/<moduleId>/<levelId>", methods=["GET"])
def moduleLoader(moduleName, moduleId, levelId):
    if "login" not in session:
        return redirect('/')
    level = QuestionController.loadQuestion(moduleName, int(moduleId), int(levelId))

    try:
        question = level["question"]
        answers = level["answers"]

    except:
        ProgressController.unlockModule(moduleName=moduleName)
        LevelController.updateXp(moduleId=moduleId)
        return redirect("/feed/")


    path = "null"

    if "path" in level:
        path = level["path"]

    content = []
        
    while len(content) < 4:
        quest = random.choice(answers)
        if quest not in content:
            content.append(quest)

    if int(levelId) == 0 and session["playing"] == False:
        session["playing"] = True
        session["lifes"] = 3

    if "last" in session:
        if session["last"] != levelId:
            flash("Você acertou!", "flash__win")
            session["last"] = levelId
        else:
            flash("Você errou!", "flash__error")
        
    else:
        session["last"] = levelId

    return render_template("question.html", question=question, path=path, answers=content, correctAnswer=answers[0], moduleName=moduleName, moduleId=moduleId, levelId = levelId, lifes=session["lifes"])

@app.route("/derrota/<moduleName>/<moduleId>/")
def defeat(moduleName, moduleId):
    if "login" in session:
        return render_template("defeat.html", moduleName=moduleName, moduleId=moduleId)
    return redirect('/')

@app.route("/confirmar/")
def confirm():
    return render_template("confirm.html")


@app.route("/cifras/")
def cipher():
    if "login" in session:
        return render_template("cipher.html")
    return redirect("/")

@app.route("/partituras-com-clave-de-sol/")
def sheet():
    if "login" in session:
        return render_template("sheet.html")
    return redirect("/")

@app.route("/partituras-com-clave-de-sol-2/")
def sheetSecond():
    if "login" in session:
        return render_template("sheet2.html")
    return redirect("/")

@app.route("/configuracoes/")
def configurations():
    if "login" in session:
        level = Level.query.filter_by(id=session["idlevel"]).first()
        return render_template('configuration.html', name=session["name"], email=session["email"], xp=level.xp, levelname=LevelController.getLevelName(level.level))
    return redirect("/")

@app.route("/alterar/<config>/")
def showConfigPage(config):
    if "login" in session:
        if config == 'nome':
            return render_template("updatename.html")
        elif config == 'email':
            return render_template(f"updateemail.html")
    
    return redirect('/')

@app.route("/deletar/conta/")
def delete():
    if "login" in session:
        return render_template("delete.html")
    return redirect("/")

from app.controller import UserController 