# Distributed Python App with RPyC

This Python project, named "Distributed Python App with RPyC," is a simple distributed application that utilizes the RPyC (Remote Python Call) framework to create and interact with objects remotely. The project demonstrates the use of RPyC for exposing methods of Python classes as remote services, allowing clients to create and use instances of these classes from a remote server.

## Project Structure

The project consists of the following main components:

1. **app.py**: This module defines several Python classes, including `Vehicle`, `Car`, `Driver`, and `License`, which represent vehicles, cars, drivers, and driver's licenses. These classes have methods that can be remotely exposed and accessed by clients.

2. **decorator.py**: This module contains a custom decorator called `expose`. The decorator is used to expose methods of a class with a modified name, making it easier for clients to access and call these methods remotely.

3. **server.py**: The server module sets up an RPyC service using the `DistributedAppService` class. This service exposes methods for creating instances of the classes defined in `app.py` and allows clients to interact with them remotely. It also handles client connections and disconnections.

4. **client.py**: The client module connects to the RPyC server created in `server.py`. It demonstrates how to create and interact with instances of the classes remotely.

5. **requirements.txt**: This file lists the project's dependencies, including RPyC and Plumbum, which are required for running the project.

## Usage

To run the project, follow these steps:

0. Create new virtual environment and activate it.
    ```bash
   python3 -m venv distributed-python-app-with-rpyc-env
   ```
   
    ```bash
    cd distributed-python-app-with-rpyc-env; source bin/activate
    ```

1. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
2. Start the RPyC server by running server.py:
    
    ```bash
    python server.py
    ```
3. In a separate terminal, run the client script client.py:
    ```bash
    python client.py
    ```
   The client script will connect to the server and demonstrate how to create and interact with instances of the classes defined in app.py remotely.

## License
This project is provided under an open-source license. You can find the licensing information in the LICENSE file.

## Contributors
- `Farhat Shahir Zim`

If you'd like to contribute to this project or have any suggestions, please feel free to reach out to the project's maintainers.

## Contact
For any inquiries or issues related to this project, you can contact `cybertronix.4406@gmail.com`.

## Acknowledgments
This project was created to demonstrate the use of [RPyC package](https://github.com/tomerfiliba-org/rpyc) in building distributed Python applications. We acknowledge the RPyC community for providing this powerful framework.

Thank you for using the "Distributed Python App with RPyC" project! We hope you find it helpful in understanding remote Python service communication.