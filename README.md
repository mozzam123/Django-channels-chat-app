# Django-channels-chat-app

## About

This repository contains a basic chat application built with Django and Django Channels. The primary purpose of this project is to demonstrate how WebSockets work in a Django application, enabling real-time communication between users.

### Features

- **Real-time Messaging**: Send and receive messages instantly using WebSockets.
- **User Authentication**: Secure user login and registration.
- **Chat Rooms**: Create and join chat rooms to converse with multiple users.
- **Scalability**: Built using Django Channels to handle multiple connections efficiently.

### Technologies Used

- **Django**: The web framework used to build the application.
- **Django Channels**: Extends Django to handle WebSockets, allowing for real-time communication.
- **Redis**: Used as a channel layer for managing WebSocket connections.
- **JavaScript**: Handles the client-side WebSocket connections.

### Installation

To set up the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Django-channels-chat-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Django-channels-chat-app
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables. Create a `.env` file in the root directory and add the following:

    ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```


8. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

### Usage

After setting up, you can start using the chat application by visiting `http://localhost:8000` in your web browser. Register a new account or log in with an existing account, create or join a chat room, and start messaging in real-time.

### Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcomed.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries or feedback, please reach out to us at [your-email@example.com].
