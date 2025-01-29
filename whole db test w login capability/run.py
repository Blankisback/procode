from app import create_app  # Import the create_app function from app/__init__.py

# Create the Flask app instance
app = create_app()

# Check if the script is being run directly
if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
