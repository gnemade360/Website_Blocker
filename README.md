# Website_Blocker

# Python Website Blocker

Python Website Blocker is a simple program that blocks access to specific websites during certain hours of the day. It modifies the hosts file on your operating system to redirect the blocked websites to the localhost (127.0.0.1), effectively preventing access to them.

## Getting Started

These instructions will help you run the Website Blocker program on your local machine.

### Prerequisites

- Python 3.x

### Usage

1. Clone this repository or download the `website_blocker.py` file.

2. Open the `website_blocker.py` file in a text editor.

3. Replace the `websites_list` variable with the websites you want to block. For example:

websites_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"


4. Set the `start_hour` and `end_hour` variables to specify the time range during which the websites should be blocked. Use the 24-hour format.

start_hour = 9 # 9 AM
end_hour = 17 # 5 PM


5. Save the changes to the `website_blocker.py` file.

6. Open a terminal or command prompt.

7. Navigate to the directory containing the `website_blocker.py` file.

8. Run the program by executing the following command:

python website_blocker.py

9. The program will continuously run and block the specified websites during the specified time range. To stop the blocking, you can terminate the program (e.g., press Ctrl+C).
