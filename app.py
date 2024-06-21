import webview

def on_loaded(window):
    current_url = window.get_current_url()
    print(f"Current URL: {current_url}")

    # Check if the URL is the specified one, then redirect
    if current_url == "http://127.0.0.1:8000/":
        new_url = "http://127.0.0.1:8000/cashier/login"
        print(f"Redirecting to: {new_url}")
        window.load_url(new_url)

def main():
    # Create a webview window with the specified URL
    window = webview.create_window('Kasir', 'http://127.0.0.1:8000/cashier/login', fullscreen=True)
    
    # Add a hook to the window to handle URL changes
    window.events.loaded += on_loaded
    
    # Start the webview
    webview.start()

if __name__ == '__main__':
    main()
