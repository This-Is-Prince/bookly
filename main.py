def main():
    """Starts the Uvicorn server programmatically."""
    import uvicorn
    from src import app
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
