from app import create_app

print("Creating Flask app...")
app = create_app()
print("App created. Running now.")

if __name__ == "__main__":
    app.run(debug=True)