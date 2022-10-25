from crypt import methods
from flask import Blueprint, request
from init import db
from datetime import date
from models.card import Card, CardSchema

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route('/')
# @jwt_required()
def get_all_cards():
    # return 'all_cards route'
    
    stmt = db.select(Card).order_by(Card.date.desc()) # This will organize the cards into chosen order
    cards = db.session.scalars(stmt)
    return CardSchema(many=True).dump(cards)

@cards_bp.route('/<int:id>/') # This allows you find a single card from the database by addding /"put the id here"
def get_one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        return CardSchema().dump(card)
    else:
        return {'error': f'card not found with id {id}'}, 404  # This is to cover if the card enterd dose not exist

@cards_bp.route('/<int:id>/', methods=['DELETE']) # This allows you find a single card from the database by addding /"put the id here"
def delete_one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        db.session.delete(card)
        db.session.commit()
        return {'message': f"Card '{card.title}' deleted successfully"}
    else:
        return {'error': f'card not found with id {id}'}, 404

@cards_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
def update_one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        card.title = request.json.get('title') or card.title     # or card.title is a short circuiting if patch is left empty
        card.description = request.json.get('description') or card.description
        card.status = request.json.get('status') or card.status
        card.priority = request.json.get('priority') or card.priority
        db.session.commit()
        return CardSchema().dump(card)
    else:
        return {'error': f'card not found with id {id}'}, 404 # Having 404 at the end means "not found"

@cards_bp.route('/', methods=['POST'])
def create_card():

        card = Card(        # This allows cards to be created in the post section
            title = request.json['title'],
            description = request.json['description'],
            date = date.today(),
            status = request.json['status'],
            priority = request.json['priority']
        )
        # Add and commit user to DB
        db.session.add(card)
        db.session.commit()
        # Respond to client
        return CardSchema().dump(card), 201
   