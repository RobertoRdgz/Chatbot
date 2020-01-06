from mongo import app

def start_app():
    app.run(
        host='0.0.0.0',
        port='5004',
        debug=True,
    )


if __name__ == '__main__':
    start_app()
