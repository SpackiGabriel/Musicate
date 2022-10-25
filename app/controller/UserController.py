from flask import redirect, flash, request
from app import app, db, session

from email.message import EmailMessage
import ssl, smtplib

from app.model.User import User

from app.controller.routes import *
from app.controller.functions import generateToken, crypt
from app.controller import ProgressController
from app.controller import LevelController


@app.route("/users/create/", methods=["POST"])
def createUser():
    body = {
            "name":request.form["name"], 
            "email":request.form["email"], 
            "password":request.form["password"],
            "password_confirmation":request.form["password_confirmation"]
        }
    
    try:
        if body["password"] == body["password_confirmation"]:
            idprogress = ProgressController.createProgress()
            idlevel = LevelController.createLevel()

            password = crypt(body["password"])

            user = User(name=body["name"], email=body["email"], password=password, idprogress=idprogress, idlevel=idlevel)
            
            db.session.add(user)
            db.session.commit()
    
            session["login"] = True 
            session["name"] = user.name
            session["email"] = user.email
            session["idprogress"] = idprogress
            session["idlevel"] = idlevel
            session["playing"] = False
        
            return redirect('/feed/')
        else:
            raise Exception
    
    except Exception as e:
        flash("Email já cadastrado!", "flash__warning")
        return redirect("/registrar/")
    
@app.route("/users/login/", methods=["POST"])
def loginUser():
    body = {
            "email":request.form["email"], 
            "password":request.form["password"]
        }
    
    try:
        user = User.query.filter_by(email=body["email"]).first().toJson()

        password = crypt(body["password"])
        
        print(password, user["password"])

        if user and password == user["password"]:   
            session["login"] = True 
            session["name"] = user["name"]
            session["email"] = body["email"]
            session["playing"] = False
            session["idprogress"] = user["idprogress"]
            session["idlevel"] = user["idlevel"]

            return redirect("/feed/")
        else:
            raise Exception
        
    except Exception as e:
        print(e)
        flash("Informações inválidas!", "flash__warning")
        return redirect("/login/")

@app.route("/users/recover/", methods=["POST"])
def recoverUser():
    body = {
            "email":request.form["email"]
        }

    try:
        emailSender = "musicateincorporated@gmail.com"
        emailPssword = "toshtcphwlxuknac"
        
        session["email"] = body["email"]
        session["token"] = generateToken()

        email = {
            "subject":"Esqueceu sua senha? Fica de boa :)",
            "body":f"Aqui está o seu código de confirmação: {token}"
        }

        em = EmailMessage()
        em['From'] = emailSender
        em['To'] = body["email"]
        em['Subject'] = email["subject"]

        em.set_content(email["body"])
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(emailSender, emailPssword)
            smtp.sendmail(emailSender, body["email"], em.as_string())

        return redirect(f'/confirmar/')

    except Exception as e:
        print(e)
        flash("Erro ao enviar email!")
        return redirect(f'/esqueceu/')

@app.route("/users/confirm/", methods=["POST"])
def confirmUser():
    body = {
        "token":request.form["token"]
    }

    if session["token"] and body["token"] == session["token"]:
        del session["token"]
        return redirect("/recuperar/")
    
    flash("Token incorreto!", "flash__warning")
    return redirect("/esqueceu/")

@app.route("/users/reset/", methods=["POST"])
def resetUser():
    body = {
        "password":request.form["password"],
        "password_confirmation":request.form["password_confirmation"]
    }

    try:
        user = User.query.filter_by(email=session["email"]).first()
        del session["email"]

        if user and body["password"] == body["password_confirmation"]:
            user.password = body["password"]

            db.session.add(user)
            db.session.commit()

            return redirect("/login/")
        else:
            flash("As senhas não conferem!", "flash__warning")
            return redirect("/esqueceu/")
        
        raise Exception
    
    except Exception as e:
        flash("Algo deu errado!", "flash__warning")
        return redirect("/esqueceu/")

@app.route("/users/update/email", methods=['POST'])
def updateUserEmail():
    body = {
        "email":request.form["email"],
        "password":request.form["password"]
    }
    
    try:
        user = User.query.filter_by(email=session["email"]).first()
        password = crypt(body["password"])
        
        if password == user.toJson()["password"]:
            
            user.email = body["email"]
            session["email"] = body["email"]
            
            db.session.add(user)
            db.session.commit()

            return redirect('/feed/')
            
        raise Exception
    
    except Exception as e:
        flash("senha incorreta!")
        return redirect('/feed/')

@app.route("/users/update/name", methods=['POST'])
def updateUserName():
    body = {
        "name":request.form["name"],
        "password":request.form["password"]
    }
    
    try:
        user = User.query.filter_by(email=session["email"]).first()
        password = crypt(body["password"])
        
        if password == user.toJson()["password"]:
            
            user.name = body["name"]
            session["name"] = body["name"]
            
            db.session.add(user)
            db.session.commit()
            
            return redirect('/feed/')
        
        raise Exception
    
    except Exception as e:
        flash("senha incorreta!")
        return redirect('/feed/')

@app.route("/users/delete", methods=['POST'])
def deleteUser():
    body = {
        "email":request.form["email"],
        "password":request.form["password"]
    }
    
    password = crypt(body["password"])
    
    try:
        user = User.query.filter_by(email=session["email"]).first()
        progress = Progress.query.filter_by(id=session["idprogress"]).first()
        level = Level.query.filter_by(id=session["idlevel"]).first()
    
        print(user)
        
        if user and user.toJson()["password"] == password:
            db.session.delete(user)
            db.session.delete(progress)
            db.session.delete(level )
            db.session.commit()
            
            return redirect("/logout/")
    
        raise Exception
    
    except Exception as e:
        print(e)
        flash("Senha incorreta!")
        return redirect('/feed/')
