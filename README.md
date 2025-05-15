# ⌛Nodi
![image](https://github.com/user-attachments/assets/cab15be6-53b9-42b0-a1c3-05a7929f435f)

Nodi is a community time bank web application that makes it easy to share your skills and time with others. Whether you’re offering tutoring, home repairs, or creative workshops, Nodi connects you with people in your community who need your expertise and lets you earn time credits in return. It’s simple, fair, and designed to bring people closer together.


<<<<<<< HEAD
>[!WARNING] 
>🚧 Work in progress – expect changes and improvements!
=======
>>>>>>> eb5da218bd83da963db6af0eb8b115ad8006527f


## 📦 Installation

### Prerequisites

- Python version 3.10 or above
- Django version 5.1.3 or above

### Core Dependencies

#### For Debian/Ubuntu

```bash
# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Install database dependecy
sudo apt install sqlite3
```

#### For Windows

 Install Python 3.10+ from python.org
 Use Git Bash or WSL2 (better option) or Any other Linux distro(an even better option) 

#### For MacOS

```
# Via Homebrew
brew install python3 
```

### Project Setup

1. Clone this repository
```bash
git clone https://github.com/Adil-im/Time_Bank.git
cd Time_Bank
```

2. In the project directory create a virtual Environment(to isolate project-specific dependencies)
```bash
python3 -m venv venv
source venv/bin/activate #Linux/macOS
# On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install requirements.txt
```

4. Database Setup
```bash
python manage.py migrate
```

5. Run the development Server
```bash
python manage.py runserver
```


















 	
