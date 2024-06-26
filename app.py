import webview
from screeninfo import get_monitors

def on_loaded(window):
    current_url = window.get_current_url()
    print(f"Current URL: {current_url}")

    # Check if the URL is the specified one, then redirect
    if current_url == "https://staging.garamqu.id/":
        new_url = "https://staging.garamqu.id/cashier/login"
        print(f"Redirecting to: {new_url}")
        window.load_url(new_url)

def main():
    # Get the screen size of the primary monitor
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height

    # Create a webview window with the calculated size
    window = webview.create_window('Kasir', 'https://staging.garamqu.id/cashier/login', width=screen_width, height=screen_height, x=0, y=0, resizable=True)
    
    # Add a hook to the window to handle URL changes
    window.events.loaded += on_loaded
    
    # Start the webview
    webview.start()

if __name__ == '__main__':
    main()
