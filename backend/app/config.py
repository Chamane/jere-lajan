class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///expenses.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="ihfbr4kuehbfhubrhubr3uhfbu3h2bf"
    JWT_SECRET_KEY = "jhebuhdb3beihdbjebwrdhjbjqw"
    SWAGGER = {
        "title": "Jere Lajan API",
        "uiversion": 3,
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        }
    }