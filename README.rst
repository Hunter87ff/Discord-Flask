Discord-Flask
=============

.. image:: https://img.shields.io/github/v/release/hunter87ff/Discord-Flask?include_prereleases&label=Latest%20Release&logo=github&sort=semver&style=for-the-badge&logoColor=white
    :target: https://github.com/hunter87ff/Discord-Flask/releases

Discord-Flask is a feature rich extension for Flask, with discord.py like functionalities.

Installation
------------

Install Released Version
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

     pip install Discord-Flask

To install current development version you can use following command:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

     pip install git+https://github.com/hunter87ff/Discord-Flask.git

Basic Example
-------------

.. code-block:: python

     import os
     import traceback
     import config
     from flask import Flask, redirect, url_for, render_template
     from discord_flask import Session, User, requires_authorization
     from discord_flask.exceptions import Unauthorized

     app = Flask(__name__)
     app.guilds = {} #for cache purpose
     app.secret_key = b"SECRET_KEY"
     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"    # !! Only in development environment.

     discord = Session(
          app=app, 
          bot_token="TOKEN", # make sure to access these as secret
          client_id="CLIENT_ID", 
          client_secret="CLIENT_SECRET", 
          redirect_uri="http://127.0.0.1:5000/callback"
     )

     @app.errorhandler(Unauthorized)
     def redirect_unauthorized(e):
          return redirect(url_for("login"))
          
     @app.route("/")
     def home():
          return """<a href="/login/">Login</a>"""

     @app.route("/login/")
     def login():
          return discord.create_session()
          
     @app.route("/callback/")
     def callback():
          try:
                redirect_to = discord.callback().get("redirect", "/dashboard/")
                return redirect(redirect_to)
          except Exception as e:
                traceback.print_exc()
                return render_template("error/500.html"), 500

     @app.route("/dashboard/")
     @requires_authorization
     def dashboard():
          try:
                user:User = discord.fetch_user()
                _guilds_list = []
                _guild_dict = {g.id:g for g in discord.fetch_guilds() if g.permissions.administrator}
                app.guilds = _guild_dict
                return render_template(
                     "dash.html",
                     avatar=user.avatar_url,
                     leng=len(_guilds_list),
                     guilds=_guild_dict.values(),
                     user=user
                )
          except Exception:
                traceback.print_exc()
                return "Something went wrong", 500

     @app.route("/dashboard/<guild_id>/")
     @requires_authorization
     def guild_dashboard(guild_id):
          if not app.guilds:
                app.guilds = {g.id:g for g in discord.fetch_guilds() if g.permissions.manage_guild}
          guild = discord.get_guild(guild_id)
          if not guild:
                return redirect(config.INVITE_URL + guild_id)
          if guild.id not in app.guilds.keys():
                return redirect("/dashboard")
          return render_template("guild.html",guild=guild, config=config) #Change configurations accordingly

     if __name__ == "__main__":
          app.run(host="0.0.0.0", port=5000)

For an example to the working application, check `test_app.py <example/test_app.py>`_.

.. note::
     Documentation is currently not available.
