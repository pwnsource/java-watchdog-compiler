# Java File Compiler with Watchdog

This Python script monitors changes in Java files within a specified directory and automatically compiles them using `javac` whenever a change is detected. It utilizes the `watchdog` library for file monitoring.

## How to Use

1. **Install Dependencies**: Make sure you have Python installed on your system. Install the required dependencies using pip:

pip install watchdog

2. **Run the Script**: Navigate to the repository directory and run the Python script:

python main.py

Follow the prompts to specify the file or folder to monitor and whether you want to log errors.

3. **Make Changes**: Make changes to Java files within the monitored directory. The script will automatically compile them whenever a change is detected.

4. **Logging (Optional)**: If you chose to log errors, they will be appended to a file named `log.txt` in the repository directory.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.