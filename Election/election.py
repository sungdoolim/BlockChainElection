from datetime import datetime
 
from flask import Flask, render_template
from views import login, vote, index, election, message
from models import db, db_commit, db_end
from login_manager import login_manager
from flask_util_js import FlaskUtilJs
from blockchain_manager import BlockChainManager
import debugpy
import default_config
app = Flask(__name__)

app.register_blueprint(index.index_page, url_prefix='/')
app.register_blueprint(login.login_page, url_prefix='/login')
app.register_blueprint(vote.vote_page, url_prefix='/vote')
app.register_blueprint(message.message_page, url_prefix='/message')
app.register_blueprint(election.election_page, url_prefix='/election')

#debugpy.listen(("0.0.0.0", 5678))

def init_app():
    app.config.from_object(default_config)
    for logger in app.config.get('LOGGERS', ()):
        app.logger.addHandler(logger)

    JINJA_GLOBAL_FUNCTIONS = {
        
    }

    app.jinja_env.globals.update(JINJA_GLOBAL_FUNCTIONS)

    FlaskUtilJs(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    # blockchain server load
    blockchain_manager = BlockChainManager(app)
    blockchain_manager.load_blockchain_server()

    return app


@app.before_request
def before_request():
    pass

@app.after_request
def after_request(response):
    db_commit()
    db_end()
    return response
