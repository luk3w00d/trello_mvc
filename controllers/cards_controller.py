from flask import Blueprint
from db import db
from models.card import Card, CardSchema

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route('/')
# @jwt_required()
def all_cards():
    # return 'all_cards route'
    
    stmt = db.select(Card).order_by(Card.priority.desc(), Card.title)
    cards = db.session.scalars(stmt)
    return CardSchema(many=True).dump(cards)

@cards_bp.route('/<int:id>/') # This allows you find a single card from the database by addding / "the id here"
def one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)  
    return CardSchema().dump(card)