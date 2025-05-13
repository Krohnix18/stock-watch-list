from flask import render_template, request, redirect, url_for
from app import db
from app.models.watchlist_item import WatchlistItem
from flask import current_app as app
from app.schemas.watchlist import WatchlistItemSchema
from pydantic import ValidationError

@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        symbol = request.form.get("symbol")
        notes = request.form.get("notes")

        try:
            validated = WatchlistItemSchema(symbol=symbol, notes=notes)
            item = WatchlistItem(symbol=validated.symbol, notes=validated.notes)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for("index"))
        except ValidationError as e:
            error = e.errors()[0]['msg']

    items = WatchlistItem.query.order_by(WatchlistItem.created_at.desc()).all()
    return render_template("index.html", items=items, error=error)