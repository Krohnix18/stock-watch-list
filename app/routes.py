from flask import render_template, request, redirect, url_for
from app import db
from app.models.watchlist_item import WatchlistItem
from flask import current_app as app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        notes = request.form.get("notes")
        if symbol:
            item = WatchlistItem(symbol=symbol.upper(), notes=notes)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for("index"))

    items = WatchlistItem.query.order_by(WatchlistItem.created_at.desc()).all()
    return render_template("index.html", items=items)