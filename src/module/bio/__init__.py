from flask import Blueprint

bp_bio = Blueprint("bio", __name__)

import src.module.bio.controller
