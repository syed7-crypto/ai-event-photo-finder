from src.drive_auth import authenticate

def main():
    creds = authenticate()
    print("Authentication successful!")
    print(creds)

if __name__ == "__main__":
    main()