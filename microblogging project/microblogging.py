from app import app

if __name__ == "__main__":

  with app.app_context():
    # from app import db
    # from app.models import User
    # username = 'rrr'
    # about_me = 'First cry on 13th Oct.Follow me to know more about me...!!! '
    # myuser = User(username=username,
    #               about_me=about_me,
    #               user_email='rrr@gmail.com')
    # myuser.set_password_hash('123')
    # db.session.add(myuser)
    # db.session.commit()
    # print('its u', myuser.password_hash)

    app.run(debug=True)
